import boto3

aws_console=boto3.session.Session()

ec2_client=aws_console.client('ec2', region_name="us-east-1")

response=ec2_client.describe_volumes()
print(response)

print("###########################################################")

response=ec2_client.describe_volumes()['Volumes']
print(response)

print("###########################################################")

response=ec2_client.describe_volumes()['Volumes']
for each_item in response:
    # print(each_item['InstanceId'])
    # print(each_item['State'])
    print("###########################################################")
    print(each_item['VolumeId'])