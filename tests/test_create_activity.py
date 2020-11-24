import boto3
import json
import os
from moto import mock_dynamodb2
from unittest.mock import patch
from src.create_activity import app
from contextlib import contextmanager

table_name = 'Activities'

event_data = 'events/create_activity_event.json'
with open(event_data, 'r') as f:
    event = json.load(f)


@contextmanager
def do_test_setup():
    with mock_dynamodb2():
        set_up_dynamodb()
        yield


def set_up_dynamodb():
    conn = boto3.client(
        'dynamodb',
        region_name='us-east-1',
        aws_access_key_id='mock',
        aws_secret_access_key='mock',
    )
    conn.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'},
            {'AttributeName': 'date', 'KeyType': 'RANGE'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'S'},
            {'AttributeName': 'date', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        },
    )


@patch.dict(os.environ, {
    'TABLE': 'Activities',
    'REGION': 'us-east-1',
    'AWSENV': 'MOCK'
})
def test_create_activity_201():
    with do_test_setup():
        response = app.lambda_handler(event, '')

        payload = {
            'statusCode': 201,
            'headers': {},
            'body': json.dumps({'msg': 'Activity created'})
        }

        conn = boto3.client(
            'dynamodb',
            region_name='us-east-1',
            aws_access_key_id='mock',
            aws_secret_access_key='mock',
        )

        item = conn.scan(TableName=table_name)

        assert item != ''
        assert event['httpMethod'] == 'POST'
        assert response == payload


@patch.dict(os.environ, {
    'TABLE': 'Activities',
    'REGION': 'us-east-1',
    'AWSENV': 'MOCK'
})
def test_create_activity_400():
    with do_test_setup():
        response = app.lambda_handler({}, '')

        payload = {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps({'msg': 'Bad Request'})
        }

        assert response == payload
