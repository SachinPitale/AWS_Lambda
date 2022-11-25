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
    print("The volume id is: {}\n AZ: {}\n volume type: {}\n ".format(each_item['VolumeId'],each_item['AvailabilityZone'],each_item['VolumeType']))

response=ec2_client.describe_volumes()['Volumes']
for each_item in response:
    # print(each_item['InstanceId'])
    # print(each_item['State'])
    print("###########################################################")
    print(each_item['Attachments'])
    for i in each_item['Attachments']:
        print(i['AttachTime'])
        print(i['Device'])

