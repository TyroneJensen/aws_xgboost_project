import json
import boto3
import requests


def lambda_handler(event, context):
    # Fetch data from endpoint
    response = requests.get("http://your-endpoint.com/data")
    data = response.json()
    
    # Process data (example: extract relevant fields)
    processed_data = process_data(data)
    
    # Store data in S3
    s3 = boto3.client('s3')
    s3.put_object(Bucket='your-bucket-name', Key='data/processed_data.json', Body=json.dumps(processed_data))
    
    # Trigger AWS Glue Crawler to update Athena table
    glue = boto3.client('glue')
    glue.start_crawler(Name='your-glue-crawler-name')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data processed and stored successfully!')
    }

def process_data(data):
    # Example processing function
    return [{'field1': item['field1'], 'field2': item['field2']} for item in data]
