import boto3

aws_con=boto3.session.Session()
list_s3=aws_con.resource('s3')

print(list_s3)
# for i in list_s3.buckets_all():
#     print(i)
