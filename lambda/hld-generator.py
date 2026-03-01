import json
import boto3
import math

s3 = boto3.client("s3")
bedrock = boto3.client("bedrock-runtime", region_name="eu-west-1")

BUCKET_NAME = "hld-generator-brd-bucket"
EMBED_MODEL = "amazon.titan-embed-text-v2:0"
LLM_MODEL = "anthropic.claude-3-haiku-20240307-v1:0"

def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

def get_embedding(text):
    response = bedrock.invoke_model(
        modelId=EMBED_MODEL,
        body=json.dumps({
            "inputText": text
        })
    )
    
    result = json.loads(response["body"].read())
    return result["embedding"]

def cosine_similarity(vec1, vec2):
    dot = sum(a*b for a,b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a*a for a in vec1))
    norm2 = math.sqrt(sum(b*b for b in vec2))
    return dot / (norm1 * norm2)

def lambda_handler(event, context):
    
    file_name = event["file_name"]
    
    # 1. Read BRD from S3
    response = s3.get_object(Bucket=BUCKET_NAME, Key=file_name)
    brd_text = response["Body"].read().decode("utf-8")
    
    # 2. Chunk BRD
    chunks = chunk_text(brd_text)
    
    # 3. Create embeddings for each chunk
    chunk_embeddings = []
    
    for chunk in chunks:
        embedding = get_embedding(chunk)
        chunk_embeddings.append((chunk, embedding))
    
    # 4. Create query embedding
    query = "Generate High Level Design"
    query_embedding = get_embedding(query)
    
    # 5. Find top 3 relevant chunks
    similarities = []
    
    for chunk, emb in chunk_embeddings:
        score = cosine_similarity(query_embedding, emb)
        similarities.append((chunk, score))
    
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_chunks = [item[0] for item in similarities[:3]]
    
    context_text = "\n\n".join(top_chunks)
    
    # 6. Generate HLD using Claude
    prompt = f"""
    You are a cloud architect.
    Based on the following business requirements:
    
    {context_text}
    
    Generate output in JSON format:
    {{
        "project_name": "",
        "overview": "",
        "architecture_summary": "",
        "aws_services": [],
        "security": "",
        "availability": "",
        "integrations": [],
        "assumptions": ""
    }}
    """
    
    llm_response = bedrock.invoke_model(
        modelId=LLM_MODEL,
        body=json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 1000,
            "anthropic_version": "bedrock-2023-05-31"
        })
    )
    
    llm_result = json.loads(llm_response["body"].read())
    output_text = llm_result["content"][0]["text"]
    
    hld_data = json.loads(output_text)
    
    # 7. Convert JSON to HTML
    html_content = f"""
    <html>
    <head><title>{hld_data['project_name']} - HLD</title></head>
    <body>
    <h1>High Level Design</h1>
    <h2>Overview</h2>
    <p>{hld_data['overview']}</p>
    <h2>Architecture</h2>
    <p>{hld_data['architecture_summary']}</p>
    <h2>AWS Services</h2>
    <ul>{''.join(f'<li>{s}</li>' for s in hld_data['aws_services'])}</ul>
    </body>
    </html>
    """
    
    output_file = "generated_HLD.html"
    
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=output_file,
        Body=html_content,
        ContentType="text/html"
    )
    
    return {
        "statusCode": 200,
        "message": "HLD generated successfully",
        "output_file": output_file
    }
