import boto3
import csv

csv_ob=open("inventory_info.csv","w",newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["S_NO","Instance_Id",'Instance_Type','Architecture','LaunchTime','Privat_Ip'])
aws_console=boto3.session.Session()
ec2_res=aws_console.resource('ec2')
response=ec2_res.instances.all()

for each in response:
    print(each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address)
    csv_w.writerow([cnt,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address])

csv_ob.close()
    