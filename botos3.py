import boto3

# Created S3 client 
s3_client = boto3.client('s3')

def create_s3_bucket(bucket_name, region='us-east-1'):
    try:
        # Created S3 bucket
        response = s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'us-east-1'
            }
        )
        print("Bucket created successfully:", bucket_name)
        print(response)
    except Exception as e:
        # Print any errors that occur during the process
        print("Error:", str(e))




