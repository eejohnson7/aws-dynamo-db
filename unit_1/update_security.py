'''
For this task, we're going to deepen our understanding of AWS DynamoDB by altering some code. Currently, the provided script 
uses hardcoded access credentials to establish a session with AWS. As this is generally not considered good practice in terms 
of security, your task will be to adapt the code to use a default AWS session instead. Modify the code in the starter prompt 
accordingly and re-run the script.
'''

import boto3

# Create an AWS session with explicit credentials and a region
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY_ID',
    aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
    region_name='us-west-2'
)

# TODO: Modify these resources and client creations to not rely on the explicit session above

# Create a DynamoDB resource based on the session
dynamodb_resource = boto3.resource('dynamodb')

# Create a DynamoDB client based on the session
dynamodb_client = boto3.client('dynamodb')