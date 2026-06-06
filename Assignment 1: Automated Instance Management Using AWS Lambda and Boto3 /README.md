# Assignment 1: Automated Instance Management Using AWS Lambda and Boto3

## Short Summary
The Goal here is to Start and Stop the EC2 Instances based on the EC2 Tags. We are going to automate this using Lambda function with proper IAM roles to it

## AWS Service used
1) EC2 Instances
2) IAM Roles and Policies
3) Lambda Fumction
4) CloudWatch for Logs

## Instructions
1) Create a 2 EC2 Instances and Tag the name (Auto-Start / Auto-Stop)

   ### EC2 Instance 1 - TAG:
   
   `Name : Auto Start`
   
   `Action: Auto-Start`
   
   `Current Status: Stopped`
   
   ### EC2 Instance 2- TAG:
   
   `Name: Auto Stop`
   
   `Action: Auto-Stop`
   
   `Current Status: Running`

<img width="817" height="643" alt="image" src="https://github.com/user-attachments/assets/bd5edc91-996e-4290-9f51-a0a08ec1f324" />

   
2) Provide proper permisssion in IAM Roles and policy so that Lambda can able to `Describe the EC2 Instance and to Check for the Logs`

   ### IAM ROLE and POLICY
   
   `IAM Role: lambda-ec2-start-stop-role`
   
   `IAM Policy: AmazonEC2FullAccess`

   <img width="1267" height="456" alt="image" src="https://github.com/user-attachments/assets/05321b90-ba0d-47aa-97a3-bbf44266f87c" />

3) Create a New Lambda function and Map the Roles and implement the Python code with Boto3
   
   `Function Name: ec2-auto-start-stop`
   
   `Runtime: Python 3.14`

   `Execution role: lambda-ec2-start-stop-role` 
  
   
4)  Finally Deploy and Test the code that should automate the EC2 Instance Auto-Start / Auto- Stop

   ###Deploy the Python Code `lambda_function.py`


    import boto3
    
    ec2 = boto3.client('ec2')
    
    def lambda_handler(event, context):
        stopped_instances = []
        started_instances = []
    
        # Find instances with Action = Auto-Stop
        auto_stop_response = ec2.describe_instances(
            Filters=[
                {'Name': 'tag:Action', 'Values': ['Auto-Stop']},
                {'Name': 'instance-state-name', 'Values': ['running']}
            ]
        )
    
        for reservation in auto_stop_response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                ec2.stop_instances(InstanceIds=[instance_id])
                stopped_instances.append(instance_id)
    
        # Find instances with Action = Auto-Start
        auto_start_response = ec2.describe_instances(
            Filters=[
                {'Name': 'tag:Action', 'Values': ['Auto-Start']},
                {'Name': 'instance-state-name', 'Values': ['stopped']}
            ]
        )
    
        for reservation in auto_start_response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                ec2.start_instances(InstanceIds=[instance_id])
                started_instances.append(instance_id)
    
        return {
            'Stopped Instances': stopped_instances,
            'Started Instances': started_instances
        }

    ## Test the Code
    <img width="323" height="243" alt="image" src="https://github.com/user-attachments/assets/9e86a835-564a-4854-a14a-50689407d5b2" />

5)  Check the EC2 Instance Status
   <img width="568" height="183" alt="image" src="https://github.com/user-attachments/assets/975cdf12-1a19-4258-85bb-e48ab39bd2fc" />


## Final Output

As per the Output the EC2 Instance Start / Stop is automated through Lambda Function suing Python Code

### Before Lambda Function

<img width="817" height="643" alt="image" src="https://github.com/user-attachments/assets/bd5edc91-996e-4290-9f51-a0a08ec1f324" />

### After lambda Function - Auto Start / Stop

<img width="568" height="183" alt="image" src="https://github.com/user-attachments/assets/c06b5263-9173-4f10-82cb-5323da43353b" />








