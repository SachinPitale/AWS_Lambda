import boto3
import datetime
session=boto3.session.Session()
iam_con_re=session.resource("iam")
#Get details of any iam user

'''
iam_user_ob=iam_con_re.User("s3_developer")
print(iam_user_ob.user_name,iam_user_ob.user_id,iam_user_ob.arn,iam_user_ob.create_date.strftime("%Y-%m-%d"))
'''
for iam_group_ob in iam_con_re.groups.all():
	print(iam_group_ob)
