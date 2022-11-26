import boto3

aws_console=boto3.session.Session()
ec2_con_res=aws_console.resource('ec2')

response=ec2_con_res.volumes.all()
for each_iteam in response:
    print(each_iteam)
