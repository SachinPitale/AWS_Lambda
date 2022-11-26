import boto3

aws_console=boto3.session.Session()
ec2_client=aws_console.client('ec2')

#response=ec2_client.describe_volumes()['Volumes']
#print(response)
# for each_item in ec2_client.describe_volumes()['Volumes']:
#     print(each_item['VolumeId'], each_item['State'])
#     try:
#         if each_item['Tags']:
#             print(each_item['Tags'])
#     except:
#         print("Tags is not avaliable for {each_item['VolumeId']}")


response=ec2_client.describe_volumes()['Volumes']
for each_item in response:
    if not "Tags" in each_item and each_item['State']=='available':
        print(each_item['VolumeId'], each_item['State'])
