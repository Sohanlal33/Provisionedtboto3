#Ex.Which instance are in which state

#created 3 ec2 instance through terraform 
import boto3

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

    
