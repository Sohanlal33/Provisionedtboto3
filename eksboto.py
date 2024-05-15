#Eks cluster information
import boto3

client = boto3.client('eks', region_name= "us-east-1")
clusters = client.list_clusters()['clusters']

for cluster in cluster:
    response = client.describe_cluster(
        name = cluster 
    )
    cluster_info = response ['cluster']
    cluste_status = cluster_info['status']
    cluste_endpoint = cluster_info['endpoint']
    cluste_version = cluster_info['version']

    print(f"cluster {cluster} status is {cluster_status}")
    print(f"cluster endpont : {cluster_endpoint}")
    print(f"cluster version :  {cluster_version}")
    
