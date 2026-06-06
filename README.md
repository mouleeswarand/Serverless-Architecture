# Serverless-Architecture

# AWS Lambda and Boto3 Automation Assignments

## Overview

This repository contains four AWS automation assignments completed using **AWS Lambda**, **Python**, and **Boto3**. The main goal of these assignments is to understand how cloud automation works in real-world AWS environments.

The assignments focus on automating common cloud administration tasks such as managing EC2 instances, cleaning up old S3 files, creating EBS snapshots, and automatically tagging EC2 instances during launch.

## Assignments Completed

| Assignment   | Title                                | Main AWS Services Used                    |
| ------------ | ------------------------------------ | ----------------------------------------- |
| Assignment 1 | Automated EC2 Instance Management    | EC2, Lambda, IAM, Boto3                   |
| Assignment 2 | Automated S3 Bucket Cleanup          | S3, Lambda, IAM, Boto3                    |
| Assignment 4 | Automatic EBS Snapshot and Cleanup   | EC2, EBS, Lambda, IAM, Boto3, EventBridge |
| Assignment 5 | Auto-Tagging EC2 Instances on Launch | EC2, Lambda, IAM, Boto3, EventBridge      |

---

## Assignment 1: Automated EC2 Instance Management Using AWS Lambda and Boto3

### Summary

This assignment automates the process of starting and stopping EC2 instances based on their tags. Two EC2 instances were created with different tag values.

One instance was tagged with `Action = Auto-Stop`, and another instance was tagged with `Action = Auto-Start`. The Lambda function checks the tags and performs the required action automatically.

### What Was Implemented

* Created two EC2 instances.
* Added tags to identify which instance should be started or stopped.
* Created an IAM role for Lambda with EC2 permissions.
* Created a Lambda function using Python and Boto3.
* Used Boto3 to describe, start, and stop EC2 instances.
* Tested the Lambda function manually from the AWS Lambda console.
* Verified the result in the EC2 dashboard.

### Learning Outcome

This assignment helped me understand how AWS Lambda can be used to automate EC2 instance management and how EC2 tags can be used for automation decisions.

---

## Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

### Summary

This assignment automates the cleanup of old files from an S3 bucket. The Lambda function checks files inside a specific S3 bucket and deletes files that are older than the defined number of days.

This type of automation is useful for reducing unnecessary storage usage and controlling AWS S3 storage costs.

### What Was Implemented

* Created an S3 bucket.
* Uploaded test files into the bucket.
* Created an IAM role for Lambda with S3 permissions.
* Created a Lambda function using Python and Boto3.
* Used Boto3 to list objects in the S3 bucket.
* Checked the last modified date of each file.
* Deleted files that matched the old-file condition.
* Verified the result in the S3 bucket.

### Learning Outcome

This assignment helped me understand how to automate S3 file management using Lambda and Boto3. It also gave me practical knowledge about storage cleanup and cost optimization.

---

## Assignment 4: Automatic EBS Snapshot and Cleanup Using AWS Lambda and Boto3

### Summary

This assignment automates the backup process for an EBS volume by creating snapshots using AWS Lambda and Boto3. The Lambda function also checks for old snapshots and deletes snapshots older than the defined retention period.

This type of automation is useful for backup management and cost control.

### What Was Implemented

* Identified an EBS volume from the EC2 dashboard.
* Created an IAM role for Lambda with EC2/EBS permissions.
* Created a Lambda function using Python and Boto3.
* Used Boto3 to create a snapshot of the selected EBS volume.
* Added tags to identify snapshots created by Lambda.
* Checked existing snapshots.
* Deleted old snapshots based on the retention period.
* Configured EventBridge Schedule to run the Lambda function automatically.
* Verified snapshot creation in the EC2 Snapshots section.

### Learning Outcome

This assignment helped me understand EBS volume backups, snapshot automation, snapshot cleanup, and how EventBridge can be used to schedule Lambda functions.

---

## Assignment 5: Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3

### Summary

This assignment automates the process of tagging EC2 instances when they are launched. An EventBridge rule detects when an EC2 instance enters the running state and triggers a Lambda function.

The Lambda function retrieves the instance ID from the event and adds custom tags such as `CreatedBy`, `LaunchDate`, and `Project`.

### What Was Implemented

* Created an IAM role for Lambda with EC2 permissions.
* Created a Lambda function using Python and Boto3.
* Created an EventBridge rule with an EC2 instance state-change event pattern.
* Configured the rule to trigger when an EC2 instance enters the running state.
* Added Lambda as the target for the EventBridge rule.
* Launched a new EC2 instance for testing.
* Verified that tags were automatically added to the EC2 instance.

### Learning Outcome

This assignment helped me understand event-driven automation in AWS. I learned how EventBridge can detect EC2 state changes and trigger Lambda automatically.

---

## Repository Structure

```text
aws-lambda-boto3-assignments/
│
├── Assignment 1: Automated Instance Management/
│   ├── lambda_function.py
│   ├── README.md
│   └── screenshots/
│
├── Assignment 2: Automated S3 Bucket Cleanup/
│   ├── lambda_function.py
│   ├── README.md
│   └── screenshots/
│
├── Assignment 4: Automatic EBS Snapshot and Cleanup/
│   ├── lambda_function.py
│   ├── README.md
│   └── screenshots/
│
├── Assignment 5: Auto-Tagging EC2 Instances on Launch/
│   ├── lambda_function.py
│   ├── README.md
│   └── screenshots/
│
└── README.md
```

---

## Skills Learned

Through these assignments, I gained hands-on experience with:

* AWS Lambda function creation
* IAM role and permission configuration
* Python Boto3 automation
* EC2 instance start and stop automation
* S3 file cleanup automation
* EBS snapshot backup and cleanup
* EventBridge rule and schedule configuration
* EC2 auto-tagging using events
* CloudWatch Logs for troubleshooting
* AWS resource management and cost optimization

---

## Testing and Verification

Each assignment was tested manually or automatically depending on the requirement.

* Lambda test events were used to verify function execution.
* AWS Console was used to confirm EC2, S3, and EBS changes.
* CloudWatch Logs were checked to verify execution logs and troubleshoot errors.
* Screenshots were captured for documentation and submission.

---

## Conclusion

These four assignments provided practical knowledge of AWS automation using Lambda and Boto3. They helped me understand how cloud engineers automate daily operational tasks such as server management, storage cleanup, backup creation, and resource tagging.

This project improved my understanding of AWS services, IAM permissions, Python scripting, and event-driven cloud automation.
