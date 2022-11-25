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