# ☁️ AWS Boto3 Automation

> **AWS infrastructure automation using Python and Boto3**

A collection of Python scripts for hands-on practice with core AWS services including **VPC, EC2, S3, IAM, and RDS**.

## 🏗️ Architecture

```text
                    AWS CLOUD
                        │
                       VPC
                  10.0.0.0/16
                        │
                     Subnet
                  10.0.1.0/24
                        │
          ┌─────────────┼─────────────┐
          │             │             │
    Internet        Route Table   Security Group
    Gateway              │             │
          │              └──────┬──────┘
          │                     │
          └──────────────────► EC2
                                │
                         ┌──────┴──────┐
                         │             │
                        S3            RDS
```

## 🛠️ Tech Stack

* Python
* Boto3
* Amazon Web Services (AWS)
* Git & GitHub

## ☁️ AWS Services

* **VPC** — VPC, Subnets, Internet Gateway, Route Tables
* **EC2** — Instance creation and management
* **S3** — Bucket, upload and download operations
* **IAM** — Identity and access management
* **RDS** — Database operations

## 📂 Files

| File                | Description                       |
| ------------------- | --------------------------------- |
| `aws_vpc_ec2_s3.py` | Complete VPC, EC2 and S3 workflow |
| `awsdemo.py`        | Basic Boto3 demonstration         |
| `vpc.py`            | Create VPC                        |
| `subnet.py`         | Create subnet                     |
| `internet.py`       | Create Internet Gateway           |
| `route.py`          | Configure Route Table             |
| `security.py`       | Configure Security Group          |
| `ec2.py`            | EC2 operations                    |
| `stopec2.py`        | Stop EC2 instance                 |
| `createB.py`        | Create S3 bucket                  |
| `upload.py`         | Upload file to S3                 |
| `download.py`       | Download file from S3             |
| `iamdemo.py`        | IAM operations                    |
| `rdsdemo.py`        | RDS operations                    |
| `rdsstop.py`        | Stop RDS instance                 |

## 🚀 Setup

Install Boto3:

```bash
pip install boto3
```

Configure AWS credentials:

```bash
aws configure
```

Run a script:

```bash
python vpc.py
```

## 🔄 Workflow

```text
VPC
 ↓
Subnet
 ↓
Internet Gateway
 ↓
Route Table
 ↓
Security Group
 ↓
EC2
 ↓
S3 / RDS
```

## 🔐 Security

Never commit real AWS credentials, secret keys, `.pem` files, or `.env` files to GitHub.

Use **AWS CLI, environment variables, or IAM roles** for credentials.

## ⚠️ Note

Some AWS resources may incur charges. Stop or delete resources after testing.

## 👩‍💻 Author

**Shruti P. Sangvikar**

## 📚 Educational Use

This project is created for **educational and learning purposes** to practice AWS cloud services, infrastructure concepts, and Python-based automation using Boto3.

