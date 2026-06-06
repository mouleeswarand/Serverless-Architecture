# Assignment 5: Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3

## Short Summary
This assignment automates the tagging of EC2 instances when they are launched. An EventBridge rule detects when an EC2 instance enters the running state and triggers a Lambda function.

The Lambda function uses Python Boto3 to retrieve the instance ID from the event and adds custom tags such as `CreatedBy`, `LaunchDate`, and `Project`. This helps improve resource tracking and cost management in AWS.

## AWS Services Used
- AWS EC2
- AWS Lambda
- IAM
- Boto3
- Amazon EventBridge
- CloudWatch Logs

## Implementation Steps
### 1. Created an IAM role for Lambda with EC2 and CloudWatch Logs permissions.
   
   `Role Name: lambda-ec2-auto-tag-role`
   
    `Policies: AmazonEC2FullAccess, AWSLambdaBasicExecutionRole`
   

  <img width="1296" height="478" alt="image" src="https://github.com/user-attachments/assets/9d8872e3-378d-4e13-991e-ad46f607d043" />

### 2. Created a Lambda function using Python.

   `Function name: ec2-auto-tag-on-launch`

   `Runtime: Python 3.12`

   `Execution role: lambda-ec2-auto-tag-role`
   
### 3. Used Boto3 to add tags to an EC2 instance.
```
  import boto3
  from datetime import datetime
    
  ec2 = boto3.client('ec2')
     def lambda_handler(event, context):
        print("Received event:", event)
            try:
            # Get instance ID from EventBridge event
            instance_id = event['detail']['instance-id']
    
            # Get today's date
            current_date = datetime.now().strftime('%Y-%m-%d')
    
            # Add tags to the newly launched EC2 instance
            ec2.create_tags(
                Resources=[instance_id],
                Tags=[
                    {
                        'Key': 'CreatedBy',
                        'Value': 'Lambda'
                    },
                    {
                        'Key': 'LaunchDate',
                        'Value': current_date
                    },
                    {
                        'Key': 'Project',
                        'Value': 'AutoTaggingDemo'
                    }
                ]
            )
    
            print(f"Tags added successfully to instance: {instance_id}")
    
            return {
                'statusCode': 200,
                'message': f'Tags added successfully to instance {instance_id}'
            }
    
        except Exception as error:
            print("Error:", str(error))
    
            return {
                'statusCode': 500,
                'message': str(error)
            }
   ```

<img width="1349" height="641" alt="image" src="https://github.com/user-attachments/assets/6616f298-623c-4565-9ca7-05e310998c64" />

## Deploy the Lambda Function

  ### EC2 Instance - Before the Lambda function 

<img width="791" height="697" alt="image" src="https://github.com/user-attachments/assets/bfab25cb-38ec-47ce-bef2-fa6f1f344423" />

  ### EC2 Instance - After the Lambda function - New Tags Created

<img width="768" height="703" alt="image" src="https://github.com/user-attachments/assets/9fe07f0f-9c81-4b6b-966a-f757af10db8a" />


### 4. Created an EventBridge rule to detect EC2 running state changes.
```
Name: ec2-launch-auto-tag-rule
Rule type: Rule with an event pattern
Choose: Event source: AWS Service events
AWS service: EC2
Event type: EC2 Instance State-change Notification
Specific state: running
```

### 5. Added the Lambda function as the EventBridge target.
```
Target type: AWS service
Target: Lambda function
Function: ec2-auto-tag-on-launch
```

<img width="1152" height="666" alt="image" src="https://github.com/user-attachments/assets/57d7f6b6-45d1-4b75-9761-3e47b2488dff" />

### 6. Launched a new EC2 instance for testing and Verified that tags were automatically added to the instance.

## Testing
A new EC2 instance was launched to trigger the EventBridge rule. Once the instance entered the running state, the Lambda function executed automatically and added the required tags.


## Output
The EC2 instance was successfully tagged automatically with `CreatedBy`, `LaunchDate`, and `Project`.

<img width="782" height="752" alt="image" src="https://github.com/user-attachments/assets/c4123e26-e772-4a8f-a638-c806123ae6e5" />

