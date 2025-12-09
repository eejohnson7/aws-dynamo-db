'''
Great job! This time, we are refining our interaction skills with AWS DynamoDB. Before running the provided Python script, 
you are tasked with modifying it. Specifically, you need to update the Students table that we've been working with by 
modifying the attributes of a particular student record. Here’s what you need to do:

Change the name attribute from John Doe to John Smith for the student with student_id of 1.
Add a new attribute email with the value john.smith@example.com for the same student record.
Important Note: Running scripts can modify the resources in our AWS simulator. To revert to the initial state, you can use 
the reset button located in the top right corner. However, keep in mind that resetting will erase any code changes. To 
preserve your code during a reset, consider copying it to the clipboard.
'''

import boto3
import time

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table
table_name = 'Students'
table_names = [table.name for table in dynamodb.tables.all()]

if table_name in table_names:
    table = dynamodb.Table(table_name)
else:
    table = dynamodb.create_table(
        TableName=table_name,
        AttributeDefinitions=[
            {
                'AttributeName': 'student_id',
                'AttributeType': 'N'
            }
        ],
        KeySchema=[
            {
                'AttributeName': 'student_id',
                'KeyType': 'HASH'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

# Wait for the table to be created
dynamodb.meta.client.get_waiter('table_exists').wait(
    TableName='Students',
    WaiterConfig={
        'Delay': 2,  # Poll every 2 seconds
        'MaxAttempts': 10  # Stop after 20 seconds
    }
)

# TODO: Modify the PutItem code below to change the name from 'John Doe' to 'John Smith' and add a new attribute 'email' with the value 'john.smith@example.com'

# Put a data item in the table with PutItem
table.put_item(
    Item={
        'student_id': 1,
        'name': 'John Smith',
        'age': 22,
        'major': 'Computer Science',
        # Add new attribute 'email' here
        'email': 'john.smith@example.com'
    }
)

# List all items in the created table
response = table.scan()

for item in response['Items']:
    print(item)