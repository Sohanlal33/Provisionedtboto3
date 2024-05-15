#pip install boto3

#then import it in file

import boto3


#then use aws cli and check with cmd ls ~/ .aws it will show config-default region and output format 
#& credentials option- secret key pair---if file show it is already configured

#Check and use boto3 documention for more
#we need function name,we need to call and datatypes 
#for region 
ec2_client = boto3.client('ec2', region_name="us-east-1") # added specific  region 

all_available_vpcs = ec2_client.describe_vpcs() 
print(all_available_vpcs["Vpcs"])
for vpc in vpcs:
    print(vpc["VpcId"])
    cidr_block_assoc_sets = vpc["CidrBlockAssociationSet"]
    for assoc_set in cidr_block_asscoc_sets:
        print(assoc_set["CidrBlockState"])    