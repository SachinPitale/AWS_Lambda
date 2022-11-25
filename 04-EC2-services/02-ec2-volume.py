import boto3

aws_console=boto3.session.Session()

ec2_client=aws_console.client('ec2', region_name="us-east-1")

response=ec2_client.describe_volumes()
print(response)