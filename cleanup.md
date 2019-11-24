### Cleanup

1.  Remove deployed CloudFormation stacks.
You can do so by  visiting [CloudFormation console](https://us-east-2.console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks?filteringText=&filteringStatus=active&viewNested=true&hideStacks=false)

Alternatively, delete using aws cli commands from your Cloud9 workspace

```
aws cloudformation delete-stack --stack-name CloudToolsMeetup-DEC19-WAF

aws cloudformation delete-stack --stack-name CloudToolsMeetup-DEC19-API
```

2. Cleanup Cloud9 workspace. Depending on your configuration settings, Cloud9 may shut down on it's
own after period of inactivity