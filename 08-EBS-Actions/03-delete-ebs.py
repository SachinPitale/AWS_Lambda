import boto3

aws_console=boto3.session.Session()

ec2_client=aws_console.client('ec2')

response=ec2_client.describe_volumes()['Volumes']
for each_item in response:
    try:
        tags=each_item['Tags']
        print(tags)
        attach_tags=[i['Key'] for i in tags]
        if 'support-group' in attach_tags:
            print(each_item['VolumeId'], each_item['State'])
    except:
        print(f"Volume doesn't contain tags {each_item['VolumeId']}")