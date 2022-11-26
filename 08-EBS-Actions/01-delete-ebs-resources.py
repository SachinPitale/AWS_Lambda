import boto3

aws_console=boto3.session.Session()
ec2_con_res=aws_console.resource('ec2')
ec2_client=aws_console.client('ec2')
waiter = ec2_client.get_waiter('volume_deleted')
ebs_filter={"Name":"status","Values":['available']}
response=ec2_con_res.volumes.filter(Filters=[ebs_filter])
for each_iteam in response:
    if not each_iteam.tags:
        print(each_iteam.tags,each_iteam.id,each_iteam.state)
        print("deleting a untagged volumes.........")
        each_iteam.delete()
        waiter.wait(VolumeIds=[each_iteam.id])
        print(f"{each_iteam.id} got deleted")