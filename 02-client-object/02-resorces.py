import boto3

ima_res=boto3.session.Session()

for each_item in ima_res.users.all():
    print(each_item)