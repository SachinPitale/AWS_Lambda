import boto3
aws_mag_con=boto3.session.Session()
ec2_con_re=aws_mag_con.resource("ec2")

sts_con_cli=aws_mag_con.client("sts")
response=sts_con_cli.get_caller_identity()
my_own_id=response.get('Account')

for each_snap in ec2_con_re.snapshots.filter(OwnerIds=[my_own_id]):
	print(each_snap)