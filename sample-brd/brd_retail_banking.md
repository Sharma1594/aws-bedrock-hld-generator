Business Requirements Document (BRD)

Project Name: Digital Retail Banking Platform
Client: ABC Bank UK
Version: 1.0
Date: 15 Feb 2026

1. Business Objective

- ABC Bank wants to build a secure, scalable digital banking platform to:
- Allow customers to view accounts
- Transfer funds
- Pay bills
- Apply for loans
- Access via web and mobile

2. Functional Requirements

- Users must authenticate using multi-factor authentication.
- System must support 1 million users.
- Funds transfer should process within 5 seconds.
- Admin portal required for internal operations team.
- Audit logs must be maintained for all transactions.

3. Non-Functional Requirements

- Availability: 99.95%
- Data encryption at rest and in transit
- GDPR compliant
- PCI-DSS compliant
- RPO: 15 minutes
- RTO: 30 minutes

4. Integration Requirements

- Core Banking System (on-premise)
- Payment Gateway API
- Credit Score Agency API

5. Constraints

- Must be hosted in AWS London region
- Use managed AWS services where possible
- High security is mandatory
