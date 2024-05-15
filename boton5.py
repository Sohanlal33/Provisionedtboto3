#Ex.Which instance are in which state

#created 3 ec2 instance through terraform 
import boto3
import schedule        #library added for scheduled tasks

#for region 
import boto3

# for region
ec2_client = boto3.client('ec2', region_name="us-east-1") 
ec2_resource = boto3.resource('ec2', region_name="us-east-1")

# Describe instances
reservations = ec2_client.describe_instances()

for reservation in reservations['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance {instance['InstanceId']} is {instance['State']['Name']}")

statuses = ec2_client.describe_instance_status(
    IncludeAllInstances=True
)
for status in statuses ['InstanceStatuses']:
    ins_status = status['InstanceStatus']['Status']
    sys_status = status['SystemStatus']['Status']
    state =status['InstanceState']['Name']
    print(f"Instance {status['InstanceId']} is {status} with instance status {ins-status} and system status {sys_status}")
    print("#########################################\n") 

schedule.every(5).seconds.do(check_instance_status)

while True:
    schedule.run_pending()