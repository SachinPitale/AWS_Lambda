import boto3

aws_con=boto3.session.Session()
list_s3=boto3.resource('s3')

for i in list_s3.buckets_all():
    print(i)