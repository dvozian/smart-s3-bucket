# AWS SNS Topic

- Topic Name: NotificationsFromS3
- Description: This SNS topic is receiving messages from the lambda and pushing it to email and/or sms.
- Subscriptions: 
    - dvozian@student.rtc.edu
    - iturcan@student.rtc.edu
    
Sample message:
```
Activity in the S3 bucket: smart-s3-bucket.
This event happened at: 2021-06-05T02:33:02.974Z.
The action type is: ObjectCreated:Put.
The IP address from which the event was performed: 73.118.190.118.
File name: Picture1.png
```