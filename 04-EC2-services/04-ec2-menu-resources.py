import boto3
import sys

aws_console=boto3.session.Session()
ec2_con_re=aws_console.resource("ec2",region_name="us-east-1")

while True:
    print("Script will perform following operations")
    print("""
        start: 1,
        stop: 2
        terminate: 3
        exit: 4
    """)

    opt=int(input("Enter your option: "))
    if opt==1:
        instance_id=input("Enter your instance id: ")
        my_req_instance_object=ec2_con_re.Instance(instance_id)
        print("Starting ec2 instance.....")
        my_req_instance_object.start()
    elif opt==2:
        instance_id=input("Enter your instance id: ")
        print("Stopping ec2 instance.....")
        my_req_instance_object=ec2_con_re.Instance(instance_id)
        my_req_instance_object.stop()
    elif opt==3:
        instance_id=input("Enter your instance id: ")
        my_req_instance_object=ec2_con_re.Instance(instance_id)
        print("Terminating ec2 instance.....")
        my_req_instance_object.terminate()
    elif opt==4:
        print("Thank you for using this script")
        sys.exit()
    else:
        print("Your option is invalid. Please try once again")
