import boto3
import sys

aws_console=boto3.session.Session()
ec2_client=aws_console.client('ec2', region_name='us-east-1')

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
        print("Starting ec2 instance.....")
        ec2_client.start_instances(InstanceIds=[instance_id])
    elif opt==2:
        instance_id=input("Enter your instance id: ")
        print("Stopping ec2 instance.....")
        ec2_client.stop_instances(InstanceIds=[instance_id])
    elif opt==3:
        instance_id=input("Enter your instance id: ")
        print("Terminating ec2 instance.....")
    elif opt==4:
        print("Thank you for using this script")
        sys.exit()
    else:
        print("Your option is invalid. Please try once again")
