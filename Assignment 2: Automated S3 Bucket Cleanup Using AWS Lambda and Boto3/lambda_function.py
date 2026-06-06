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
