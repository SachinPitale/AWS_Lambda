import  boto3
from pprint import pprint

aws_console=boto3.session.Session()
ec2_client=aws_console.client('ec2', region_name='us-east-1')

response=ec2_client.describe_instances()
pprint(response)

response=ec2_client.describe_instances()['Reservations']
pprint(response)

response=ec2_client.describe_instances()['ResponseMetadata']
pprint(response)


response=ec2_client.describe_instances()['Reservations']
pprint(response)

for each_item in response:
    for each in each_item['instances']:
        print("The Image Id is: {}\nThe Instance Id Is: {}\nThe Instance Launch Time is: {}".format(each['ImageId'],each['InstanceId'],each['LaunchTime'].strftime("%Y-%m-%d")))