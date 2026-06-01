import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    instance_id = "i-01d7b13317c5f520b"

    ec2.start_instances(
        InstanceIds=[instance_id]
    )

    print(f"Started EC2 instance: {instance_id}")

    return {
        "statusCode": 200,
        "body": "EC2 started successfully"
    }
