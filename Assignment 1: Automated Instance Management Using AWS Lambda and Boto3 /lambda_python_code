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
