import boto3
import os
import json


def lambda_handler(message, context):

    if ('body' not in message or
            message['httpMethod'] != 'PUT'):
        return {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps({'msg': 'Bad Request'})
        }

    table_name = os.environ.get('TABLE', 'Activities')
    region = os.environ.get('REGION', 'us-east-1')
    aws_environment = os.environ.get('AWSENV', 'AWS')

    if aws_environment == 'AWS_SAM_LOCAL':
        activities_table = boto3.resource(
            'dynamodb',
            endpoint_url='http://dynamodb:8000'
        )
    else:
        activities_table = boto3.resource(
            'dynamodb',
            region_name=region
        )

    table = activities_table.Table(table_name)
    activity = json.loads(message['body'])

    params = {
        'id': activity['id'],
        'date': activity['date']
    }

    response = table.update_item(
        Key=params,
        UpdateExpression="set stage = :s, description = :d",
        ExpressionAttributeValues={
            ':s': activity['stage'],
            ':d': activity['description']
        },
        ReturnValues="UPDATED_NEW"
    )
    print(response)

    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps({'msg': 'Activity updated'})
    }
