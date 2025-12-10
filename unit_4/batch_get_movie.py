'''
Good job! This task will test your understanding of DynamoDB data retrieval operations. You have a script that builds a 
table named Movies and populates it with a few records. Each record represents a movie, containing attributes such as year 
and title. Your objective is to extend the functionality of this script by adding data retrieval operations to fetch movies 
from the table. Specifically, you must add the batch_get_item operation to retrieve two movies simultaneously: 
'The Big New Movie' from 2016 and 'The Bigger, Newer Movie' from 2017.
'''

import boto3

# Create DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Table creation
table_name = 'Movies'
table_names = [table.name for table in dynamodb.tables.all()]

if table_name in table_names:
    table = dynamodb.Table(table_name)
else:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            { 'AttributeName': 'year', 'KeyType': 'HASH' }, # Partition key 
            { 'AttributeName': 'title', 'KeyType': 'RANGE' }  # Sort key
        ],
        AttributeDefinitions=[
            { 'AttributeName': 'year', 'AttributeType': 'N' },
            { 'AttributeName': 'title', 'AttributeType': 'S' },
        ],
        ProvisionedThroughput={ 'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5 }
    )

# Wait for table to be created, polling every 2 seconds and making 10 attempts maximum
table.meta.client.get_waiter('table_exists').wait(TableName='Movies', WaiterConfig={'Delay': 2, 'MaxAttempts': 10})

# Insert movies into the table
table.put_item(Item={'year': 2016, 'title': 'The Big New Movie'})
table.put_item(Item={'year': 2017, 'title': 'The Bigger, Newer Movie'})
table.put_item(Item={'year': 2017, 'title': 'Yet Another Movie'})
table.put_item(Item={'year': 2017, 'title': 'One More Movie'})
table.put_item(Item={'year': 2015, 'title': 'An Old Movie'})
table.put_item(Item={'year': 2018, 'title': 'Another New Movie'})

# TODO: Add BatchGetItem operation to fetch 'The Big New Movie' and 'The Bigger, Newer Movie'
result = dynamodb.batch_get_item(
    RequestItems={
        'Movies': {
            'Keys': [
                {'year': 2016, 'title': 'The Big New Movie'},
                {'year': 2017, 'title': 'The Bigger, Newer Movie'}
            ],
            'ConsistentRead': True
        }
    }
)

# Print retrieved items
print(result['Responses'])