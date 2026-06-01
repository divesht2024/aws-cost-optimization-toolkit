# AWS Cost Optimization Toolkit

Serverless automation to detect and eliminate unnecessary AWS resource costs using Lambda, EventBridge, SNS, and Python (Boto3).

---

## Overview

This toolkit automates the detection of stale and unused AWS resources that silently increase your AWS bill. It runs on a scheduled basis using EventBridge cron expressions and sends real-time SNS alerts for immediate action.

### What it covers:

| Module | What it detects | Action |
|--------|----------------|--------|
| EBS Volume Cleanup | Unattached EBS volumes | SNS alert |
| Public IP Cleanup | Unused Elastic IPs | SNS alert |
| S3 Cost Optimization | Oversized / unoptimized S3 buckets | SNS alert |
| EC2 Scheduler | Running EC2 instances during non-business hours | Auto shutdown & startup |

---

## Architecture

```
EventBridge (Cron Schedule)
        │
        ▼
  AWS Lambda (Python/Boto3)
        │
        ├── Scan EBS Volumes   ──► Unattached? ──► SNS Alert
        ├── Scan Elastic IPs   ──► Unused?     ──► SNS Alert
        ├── Scan S3 Buckets    ──► Oversized?  ──► SNS Alert
        └── EC2 Scheduler      ──► Stop/Start EC2 instances
```

---

## Tech Stack

- **AWS Lambda** — Serverless compute for all automation logic
- **Amazon EventBridge** — Cron-based scheduling of Lambda functions
- **Amazon SNS** — Real-time cost alert notifications
- **AWS IAM** — Least-privilege roles and policies per Lambda function
- **Python (Boto3)** — AWS SDK for resource scanning and automation
- **CloudWatch Logs** — Lambda execution logs and monitoring

---

## Project Structure

```
aws-cost-optimization-toolkit/
│
├── ebs-cleanup/
│   ├── lambda_function.py       # Detects unattached EBS volumes
│   ├── iam_policy.json          # IAM policy for EBS Lambda
│   └── README.md
│
├── elastic-ip-cleanup/
│   ├── lambda_function.py       # Detects unused Elastic IPs
│   ├── iam_policy.json          # IAM policy for EIP Lambda
│   └── README.md
│
├── s3-cost-optimization/
│   ├── lambda_function.py       # Scans S3 buckets for cost issues
│   ├── iam_policy.json          # IAM policy for S3 Lambda
│   └── README.md
│
├── ec2-scheduler/
│   ├── lambda_function.py       # Auto stop/start EC2 instances
│   ├── iam_policy.json          # IAM policy for EC2 Lambda
│   └── README.md
│
├── eventbridge/
│   └── cron_rules.md            # EventBridge cron expressions used
│
├── sns/
│   └── sns_setup.md             # SNS topic and subscription setup
│
├── architecture-diagram.png     # Architecture diagram
└── README.md                    # This file
```

---

## Setup & Deployment

### Prerequisites
- AWS Account with appropriate permissions
- Python 3.9+
- AWS CLI configured (`aws configure`)
- Boto3 installed (`pip install boto3`)



---

## EventBridge Cron Schedules

| Lambda Function | Schedule | Description |
|----------------|----------|-------------|
| EBS Cleanup | `cron(0 8 * * ? *)` | Daily at 8 AM UTC |
| Elastic IP Cleanup | `cron(0 8 * * ? *)` | Daily at 8 AM UTC |
| S3 Optimization | `cron(0 9 * * ? *)` | Daily at 9 AM UTC |
| EC2 Stop | `cron(0 13 * * ? *)` | Daily at 1 PM UTC (after business hours) |
| EC2 Start | `cron(0 4 * * ? *)` | Daily at 4 AM UTC (before business hours) |

---

## Results

- Automated detection of stale resources across 4 AWS service categories
- Real-time SNS email alerts for immediate cost action
- EC2 auto-scheduling reduces compute costs during non-business hours
- Zero manual intervention required after deployment

---

## Author

**Divesh M. Tayade**
- GitHub: [@divesht2024](https://github.com/divesht2024)
- LinkedIn: [linkedin.com/in/divesh-tayade](https://www.linkedin.com/in/divesh-tayade-4a010124a/)

---
