## Step 2 - Load test your API

In this step you will be installing goad, Go-written, AWS Lambda-powered 
website load testing tool. Once the tool is installed, you will use it
to put some load onto the serverless API endpoint created in previous step. 
As end result, you'll look at some CloudWatch metrics showing the results of load
tesing. 


### Install goad

This tutorial assumes you are running Cloud9 w/Amazon Linux2, however
if you are running this tutorial from Mac or Windows, head to 
[GOAS website for download url](https://goad.io/#install)

Installing goad on Linux (Cloud9) - copy & Paste commands below into
your Cloud 9 instance

```
$ wget https://github.com/goadapp/goad/releases/download/2.0.4/goad-linux-x86-64.zip && \
      unzip goad-linux-x86-64.zip && \
      sudo mv goad /usr/bin/goad && \
      goad -h
```

You should see output like below, verifying that downloaded binary is compatible
with your OS/Cpu:

```
usage: goad [<flags>] [<url>]

An AWS Lambda powered load testing tool

Flags:
  -h, --help                     Display usage information (this message)
  -n, --requests=1000            Number of requests to perform. Set to 0 in combination with a specified timelimit allows
                                 for unlimited requests for the specified time.
  -c, --concurrency=10           Number of multiple requests to make at a time
  -t, --timelimit=3600           Seconds to max. to spend on benchmarking
  -s, --timeout=15               Seconds to max. wait for each response
  -H, --header=HEADER ...        Add Arbitrary header line, eg. 'Accept-Encoding: gzip' (repeatable)
  -m, --method="GET"             HTTP method
      --body=BODY                HTTP request body
      --json-output=JSON-OUTPUT  Optional path to file for JSON result storage
      --region=us-east-1... ...  AWS regions to run in. Repeat flag to run in more then one region. (repeatable)
      --run-docker               execute in docker container instead of aws lambda
      --create-ini-template      create sample configuration file "goad.ini" in current working directory
  -V, --version                  Show application version.

Args:
  [<url>]  [http[s]://]hostname[:port]/path optional if defined in goad.ini
```


### Load testing API

For simplicity reasons we will be running Goad locally through docker, 
so we avoid potential issues with IAM etc. 


```
# Grab the endpoint url
ENDPOINT_URL=$(aws cloudformation describe-stacks \
        --stack-name CloudToolsMeetup-DEC19-API \
        --query 'Stacks[0].Outputs[0].OutputValue' --out text)
        
# Run the load testing tool 
goad -m GET --requests  500 \
     --concurrency=10 \
     --timeout=2 \
     --timelimit=60 \
     -H 'x-from: awsworkshop' $ENDPOINT_URL 
     --run-docker
```

Once the load testing tool has completed execution, you should see text like below
at the end of the output

```
Overall

   TotReqs   TotBytes    AvgTime    AvgReq/s  (post)unzip
       500      25 kB     0.066s      134.66     6.8 kB/s
   Slowest    Fastest   Timeouts  TotErrors
    0.425s     0.046s          0          0
HTTPStatus   Requests
       200        500
```
    
### Verifying number of API requests. 

To verify that API was actually hit, go to [CloudWatch metrics home page first](https://us-east-2.console.aws.amazon.com/cloudwatch/home?region=us-east-2#metricsV2:graph=~(view~'timeSeries~stacked~false~region~'us-east-2~stat~'Sum~period~300)

As we want to see API Gateway metrics, select (AllMetrics/ApiGateway/ByApiName).
Like on screenshot below, you should see "CloudToolsMeetup-DEC19-WAF" 
Select "Count" for MetricName as we are interested only in total number of requests (screenshot1 below),
then head of to "Graphed Metrics Tab". Selecting "SUM" for statistics like on 
screenshot2 should display total number of requests, which in this case
should be 500. (screenshot3)

#### Select Count for Metric Name for Workshop API Gateway
<img width="1157" alt="Screenshot 2019-11-17 19 38 51" src="https://user-images.githubusercontent.com/1170273/69005193-93464880-0972-11ea-8219-eaf3c11c68d5.png">


#### Select SUM as statistic name so TOTAL number of requests are visible
<img width="1119" alt="Screenshot 2019-11-17 19 39 01" src="https://user-images.githubusercontent.com/1170273/69005192-917c8500-0972-11ea-98c4-583704eb6cfd.png">

#### You should see 500 API Requests
<img width="246" alt="Screenshot 2019-11-17 19 39 10" src="https://user-images.githubusercontent.com/1170273/69005190-904b5800-0972-11ea-9723-45a63479e3b7.png">


#### Extras (try this at home)

1. Try and see how many invocations of Lambda function
`CloudToolsMeetup-DEC19-WAF-LambdaFunction-xxxx` is there in CloudWatch metrics. 

2. Try running goad from Lambda functions, rather then from Container (Tip: You may need to compile goad from source
for this one to work)



[>> Go to step 3 >> ](../step3/README.md)