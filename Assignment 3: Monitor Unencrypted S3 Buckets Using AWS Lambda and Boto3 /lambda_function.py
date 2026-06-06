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
