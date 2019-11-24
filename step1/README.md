## Step 1 - Deploy serverless API

In this step, you will deploy serverless API, utilising AWS resourcesLambda
Functions and API Gateway. To do so, you will use [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html) to package,
and deploy SAM CloudFormation template.

**Important** Set your region to `us-east-2`, or region where your Cloud9
runs. You can do so by exporting `AWS_DEFAULT_REGION` variable, e.g.

```
export AWS_DEFAULT_REGION=us-east-2
```

### Create S3 bucket for template and code

For the demo, I've used *melbournecloudtoolsmeetups.$timestamp* for bucket
name, but you can really use any bucket.

```

export BUCKET_NAME=melbournecloudtoolsmeetup.`date +%s`
aws s3 mb s3://${BUCKET_NAME}
```

Remember your S3 bucket

### Package CloudFormation

As an AWS SAM exercise, package the template first - this will
replace all local references to application code to hardcoded ones, pointing
to code that has been uploaded to S3 bucket created in previous step.
For this you will use `sam package` command

```
$ cd step1
$ sam package --template-file=template.yaml --s3-bucket=$BUCKET_NAME --output-template=template.processed.yaml
```

You should see output like following
```
Successfully packaged artifacts and wrote output template to file template.processed.yaml.
Execute the following command to deploy the packaged template
aws cloudformation deploy --template-file /Users/nikolatosic/Development/projects/github/aws-waf-demo-workshop/step1/template.processed.yaml --stack-name <YOUR STACK NAME>
```

### Deploy Serverless API

In this step you deploy serverless API

```
aws cloudformation deploy --template-file template.processed.yaml --stack-name CloudToolsMeetup-DEC19-API --capabilities CAPABILITY_IAM
```


### Get your API Endpoint

In order to feed bees with machineguns an endpoint url in next step,
you will need to read the endpoint form stack outputs first. Use command
below to read your API Endpoint

```
ENDPOINT_URL=$(aws cloudformation describe-stacks --stack-name CloudToolsMeetup-DEC19-API --query 'Stacks[0].Outputs[0].OutputValue' --out text)
echo $ENDPOINT_URL
curl -s $ENDPOINT_URL | jq
```

You should see output as following, retrieving your basic API resource

```
https://9ecqet1mj2.execute-api.us-east-2.amazonaws.com/Prod/helloworld
$ curl -s $ENDPOINT_URL | jq
{
  "Message": "Hello, World!",
  "InMemoryCounter": 1
}

```


Congratulations, you have successfully deployed
serverless API in AWS and Completed step1 of this
workshop. 

[>> Go to step 2 >> ](../step2/README.md)