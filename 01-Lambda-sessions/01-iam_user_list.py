import boto3

aws_console=boto3.session.Session() #it will give aws console access programatically.
iam_con=aws_console.resource('iam')

for each_user in iam_con.users.all():
    print (each_user)