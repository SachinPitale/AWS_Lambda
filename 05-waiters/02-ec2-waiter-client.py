import boto3
import time

aws_console=boto3.session.Session()
ec2_console=aws_console.client('ec2', region_name='us-east-1')

ec2_console.start_instances(InstanceIds=['i-06186ed7e182cc28b'])
print("Instance is pending state")
waiter = ec2_console.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-06186ed7e182cc28b'])
print("Ec2 instance is running")
