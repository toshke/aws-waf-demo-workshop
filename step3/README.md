## Deploy WAF to your AWS Account

### Intro 

In this step you will be deploying [AWS Web Application Firewall, or just WAF]
to protect previously deployed and loadtested serverless API. 

WAF Resources, like most of other AWS resources can be described using
infrastructure code cloudformation template. This step's folder (step3)
contains `template.yaml` file, which includes all of the WAF resource definitions. 

Types of resources created are:

**ByteMatchSet** is describing criteria for selecting particular http(s) request. In essence, MatchSets describe which incoming requests should be picked up for further processing. [Read more on WAF rules and conditions](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works.html)

**WebACLs** are describing which criteria to apply to incoming requests, in what order (priority), and what to do with matching reqeustes (block, allow, count)

**WebACL Association** assignes ACL to an inbound http(s) traffic resource, 
such as API Gateway, Application Load Balancer or CloudFront distribution


### Create WAF resources using cfn
We will be simulating 2 scenarios - counting particular requests AND 
blocking malicous requests. 

There will be 2 rules deployed:
- One for counting any request with `x-from: awsworkshop` header
- One for blocking any request with `x-from: blackhathacker` header


```
$ cd step3
$ aws cloudformation deploy --template-file template.yaml --stack-name CloudToolsMeetup-DEC19-WAF

```

Go to [WAF Console to check for created WebACL and rules](https://console.aws.amazon.com/wafv2/home?region=us-east-2#/webacls)

Please note that if you're not following the link above and you go to WAF console directly you're landing on 'New AWS WAF', switch to 'AWS WAF Classic' to find your new created WAF resources by clicking "Switch to AWS WAF Clasic" link at left-pane menu.


#### Created Web ACL 
<img width="1094" alt="Screenshot 2019-11-24 22 21 23" src="https://user-images.githubusercontent.com/1170273/69493896-dd966f00-0f08-11ea-84f8-6501af4f23a4.png">

#### Created Rules and association between WebACL and API Gateway

<img width="1056" alt="Screenshot 2019-11-24 22 21 41" src="https://user-images.githubusercontent.com/1170273/69493897-df603280-0f08-11ea-9f36-86446f0ce78e.png">



[>> Go to step 4 >> ](../step4/README.md)
