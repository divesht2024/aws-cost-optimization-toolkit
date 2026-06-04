# 💰 AWS Cost Optimization Toolkit

Serverless automation to detect and eliminate unnecessary AWS resource costs using Lambda, EventBridge, SNS, and Python (Boto3).

Zero manual intervention required after deployment — fully automated, scheduled, and alerting.

---

## 🏆 Key Achievements

- ✅ Automated detection of stale resources across 4 AWS service categories
- ✅ Real-time SNS email alerts for immediate cost action
- ✅ EC2 auto-scheduling reduces compute costs during non-business hours
- ✅ Each Lambda function uses least-privilege IAM role — zero over-permissioning
- ✅ Zero manual intervention required after initial deployment

---
## 📦 What This Toolkit Covers

| Module | What It Detects | Action |
|--------|----------------|--------|
| EBS Volume Cleanup | Unattached EBS volumes | SNS alert + Auto delete |
| Elastic IP Cleanup | Unused Elastic IPs | SNS alert + Auto release |
| S3 Cost Optimization | Oversized / unoptimized S3 buckets | SNS alert + Auto cleanup |
| EC2 Scheduler | Running EC2 instances during non-business hours | Auto shutdown + startup |

---

## 🏗️ Architecture

![Architecture Diagram](architecture-diagram.png)

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
                                        │
                                        ▼
                               CloudWatch Logs
                               (execution logs per Lambda)
```

---

## 🔄 How It Works

```
1. EventBridge triggers Lambda on cron schedule
        ↓
2. Lambda scans AWS resources using Python (Boto3)
        ↓
3. Stale/unused resource detected?
        ↓
4. SNS publishes real-time alert to subscribed email
        ↓
5. Engineer receives alert → takes cleanup action
        ↓
6. EC2 Scheduler — stops instances after business hours
   automatically starts them before next business day
```

---

## 🛠️ Tech Stack

| Service | Role |
|---------|------|
| **AWS Lambda** | Serverless compute for all automation logic |
| **Amazon EventBridge** | Cron-based scheduling of Lambda functions |
| **Amazon SNS** | Real-time cost alert notifications via email |
| **AWS IAM** | Least-privilege roles and policies per Lambda |
| **Python (Boto3)** | AWS SDK for resource scanning and automation |
| **CloudWatch Logs** | Lambda execution logs and failure monitoring |

---

## 📂 Project Structure

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

## 🚀 Setup & Deployment

### Prerequisites
- AWS Account with appropriate permissions
- Python 3.9+
- AWS CLI configured (`aws configure`)
- Boto3 installed (`pip install boto3`)

### Step 1 — Clone the repository
```bash
git clone https://github.com/divesht2024/aws-cost-optimization-toolkit.git
cd aws-cost-optimization-toolkit
```

### Step 2 — Create SNS Topic and subscribe your email
```bash
aws sns create-topic --name cost-optimization-alerts

aws sns subscribe \
  --topic-arn <YOUR_TOPIC_ARN> \
  --protocol email \
  --notification-endpoint your-email@example.com
```

### Step 3 — Deploy each Lambda function
```bash
# Zip the function
zip function.zip lambda_function.py

# Create Lambda
aws lambda create-function \
  --function-name ebs-cleanup \
  --runtime python3.9 \
  --role <YOUR_IAM_ROLE_ARN> \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://function.zip
```

### Step 4 — Set environment variables for each Lambda
```
SNS_TOPIC_ARN = <your-sns-topic-arn>
AWS_REGION    = ap-south-1
```

### Step 5 — Create EventBridge rules
```bash
aws events put-rule \
  --name ebs-cleanup-schedule \
  --schedule-expression "cron(0 8 * * ? *)"
```

---

## ⏰ EventBridge Cron Schedules

| Lambda Function | Schedule | Description |
|----------------|----------|-------------|
| EBS Cleanup | `cron(0 8 * * ? *)` | Daily at 8 AM UTC |
| Elastic IP Cleanup | `cron(0 8 * * ? *)` | Daily at 8 AM UTC |
| S3 Optimization | `cron(0 9 * * ? *)` | Daily at 9 AM UTC |
| EC2 Stop | `cron(0 13 * * ? *)` | Daily at 1 PM UTC |
| EC2 Start | `cron(0 4 * * ? *)` | Daily at 4 AM UTC |

---

## 🔐 IAM — Least Privilege Per Lambda

Each Lambda has its own IAM role with only the permissions it needs:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeVolumes",
        "sns:Publish",
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
```

No Lambda has admin access. No shared IAM roles across functions.

---

## 📊 Results

- Automated detection of stale resources across 4 AWS service categories
- Real-time SNS email alerts for immediate cost action
- EC2 auto-scheduling reduces compute costs during non-business hours
- Zero manual intervention required after deployment
- CloudWatch Logs provide full visibility into every Lambda execution

---

## 👨‍💻 Author

**Divesh M. Tayade**
- 🐙 GitHub: [@divesht2024](https://github.com/divesht2024)
- 💼 LinkedIn: [linkedin.com/in/divesh-tayade](https://www.linkedin.com/in/divesh-tayade-4a010124a/)
- 📧 diveshtayade20@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
