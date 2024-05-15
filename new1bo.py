#python is language and boto3 is AWs library-monitoring, Backups & Schedule Tasks
#we can add web interface ,library and diff. functionalities
#pip install boto3

#then import it in file

import boto3


#then use aws cli and check with cmd ls ~/ .aws it will show config-default region and output format 
#& credentials option- secret key pair---if file show it is already configured

#Check and use boto3 documention for more
#we need function name,we need to call and datatypes 

ec2_client = boto3.client('ec2')

all_available_vpcs = ec2_client.describe_vpcs() 
print(all_available_vpcs["Vpcs"])

for vpc in Vpcs:
    print(vpc["VpcId"])
    cidr_block_assoc_sets = vpc["CidrBlockAssociationSet"]
    for assoc_set in cidr_block_asscoc_sets:
        print(assoc_set["CidrBlockState"])    #shows vpc id and associated state










