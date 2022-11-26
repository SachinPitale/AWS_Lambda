import boto3

aws_console=boto3.session.Session()

ec2_client=aws_console.client('ec2')

response=ec2_client.describe_volumes()['Volumes']
for each_item in response:
    try:
        tags=each_item['Tags']
        print(tags)
    except:
        print(f"Volume doesn't contain tags {each_item['VolumeId']}")