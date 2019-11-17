# Aws WAF Workshop

This workshop provides hands on experience with
- Deploying Serverless API Endpoint using api gateway
- Load testing HTTPS API Endpoint in Docker
- Deploying WebApplicationFirewall (WAF) to protect the endpoint
- Demonstrating the WAF blocking functionality

## Prereqs

This workshop makes assumptions on students running it through [Cloud9](https://aws.amazon.com/cloud9/) in `us-east-2` region. You may be able to run from Mac
or Windows as well, and in other regions, though workshop steps are not optimised for such environment. 

Cloud9 instance should have IAM Role with following permissions attached to it
 - Manage lambda functions
 - Manage IAM Roles

### Workshop content

## Step 1

Deploy Simple WebAPI with ApiGateway and Lambdas

## Step 2

Install [goad](https://github.com/goadapp/goad/). Load test the API. Look at the traffic data. 

## Step 3

Deploy the WAF that will detect Load testing header and block traffic. 

## Step 4

Run the load testing tool with and without the header. Look at 
the traffic data. 
