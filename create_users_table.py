#!/usr/bin/env python3
import boto3

def create_table(
        ddb_table_name,
        ):

    dynamodb = boto3.resource('dynamodb')

    # The variables below transform the arguments into the parameters expected by dynamodb.create_table.

    table_name = ddb_table_name
    
    # Query rider assigned to order
    attribute_definitions = [
        {'AttributeName': 'pk', 'AttributeType': 'S'},
        {'AttributeName': 'sk', 'AttributeType': 'S'},
        {'AttributeName': 'tags', 'AttributeType': 'S'},
        {'AttributeName': 'brand_id', 'AttributeType': 'S'}
        ]
    
    key_schema = [{'AttributeName': partition_key, 'KeyType': 'HASH'}, 
                  {'AttributeName': sort_key, 'KeyType': 'RANGE'}]
                  
    provisioned_throughput = {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 10}
    
    # Grouped by order_id; Query payment method
    global_secondary_indexes = [{
            'IndexName': 'inverted-index',
            'KeySchema': [
                {'AttributeName': 'sk', 'KeyType': 'HASH'},
                {'AttributeName': 'pk', 'KeyType': 'RANGE'}],
            'Projection': {'ProjectionType': 'INCLUDE',
                           'NonKeyAttributes':["payment_method", "rider_id"]},
            'ProvisionedThroughput': {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 10}
    },{
            'IndexName': 'food-tag-index',
            'KeySchema': [
                {'AttributeName': 'brand_id', 'KeyType': 'HASH'},
                {'AttributeName': 'tags', 'KeyType': 'RANGE'}],
            'Projection': {'ProjectionType': 'INCLUDE',
                           'NonKeyAttributes':["name"]},
            'ProvisionedThroughput': {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 10}
    },{
            
    }]
    
    try:
        # Create a DynamoDB table with the parameters provided
        table = dynamodb.create_table(TableName=table_name,
                                      KeySchema=key_schema,
                                      AttributeDefinitions=attribute_definitions,
                                      ProvisionedThroughput=provisioned_throughput,
                                      GlobalSecondaryIndexes=global_secondary_indexes
                                      )
        return table
    except Exception as err:
        print("{0} Table could not be created".format(table_name))
        print("Error message {0}".format(err))
        
def delete_table(name):
    dynamodb = boto3.resource('dynamodb')  
    table = dynamodb.Table(name)
    table.delete()

if __name__ == '__main__':
    table = create_table("users-orders-items", "pk", "sk", 'order_status')