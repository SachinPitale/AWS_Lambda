import boto3
from pprint import pprint


aws_console=boto3.session.Session()
ec2_console=aws_console.client('ec2', region_name='us-east-1')

#ec2_console.start_instances(instance_id=['i-06186ed7e182cc28b'])
response=ec2_console.describe_instances(InstanceIds=['i-06186ed7e182cc28b'])
#pprint(response)
print(response['Reservations'])