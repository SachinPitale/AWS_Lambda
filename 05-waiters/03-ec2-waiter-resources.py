import boto3
import time

aws_con=boto3.session.Session()
ec2_con_re=aws_con.resource('ec2',region_name="us-east-1")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-1")


my_inst_ob=ec2_con_re.Instance("i-002d4110f1199166f")
print("Starting given instance....")
my_inst_ob.start()
my_inst_ob.wait_until_running()  #Resource waiter waits for 200sec(40 checks after every 5 sec)
print("Now your instance is up and running")