import boto3

aws_console=boto3.session.Session()

sts_session=aws_console.client('sts', region_name="us-east-1")

response=sts_session.get_caller_identity()
print(response)
print(response['UserId'])
print(response['Account'])