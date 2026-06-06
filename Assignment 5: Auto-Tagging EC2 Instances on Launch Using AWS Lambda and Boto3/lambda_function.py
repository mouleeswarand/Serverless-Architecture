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
