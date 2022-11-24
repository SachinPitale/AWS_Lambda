import boto3

aws_console=boto3.session.Session()
iam_res=aws_console.resource('iam', region_name="us-east-1")

for each_item in iam_res.users.all():
    print(each_item)
    print(dir(each_item))
    print(each_item.user_name)
    print(each_item.AccessKey)