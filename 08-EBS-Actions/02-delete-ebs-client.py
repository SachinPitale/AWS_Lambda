import boto3

aws_console=boto3.session.Session()
ec2_client=aws_console.client('ec2')

#esponse=ec2_client.describe_volumes()['Volumes']
#print(response)
for each_item in ec2_client.describe_volumes()['Volumes']:
    print(each_item['VolumeId'], each_item['State'])
    try:
        if each_item['Tags']:
            print(each_item['Tags'])
    except:
        print(f"Tags is not avaliable for {each_item['VolumeId']}")