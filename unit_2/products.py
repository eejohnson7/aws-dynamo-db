'''
Great progress on your DynamoDB journey! In this task, you are provided with a Python script that initiates a DynamoDB table 
named Products with ProductId as the primary key. Your task is to modify the script to include a range key called Manufacturer 
for each product. Additionally, add a waiter to ensure the table is fully created before the script continues, and then list 
all tables to verify the new structure. The waiter should poll every 2 seconds and make a maximum of 10 attempts.
'''

import boto3

# Initialize a boto3 resource for DynamoDB
dynamodb = boto3.resource('dynamodb')

# The script below creates a table. Modify it to include Manufacturer as a range key.
dynamodb.create_table(
    TableName='Products',
    KeySchema=[
        {
            'AttributeName': 'ProductId',
            'KeyType': 'HASH'  # Primary key
        },
        # TODO: Define Manufacturer as the range key
        {
            'AttributeName': 'Manufacturer',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ProductId',
            'AttributeType': 'S'
        },
        # TODO: Add attribute definition for Manufacturer
        {
            'AttributeName': 'Manufacturer',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

# TODO: Implement a waiter to ensure the table is fully created before proceeding; make it poll every 2 seconds for a maximum of 10 attempts
waiter = dynamodb.meta.client.get_waiter('table_exists')
waiter.wait(TableName='Products', WaiterConfig={'Delay': 2, 'MaxAttempts': 10})

# TODO: List all DynamoDB tables to confirm the table creation
print("Existing tables:", [table.name for table in dynamodb.tables.all()])