# Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

## Short Summary
The Goal here is to Cleanup the files and folders inside the bucket. We are going to automate this using Lambda function with proper IAM roles to it

## AWS Service used
1) S3 Bucket
2) IAM Roles and Policies
3) Lambda Function
4) CloudWatch for Logs

## Instructions
### 1. Create a S3 Bucket and upload some test files

   ### S3 Bucket Information
   `Bucket Name: s3-cleanup-demo1`

   <img width="962" height="362" alt="image" src="https://github.com/user-attachments/assets/35251a2f-efc1-4065-bc89-4f7f7caaba03" />


   
### 2. Provide proper permisssion in IAM Roles and policy so that Lambda can able to `Describe the EC2 Instance and to Check for the Logs`

   ### IAM ROLE and POLICY
   
   `IAM Role: lambda-s3-cleanup-role`
   
   `IAM Policy: AmazonS3FullAccess`

   <img width="614" height="480" alt="image" src="https://github.com/user-attachments/assets/1d52fef0-a5ce-49bd-bcae-076860960127" />


### 3. Create a New Lambda function and Map the Roles and implement the Python code with Boto3 to delete the older files from S3 Bucket
   
   `Function Name: s3-old-file-cleanup`
   
   `Runtime: Python 3.12`

   `Execution role: lambda-s3-cleanup-role` 
  
   
### 4.  Finally Deploy and Test the code that should delete the files and folders from S3 Bucket

   ### Deploy the Python Code `lambda_function.py`
   
    import boto3
    from datetime import datetime, timezone, timedelta
    
    s3 = boto3.client('s3')
    
    BUCKET_NAME = 's3-cleanup-demo1'
    DAYS_OLD = 0
    
    def lambda_handler(event, context):
        deleted_files = []
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=DAYS_OLD)
    
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    
        if 'Contents' not in response:
            return {
                'message': 'No files found in bucket'
            }
    
        for obj in response['Contents']:
            file_name = obj['Key']
            last_modified = obj['LastModified']
    
            if last_modified < cutoff_date:
                s3.delete_object(Bucket=BUCKET_NAME, Key=file_name)
                deleted_files.append(file_name)
    
        return {
            'Deleted Files': deleted_files,
            'Message': 'Cleanup completed'
        }

    

  ## Test the Code
    
  <img width="1038" height="426" alt="image" src="https://github.com/user-attachments/assets/3818f156-41a1-40c4-9b3b-e2de5c94be50" />



### 5.  Check the S3 Bucket Status
   <img width="1339" height="337" alt="image" src="https://github.com/user-attachments/assets/706955d4-60e5-4438-a2d0-316b707eaa0d" />


## Final Output

As per the Output the S3 Bucket files and folders got delted automatically hrough Lambda Function suing Python BOTO3 Code

### Before Lambda Function

<img width="962" height="362" alt="image" src="https://github.com/user-attachments/assets/35251a2f-efc1-4065-bc89-4f7f7caaba03" />

### After lambda Function - S3 Bucket file gets deleted 

<img width="1339" height="337" alt="image" src="https://github.com/user-attachments/assets/e2649887-f944-482c-ba81-a6123924323d" />










