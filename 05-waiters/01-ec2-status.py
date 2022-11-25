import boto3
from pprint import pprint


aws_console=boto3.session.Session()
ec2_console=aws_console.resource('ec2', region_name='us-east-1')

# #ec2_console.start_instances(instance_id=['i-06186ed7e182cc28b'])
# response=ec2_console.describe_instances(InstanceIds=['i-06186ed7e182cc28b'])
# #pprint(response)
# #print(response['Reservations'])
# for each_iteam in (response['Reservations']):
#     print("########################")
#     pprint(each_iteam)

my_inst=ec2_console.Instance("i-06186ed7e182cc28b")
print("Starting given instance")
my_inst.start()

while True:
    my_inst_obj=ec2_console.Instance("i-06186ed7e182cc28b")
    print(f"The current state of ec2: {my_inst_obj.state['Name']}")
    if my_inst_obj.state['Name'] == "running":
        break
        print("Wating instance to be up")
        time.sleep(5)

print("instance is up and running")

