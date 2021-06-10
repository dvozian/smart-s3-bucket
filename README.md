# smart-s3-bucket
## S3 bucket with notification using SNS and Lambda
### Description
A smart S3 bucket at AWS with new uploads notification to email and sms using AWS SNS and an AWS lambda. This service is useful for services that offer file storage with upload event notifications with minimum cost. An example could be a video file sharing service where users would like to get notifications when a new movie is uploaded.

### Prerequisites: 
- Access to AWS console
- Basic knowledge of AWS services, including S3, SNS, and Lambda 

### Setup
- Create one S3 bucket
- Create one SNS topic
- Create one Lambda
- Edit event notifications for S3 bucket and push to Lambda on PUT and POST event
- Add code to Lambda to parse the notification message that will come to S3 bucket event
- Make Lambda push the message to the SNS topic
- Configure the SNS topic to notificatins to your prefered way: email or sms.

### How to run
- Upload any file to the S3 bucket
- Expect the notification to arive to your email or phone within seconds.

### The costs
- Amazon S3 
  - 5GB - 12 months – Free
  - First 50 TB / Month – $ 0.023
  - Next 450 TB / Month – $ 0.022
- Amazon Simple Notification Service (Amazon SNS) 
  - Data transfer IN and  Data transfer OUT – $ 0.00 per month
  - Next 9.999 TB / Month - $ 0.09 per GB
- Amazon Lambda
  - Up to 1 GB / Month,  free request per 1 month and 400.000 GB-seconds
  - Requests - $0.20 per 1 M requests

