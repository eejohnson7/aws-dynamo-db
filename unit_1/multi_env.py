'''
Fantastic job so far! Now, we're advancing to a more complex task in our course. Consider a scenario where you are working 
in AWS with Python's boto3, and you need to manage multiple environments. For this, you are required to write a Python script 
that creates an AWS Session using specific credentials and then creates both a resource and a client instance for DynamoDB 
using that session. Additionally, you need to create resource and client instances with the default AWS Session.
'''

import boto3

# TO DO: Create an AWS session with explicit credentials 'test' / 'test' and region 'us-west-2'
aws_session = boto3.Session(
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-west-2'
)

# TO DO: Create a DynamoDB resource based on the session
aws_dynamodb_resource = aws_session.resource('dynamodb')

# TO DO: Create a DynamoDB client based on the session
aws_dynamodb_client = aws_session.client('dynamodb')

# TO DO: Create a default DynamoDB resource with the default session
dynamodb_resource = boto3.resource('dynamodb')

# TO DO: Create a default DynamoDB client with the default session
dynamodb_client = boto3.client('dynamodb')
