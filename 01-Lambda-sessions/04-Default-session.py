import boto3


iam_res=boto3.resource('iam', region_name='us-east-1')
ec2_res=boto3.resource('ec2',region_name='us-east-1')