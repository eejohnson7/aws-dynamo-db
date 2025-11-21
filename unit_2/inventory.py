'''
In this task, you will challenge your understanding of how to modify the table creation settings in DynamoDB utilizing Boto3. 
The provided Python script creates a DynamoDB table named Inventory, with ItemId as the primary key. However, the table 
provisioning is currently set to the On-Demand billing mode. Your assignment is to adjust this setting to Provisioned 
Throughput and set both the read and write capacity units to 10. After making the necessary adjustments, execute the updated 
script and verify the changes in the table creation settings.
'''

import boto3

# Initialize a boto3 resource for DynamoDB
dynamodb = boto3.resource('dynamodb')

# The script below creates a table with ItemId as a String type.
table = dynamodb.create_table(
    TableName='Inventory',
    KeySchema=[
        {
            'AttributeName': 'ItemId',
            'KeyType': 'HASH' # Primary key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'ItemId',
            'AttributeType': 'S'
        }
    ],
    # BillingMode='PAY_PER_REQUEST' # On-Demand billing mode
    ProvisionedThroughput={'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10}
)

print("Table creation initiated. Table status:", table.table_status)