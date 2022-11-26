import boto3

aws_console=boto3.session.Session()
ec2_con_res=aws_console.resource('ec2')
ebs_filter={"Name":"status","Values":['available']}
response=ec2_con_res.volumes.filter(Filters=[ebs_filter])
for each_iteam in response:
    print(each_iteam.tags,each_iteam.id,each_iteam.state)
