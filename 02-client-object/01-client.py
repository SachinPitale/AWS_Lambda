import boto3

aws_console=boto3.session.Session()

iam_client=aws_console.client('iam', region_name='us-east-1')
e2_client=aws_console.client('ec2', region_name='us-east-1')
s3_client=aws_console.client('s3', region_name='us-east-1')

## List IAM user
iam_response=iam_client.list_users()
print(iam_response)

for each_iteam in iam_response:
    print(each_iteam)

for each_iteam in iam_response['Users']:
    print(each_iteam)

for each_iteam in iam_response['Users']:
    print(each_iteam['UserName'])

## List EC2 instances

e2_response=e2_client.describe_instances()
print(e2_response)

for each_item in e2_response['Reservations']:
    for each_instance in each_item['Instances']:
        print(each_instance['InstanceId'])

## List S3 buckets

s3_response=s3_client.list_buckets()
print(s3_response)