'''
This is the final task for this lesson! You've been doing great so far, and now it's time to put everything together. In this 
exercise, you are tasked with interacting with an existing AWS DynamoDB table named Students, which already has student_id as 
the primary key. Populate this table with a few records, ensuring each record includes student_id, name, age, and major. 
Utilize conditional expressions to prevent overwriting existing records. Lastly, query and print all items from the Students 
table.

Ready to take on the challenge? Remember all the skills and knowledge you've acquired so far, and good luck!

Important Note: Running scripts can modify the resources in our AWS simulator. To revert to the initial state, you can use 
the reset button located in the top right corner. However, keep in mind that resetting will erase any code changes. To 
preserve your code during a reset, consider copying it to the clipboard.
'''

import boto3

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
        'Delay': 2, 
        'MaxAttempts': 10
    }
)

# TO DO: Add a student item to the table
table.put_item(
    Item={
        'student_id': 1,
        'name': 'Erin Johnson',
        'age': 25,
        'major': 'Computer Science'
    }
)
# TO DO: Use a BatchWriteItem operation to add multiple student items to the table
with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'student_id': 2,
            'name': 'Logan Square',
            'age': 24,
            'major': 'Data Analytics'
        }
    )
    batch.put_item(
        Item={
            'student_id': 3,
            'name': 'Roscoe Village',
            'age': 23,
            'major': 'Psychology'
        }
    )
# TO DO: Try to add another item with the same primary key as an existing item using a condition expression to avoid overwriting
try:
    response = table.put_item(
        Item={
            'student_id': 3,
            'name': 'Roscoe Village',
            'age': 23,
            'major': 'Psychology'
        },
        ConditionExpression='attribute_not_exists(student_id)'
    )
except dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
    print("Item already exists.")

# TO DO: List and print all items in the created table
response = table.scan()

for item in response['Items']:
    print(item)