import boto3
aws_mag_con=boto3.session.Session()
ec2_con_re=aws_mag_con.resource("ec2")

for each_item in ec2_con_re.meta.client.describe_regions()['Regions']:
	print(each_item['RegionName'])