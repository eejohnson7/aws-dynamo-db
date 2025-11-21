'''
Great progress! You have been tasked with setting up a DynamoDB table named Orders, storing order data for an e-commerce 
platform. However, it seems there is a mistake in the provided Python script. Please inspect the script, identify the issue, 
and rectify it. Once fixed, execute the script and ensure the creation of the DynamoDB table named Orders with OrderId as the 
primary key.
'''

import boto3

# Initialize a boto3 client for DynamoDB
dynamodb = boto3.client('dynamodb')

dynamodb.create_table(
    TableName='Orders',
    KeySchema=[
        {
            'AttributeName': 'OrderId',
            'KeyType': 'HASH'  # Primary key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'OrderId',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)