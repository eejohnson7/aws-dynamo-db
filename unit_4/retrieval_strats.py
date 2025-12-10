'''
Great job so far! In this task, you will continue to build upon your foundational knowledge of DynamoDB by writing Python 
scripts that not only demonstrate your ability to interact with DynamoDB tables but also to manipulate and retrieve data 
efficiently. You will begin with a template that already includes scripts for creating a DynamoDB table named Movies and 
populating it with several records. Your focus will be on expanding this script to include data retrieval operations using 
GetItem and BatchGetItem. Specifically, you will demonstrate different retrieval strategies including simple reads, reads 
with projection, and ensuring strongly consistent reads.
'''

import boto3

# Create DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table_name = 'Movies'
table_names = [table.name for table in dynamodb.tables.all()]

if table_name in table_names:
    table = dynamodb.Table(table_name)
else:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            { 'AttributeName': 'year', 'KeyType': 'HASH' }, # Partition key
            { 'AttributeName': 'title', 'KeyType': 'RANGE' } # Sort key
        ],
        AttributeDefinitions=[
            { 'AttributeName': 'year', 'AttributeType': 'N' },
            { 'AttributeName': 'title', 'AttributeType': 'S' },
        ],
        ProvisionedThroughput={ 'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5 }
    )

# Wait for table to be created with custom waiter
table.meta.client.get_waiter('table_exists').wait(
    TableName='Movies', 
    WaiterConfig={
        'Delay': 2,           # Poll every 2 seconds
        'MaxAttempts': 10     # Make maximum 10 attempts
    }
)

# Insert movies into the table
table.put_item(Item={'year': 2016, 'title': 'The Big New Movie'})
table.put_item(Item={'year': 2017, 'title': 'The Bigger, Newer Movie'})
table.put_item(Item={'year': 2017, 'title': 'Yet Another Movie'})
table.put_item(Item={'year': 2017, 'title': 'One More Movie'})
table.put_item(Item={'year': 2015, 'title': 'An Old Movie'})
table.put_item(Item={'year': 2018, 'title': 'Another New Movie'})

# TODO: Retrieve 'The Big New Movie' from 2016 using a simple GetItem.
result = table.get_item(Key={'year': 2016, 'title': 'The Big New Movie'})
if 'Item' in result:
    print("Movie found:", result['Item'])
else:
    print("Movie not found.")
    
# TODO: Retrieve 'The Big New Movie' from 2016 using GetItem with ProjectionExpression for 'title' and 'genre'.
result = table.get_item(Key={'year': 2016, 'title': 'The Big New Movie'}, ProjectionExpression='title, genre')
if 'Item' in result:
    print("Projected attributes of the movie:", result['Item'])
else:
    print("Movie not found.")
    
# TODO: Retrieve 'The Big New Movie' from 2016 using a strongly consistent read.
result = table.get_item(Key={'year': 2016, 'title': 'The Big New Movie'}, ConsistentRead=True)
if 'Item' in result:
    print("Movie found:", result['Item'])
else:
    print("Movie not found.")

# TODO: Use BatchGetItem to retrieve 'The Big New Movie' from 2016 and 'The Bigger, Newer Movie' from 2017 with consistent read.
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
print("Movies found:", result["Responses"])