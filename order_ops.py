#!/usr/bin/env python3
import boto3
from boto3.dynamodb.conditions import Key
import hashlib
import random
from decimal import Decimal

def add_item(order_id, product_name, quantity, price, status): 
    # Generate item ID. In real life, there are better
    # ways of doing this
    item_id = hashlib.sha256(product_name.encode()).hexdigest()[:8]
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('grabfoodb')
    
    item = {
        'pk'           : f'#ITEM#{item_id}', 
        'sk'           : order_id,
        'product_name' : product_name,
        'quantity'     : quantity,
        'price'        : price,
        'item_status'  : status,
    }
    table.put_item(Item=item)
    print("Added {0} to order {1}".format(product_name, order_id))
    
def checkout(username, address, items, date, status): 
    # Generate order ID. In real life, there are better
    # ways of doing this
    order_id = hashlib.sha256(str(random.random()).encode()).hexdigest()[:random.randrange(1, 20)]
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users-orders-items')
    
    item = {
        'pk'      : '#USER#{0}'.format(username), 
        'sk'      : '#{0}#CHECKOUT{1}#ORDER{2}'.format(status, date, order_id),
        'address' : address,
        'checkout_date' : date,
        'order_status'  : status
    }
    table.put_item(Item=item)
    
    for item in items[:-1]:
        add_item('#{0}#CHECKOUT{1}#ORDER{2}'.format(status, date, order_id), 
                 item['product_name'], 
                 item['quantity'], 
                 item['price'],
                 item['status']
                 )

def query_user_orders(username):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('users-orders-items')
    response = table.query(KeyConditionExpression=Key('pk').eq('#USER#{0}'.format(username)) & 
                                                Key('sk').begins_with('#ORDER#')
    )
    return response['Items']
    
def query_order_items(order_id):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('users-orders-items')
    response = table.query(
    IndexName='inverted-index',
    KeyConditionExpression=Key('sk').eq('#ORDER#{0}'.format(order_id)) & 
                      Key('pk').begins_with('#ITEM#')
    )
    return response['Items']
    
def query_user_order_by_status_date(username, status, date):
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('users-orders-items')
    response = table.query(
        KeyConditionExpression=Key('pk').eq('#USER#{0}'.format(username)) &
                              Key('sk').begins_with('#{0}#CHECKOUT{1}'.format(status, date))
    )
    return response['Items']
    
def query_menu_items(brand_id):
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('users-orders-items')
    response = table.query(
        KeyConditionExpression=Key('pk').eq('#USER#{0}'.format(username)) &
                              Key('sk').begins_with('#{0}#CHECKOUT{1}'.format(status, date))
    )
    return response['Items']