
import boto3

#for region 
ec2_client = boto3.client('ec2', region_name="us-east-1") 
ec2_resource = boto3.resource('ec2', region_name="us-east-1")

#Vpc creation
new_vpc = ec2_resource.create_vpc(
    CidrBlock="10.0.1.0/16"
)

new_vpc.create_subnet(
    CidrBlock="10.0.1.0/24"
)

new_vpc.create_subnet(
    CidrBlock="10.0.2.0/24"
)

new_vpc.create_tags(
    Tags=[
        {
            'Key':'Name',
            'Value' : 'New-vpc-1'
        },
    ]
)

all_available_vpcs = ec2_client.describe_vpcs() 
print(all_available_vpcs["Vpcs"])

for vpc in vpcs:
    print(vpc["VpcId"])
    cidr_block_assoc_sets = vpc["CidrBlockAssociationSet"]
    for assoc_set in cidr_block_asscoc_sets:
        print(assoc_set["CidrBlockState"])  

#Output with 2 VpcIds and their states 