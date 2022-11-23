import boto3

aws_console=boto3.session.Session()

iam_client=aws_console.client('iam', region_name='us-east-1')
e2_client=aws_console.client('ec2', region_name='us-east-1')
s3_client=aws_console.client('s3', region_name='us-east-1')


iam_response=iam_client.list_users()
print(iam_response)

for each_iteam in iam_response:
    print(each_iteam)

for each_iteam in iam_response['users']:
    print(each_iteam)

for each_iteam in iam_response['users']:
    print(each_iteam['UserName'])

