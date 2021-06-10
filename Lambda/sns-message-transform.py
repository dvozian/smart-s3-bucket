from __future__ import print_function

import json
import urllib
import boto3

print('Loading message function...')


def send_to_sns(message, context):

    sns = boto3.client('sns')
    sns.publish(
        TopicArn='arn:aws:sns:us-west-2:075763689953:NotificationsFromS3',
        Subject='Hello form lambda',
        Message='Activity in the S3 bucket: ' + message['Records'][0]['s3']['bucket']['name'] + '.\nThis event happened at: ' + message['Records'][0]['eventTime'] + '.\nThe action type is: ' + message['Records'][0]['eventName'] + '.\nThe IP address from which the event was performed: ' + message['Records'][0]['requestParameters']['sourceIPAddress'] + '. \nFile name: ' + message['Records'][0]['s3']['object']['key']
    )

    return ('Sent a message to an Amazon SNS topic.')