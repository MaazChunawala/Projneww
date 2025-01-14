import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    file = event['file']
    bucket_name = 'your-bucket-name'
    s3.put_object(Bucket=bucket_name, Key='your-file.pdf', Body=file)
    return {'statusCode': 200, 'body': 'File uploaded successfully'}