# AWS Lambda

- Lambda name: sns-message-transform

- Description: the purpose of the lambda is to receive the event message from S3 bucket, transform it by retrieving useful information from the big message, and push it to the SNS topic.

### Sample Message (INPUT)
```
{
  "Records": [
    {
      "eventVersion": "2.1",
      "eventSource": "aws:s3",
      "awsRegion": "us-west-2",
      "eventTime": "2021-06-03T06:47:49.016Z",
      "eventName": "ObjectCreated:Put",
      "userIdentity": {
        "principalId": "AWS:AIDARDI66FHQQHCOJR6QG"
      },
      "requestParameters": {
        "sourceIPAddress": "73.118.190.118"
      },
      "responseElements": {
        "x-amz-request-id": "XPY2X5QG3DR9WQ1J",
        "x-amz-id-2": "HxQntZG+1O87tVbVQVce9eW0Kcy6NKxblqz7vTfXKNQOq6ohS+sRZoxZIGdg+8fmXNMiHrGQ3HGFF9/VtCKeywFmwEbzeC1L"
      },
      "s3": {
        "s3SchemaVersion": "1.0",
        "configurationId": "NotificationsFromS3",
        "bucket": {
          "name": "bucket-with-notifications",
          "ownerIdentity": {
            "principalId": "A1SJAKF2JVK77K"
          },
          "arn": "arn:aws:s3:::bucket-with-notifications"
        },
        "object": {
          "key": "Budget1.xlsx",
          "size": 20638,
          "eTag": "7f7d997790a51eb7879281c3ef1a0242",
          "sequencer": "0060B87B173D2BC011"
        }
      }
    }
  ]
}
```

### Sample Message (OUTPUT)

```
Activity in the S3 bucket bucket-with-notifications.
This happened at 2021-06-03T06:47:49.016Z.
The action type is: ObjectCreated:Put.
The IP address from which the event was performed: 73.118.190.118
```

