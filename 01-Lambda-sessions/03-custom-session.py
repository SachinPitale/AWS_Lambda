import boto3

aws_con=boto3.session.Session()
iam_res=aws_con.resource('iam',region_name="us-east-1")
iam_con=aws_con.client(service_name='iam',region_name="us-east-1")