# Assignment 4: Automatic EBS Snapshot and Cleanup Using AWS Lambda and Boto3

## Short Summary
We going to take a Backup snapshot automatically and deletes old snapshots older than 30 days using Lambda Function + Python with BOTO3

## AWS Service used
1) EC2 Instance - EBS Volumes and Snapshot
2) IAM Roles and Policies
3) Lambda Function
4) CloudWatch for Logs

## Instructions
1) Navigate to EC2 Instance -> Volumes
2) Copy the Volume ID to take a Snapshot Backup
   `Volume ID: vol-09a88c1d726fb1498`

3) Provide proper permisssion in IAM Roles and policy so that Lambda can able to `Describe the EC2 Instance`

   ### IAM ROLE and POLICY
   
   `IAM Role: lambda-ebs-snapshot-role`
   
   `IAM Policy: AmazonEC2FullAccess`

   <img width="962" height="468" alt="image" src="https://github.com/user-attachments/assets/5aea61ad-4740-43b2-a273-1b796bb45c5a" />



5) Create a New Lambda function and Map the Roles and implement the Python code with Boto3 to take the shanpshot of the volume 
   
   `Function Name: ebs-snapshot-cleanup`
   
   `Runtime: Python 3.14`

   `Execution role: lambda-ebs-snapshot-role` 
  
   
6)  Finally Deploy and Test the code that should take the snapshot of the volume and to delete the unused snapshot

   ###Deploy the Python Code `lambda_function.py`
   
      import boto3
      from datetime import datetime, timezone, timedelta
      
      ec2 = boto3.client('ec2')
      
      VOLUME_ID = 'vol-09a88c1d726fb1498'
      RETENTION_DAYS = 30
      
      def lambda_handler(event, context):
          created_snapshot = None
          deleted_snapshots = []
      
          # Create snapshot
          snapshot_response = ec2.create_snapshot(
              VolumeId=VOLUME_ID,
              Description=f'Automated backup for volume {VOLUME_ID}'
          )
      
          created_snapshot = snapshot_response['SnapshotId']
      
          # Add tag to snapshot
          ec2.create_tags(
              Resources=[created_snapshot],
              Tags=[
                  {'Key': 'CreatedBy', 'Value': 'LambdaBackup'},
                  {'Key': 'VolumeId', 'Value': VOLUME_ID}
              ]
          )
      
          # Cleanup old snapshots
          cutoff_date = datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)
      
          snapshots = ec2.describe_snapshots(
              OwnerIds=['self'],
              Filters=[
                  {'Name': 'tag:CreatedBy', 'Values': ['LambdaBackup']},
                  {'Name': 'tag:VolumeId', 'Values': [VOLUME_ID]}
              ]
          )
      
          for snapshot in snapshots['Snapshots']:
              snapshot_id = snapshot['SnapshotId']
              start_time = snapshot['StartTime']
      
              if start_time < cutoff_date:
                  ec2.delete_snapshot(SnapshotId=snapshot_id)
                  deleted_snapshots.append(snapshot_id)
      
          return {
              'Created Snapshot': created_snapshot,
              'Deleted Old Snapshots': deleted_snapshots
          }
    

  ## Test the Code
    
  <img width="1001" height="365" alt="image" src="https://github.com/user-attachments/assets/3c28f9ff-2b5f-4c8e-a4d9-b1872f275e80" />




5)  Check the Snapshot 
   <img width="1470" height="152" alt="image" src="https://github.com/user-attachments/assets/506ddde8-9400-45ea-8e2e-b3f562d47d71" />



## Final Output

As per the Output We have created a automatic snapshot using Lambda Function and Python BOTO3 Code from EBS Volume

### After lambda Function - Snapshot gets created  

<img width="1470" height="152" alt="image" src="https://github.com/user-attachments/assets/3488077b-8c88-470c-833b-8ca0cfca9885" />

6) To Delete the snapshot Changing the `RETENTION_DAYS = 0` this will delete the currently created snapshot and I will change it back to `RETENTION_DAYS = 30`

## Test Code
<img width="971" height="392" alt="image" src="https://github.com/user-attachments/assets/ee924e83-9478-450a-ac2c-0c441227ad90" />

## Deleted Screenshot 

<img width="1262" height="195" alt="image" src="https://github.com/user-attachments/assets/8f444dca-2595-460b-9ec0-8a5b4c33500a" />















