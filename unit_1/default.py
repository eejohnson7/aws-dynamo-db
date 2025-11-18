'''
Advancing through our journey with Boto3! In this task, your job is to extend the functionality of the provided Python script. 
The script already initializes an AWS session using explicit access credentials and a region and creates a DynamoDB resource 
and client based on that session. Now, you must create a default DynamoDB resource and client using the default Boto3 session. 
Utilize your knowledge of setting up default sessions to assist in creating these new resources and clients.
'''

import boto3

# Create an AWS session with explicit credentials and region
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY_ID',
    aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
    region_name='us-west-2'
)

# Create a DynamoDB resource based on the session
dynamodb_resource = session.resource('dynamodb')

# Create a DynamoDB client based on the session
dynamodb_client = session.client('dynamodb')

# TODO: Create a default DynamoDB resource with the default session
default_resource = boto3.resource('dynamodb')

# TODO: Create a default DynamoDB client with the default session
default_client = boto3.client('dynamodb')