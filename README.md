# Aws WAF Workshop

This workshop provides hands on experience with
- Deploying Serverless API Endpoint using api gateway
- Load testing HTTPS API Endpoint using goad utility and coker
- Deploying WebApplicationFirewall (WAF) to protect the serverless api endpoint
- Demonstrate the WAF request blocking functionality based 
on header

## Prereqs

You can find [instrunctions here on how to setup Cloud9](cloud9.md)

This workshop makes assumptions on students running it using [Cloud9](https://aws.amazon.com/cloud9/) in `us-east-2` region. You may be able to run from Mac
or Windows as well, and in other regions, though workshop steps are not optimised for such environment. 

Also, all of the step instructions are relying
on the fact that you are positioned within that steps
folder.

Cloud9 instance should have IAM Role with following permissions attached to it
 - Manage CloudForamtion resources
 - Manage AWS Lambda functions
 - Manage API Gateway
 - Manage CloudWatch resources
 - Manage WAF Regional resources

For the simplicity of the workshop conduction, it is 
recommended to have admin priveleges credentials


### Workshop content

## Step 1 

[Deploy Simple WebAPI with ApiGateway and Lambdas](step1/README.md)

## Step 2

[Install goad. Load test the API. Look at the traffic data.](step2/README.md)

## Step 3

[Deploy the WAF that will detect Load testing header and block traffic.](step3/README.md)

## Step 4

[Run the load testing tool with and without the header. Look at metrics for Web Application Firewall](step4/README.md) 


## Cleanup

[Remove All of the created resources](cleanup.md)


Thanks for taking your time to go through this workshop. 