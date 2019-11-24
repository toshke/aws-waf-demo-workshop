## Step 4 - WAF In action

In this step we will send some https request to 
previously created AWS WAF-protected API point. 
We'll also look at the metrics that platform can 
provide in relation to web request fitlering. 

WAF Rules that have been created in previous steps
use  `x-from` header  as control. `awsworkshop` 
headers are allowed and counted, whereas 
`blackhathacker` ones are blocked. We will be sending
200 requests that should be allowed, 
and 100 ones that should be blocked


### Send some 'regular' requests

In this step you will sen some regular requests to
previously created API gateway. 'Regular' in this context
means these requests will be allowed and countedd by AWS WAF.

To do so, copy and paste commands below into
your Cloud9 terminal window. 

```
ENDPOINT_URL=$(aws cloudformation describe-stacks --stack-name CloudToolsMeetup-DEC19-API --query 'Stacks[0].Outputs[0].OutputValue' --out text)

goad -m GET  \
    --requests  200 \
    --concurrency=10  \
    --timeout=2 \
    --timelimit=60 \
    -H 'x-from: awsworkshop' \
    $ENDPOINT_URL \
    --run-docker
```


### Send some malicious requests (and see them blocked)

For these reqeusts, we are expecting 403 http status code returned. Again, we will retrieve endpoint url from 
as CloudFormation stack output and use `goad` to 
send some test requests

```

ENDPOINT_URL=$(aws cloudformation describe-stacks --stack-name CloudToolsMeetup-DEC19-API --query 'Stacks[0].Outputs[0].OutputValue' --out text)

goad -m GET  \
    --requests  100 \
    --concurrency=10  \
    --timeout=2 \
    --timelimit=60 \
    -H 'x-from: blackhathacker' \
    $ENDPOINT_URL \
    --run-docker
```

To see actual return status code you can use curl
command, as it's output can be more verbose
compared to goad one

```
$ curl -v -H 'x-from: blackhathacker' $ENDPOINT_URL
```

Output of this command should show 403 status code, like shown below

```
ec2-user:~/environment $ curl -v -H 'x-from: blackhathacker' $ENDPOINT_URL 
*   Trying 99.86.58.103...
* TCP_NODELAY set
* Connected to bvjsehtazj.execute-api.us-east-2.amazonaws.com (99.86.58.103) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1

<< BORING TLS OUTPUT WAS REMOVED >

* Using Stream ID: 1 (easy handle 0x1193d10)
> GET /Prod/helloworld HTTP/2
> Host: bvjsehtazj.execute-api.us-east-2.amazonaws.com
> User-Agent: curl/7.61.1
> Accept: */*
> x-from: blackhathacker
> 
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
< HTTP/2 403 
< content-type: application/json
< content-length: 23
< date: Sun, 24 Nov 2019 09:46:06 GMT
< x-amzn-requestid: e6ccf68b-e1d2-4930-861f-b30f63d9f001
< x-amzn-errortype: ForbiddenException
< x-amz-apigw-id: DqGmxFjQiYcFZyg=
< x-cache: Error from cloudfront
< via: 1.1 703b08cef218787c0412d1e05c5a7766.cloudfront.net (CloudFront)
< x-amz-cf-pop: YTO50-C1
< x-amz-cf-id: 3p7qiAxIy0FU3kTGStU7CsJUMJlISSx9tVA4OKWIPT-CLnCM9VGwYw==
< 
* Connection #0 to host bvjsehtazj.execute-api.us-east-2.amazonaws.com left intact
{"message":"Forbidden"}
```

## Look at the metrics

You can visit [CloudWatch Metrics Dashboard](https://us-east-2.console.aws.amazon.com/cloudwatch/home?region=us-east-2#metricsV2:graph=~();query=~'*7bWAF*2cRegion*2cRule*2cWebACL*7d) to look 
at the WAF data points. 

Select `WAF` namespace, `Region,Rule,WebACL` metric in the 
metrics section.

Once presented with all different metrics, we are interested
in number of Blocked `BlackHatRequests` rule requests, as well as number of counted `MeetupRequest` rule requests. You can 
select sum of all data points within 5 minute period, 
like on the screenshot below. Explore different graph modes
between Number, Graph and Line. Making additional requests
within >5 minutes from initial ones will render 'Stacked area' 
graph mode more useful

##### CloudWatch metrics for deployed WAF
<img width="1087" alt="Screenshot 2019-11-24 20 48 57" src="https://user-images.githubusercontent.com/1170273/69492963-fef15e00-0efc-11ea-907d-583bf67fa89f.png">


##### CloudWatch metrics - stacked area graph
<img width="1083" alt="Screenshot 2019-11-24 20 58 28" src="https://user-images.githubusercontent.com/1170273/69493199-0d8d4480-0f00-11ea-83f4-bd5572aa2f9c.png">


### What's next

Congratulations! You made it to end of this workshop. 
You can explore different options, metrics etc on 
[Official AWS Documentation pages](https://docs.aws.amazon.com/waf/latest/APIReference/Welcome.html)

Do not forget to 
[>> Clean up AWS resources >> ](../cleanup.md)



