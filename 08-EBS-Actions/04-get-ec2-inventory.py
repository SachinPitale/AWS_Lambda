import boto3

aws_console=boto3.session.Session()

ec2_res=aws_console.resource('ec2')

response=ec2_res.instances.all()

for each in response:
    print(each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address,each.tags)