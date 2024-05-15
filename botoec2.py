
#Data backup of ec2 instances--backup ec2 volumes automate creating snapshots
#created instance and snapshot ---tag-Name = prod

import boto3
import schedule

#Created EC2
ec2_client = boto3.client('ec2',region_name="us-east-1")

def create_volume_snapshots():
    try:
        
        volumes = ec2_client.describe_volumes(
            Filters=[
                {
                    'Name' : 'tag:Name',
                    'Value' : ['prod']  # 'Value' : ['prod','Staging','UAT','Dev']
                }
            ]
        )
            #print(volume['Volumes'])

        for volume in volume['Volume']:
            new_snapshot = ec2_client.create_snapshot(
                VolumeId = volume ['VolumeId'] 
        )
            print("snapshot created for volume:", volume['VolumeId'])  #print errors that occurs during the process
            print(new_snapshot)
    
    except Exception as e:
        print("Error;",str(e))

schedule.every().day.do(create_volume_snapshots)   #snapshot for daily 

while True:
    schedule.run_pending()


