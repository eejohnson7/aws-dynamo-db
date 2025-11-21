'''
In your final task, you will synthesize what you have learned so far and write a script that creates two DynamoDB tables — 
Users and Customers. For the Users table, you should use a provisioned capacity mode with a read and write capacity of 5. 
For the Customers table, apply the on-demand capacity mode. Each table should have only one attribute serving as a primary 
key: username in Users, and customer_id in Customers. After successfully creating the tables, implement a command to display 
all of your existing DynamoDB tables.

In this task, you will use wait_until_exists() for the Users table to automatically wait for the table to become active. For 
the Customers table, configure a custom waiter object to poll every 2 seconds and make a maximum of 10 attempts to check the 
status of the table.
'''

import boto3

# TODO: Initialize the boto3 DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# TODO: Create the 'Users' table with Provisioned Throughput and a primary key of 'username'
table_provisioned = dynamodb.create_table(
    TableName='Users',
    KeySchema=[
        {'AttributeName': 'username', 'KeyType': 'HASH'},  # Partition key
    ],
    AttributeDefinitions=[
        {'AttributeName': 'username', 'AttributeType': 'S'},  # String type
    ],
    ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}  # Specify capacity
)

# TODO: Use `wait_until_exists()` for the 'Users' table
table_provisioned.wait_until_exists()

# TODO: Create the 'Customers' table with On-Demand capacity and a primary key of 'customer_id'
table_on_demand = dynamodb.create_table(
    TableName='Customers',
    KeySchema=[{'AttributeName': 'customer_id', 'KeyType': 'HASH'}],
    AttributeDefinitions=[{'AttributeName': 'customer_id', 'AttributeType': 'S'}],
    BillingMode='PAY_PER_REQUEST'
)

# TODO: Configure a custom waiter for the 'Customers' table which polls every 2 seconds and makes 10 attempts
waiter = dynamodb.meta.client.get_waiter('table_exists')
waiter.wait(TableName='Customers', WaiterConfig={'Delay': 2, 'MaxAttempts': 10})

# TODO: List all the existing tables in DynamoDB
print("Existing tables:", [table.name for table in dynamodb.tables.all()])