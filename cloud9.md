## Setting up Cloud9 for this workshop

**NOTE 1:** If running `aws sts get-caller-identity` in Cloud9 terminal window gives you response such as `arn:aws:iam::123456789012:root` as your identity - you are already running Cloud9 from your root account, so you can skip any instructions below. Additionally, you can [read on using IAM for least privileged access (see NOTE2 Below)](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html?)

**NOTE 2:** Allowing admin permissions 
should be highly discouraged in any enterpise
or other envionrment. For the sake of simplicity 
this workshop step instructs to allow admin permissions
to Cloud9, but if you would like to do so, you can
go down the path of least privlieged instance
and create IAM user with following permissions

- Manage CF stacks
- Manage WAF Regional resources
- Manage Api Gateways
- Manage Lamdba functions (CloudWatch Logs and S3 bucket)
- Create bucket and manage data in S3

### Create Cloud9 environment

Go to [Create New Environment](https://us-east-2.console.aws.amazon.com/cloud9/home/create) within
AWS Console and create new environment


##### Cloud9 new environment
<img width="1039" alt="Screenshot 2019-11-24 21 37 57" src="https://user-images.githubusercontent.com/1170273/69493654-4a0f6f00-0f05-11ea-902a-89822e6fd0cd.png">


## Create IAM Rrole 
[Go to IAM Console and Create new EC2 role](https://console.aws.amazon.com/iam/home?region=us-east-2#/roles$new?step=type
)

Select 'EC2' for service and attach 'Administrator access'
policy

Use 'Cloud9Admin' as role name

Select Administrator access
<img width="1014" alt="Screenshot 2019-11-24 21 40 16" src="https://user-images.githubusercontent.com/1170273/69493489-4ed32380-0f03-11ea-92a3-55e5de5a9469.png">

<img width="1123" alt="Screenshot 2019-11-24 21 41 27" src="https://user-images.githubusercontent.com/1170273/69493478-3400af00-0f03-11ea-9fad-5a6d79e6aae2.png">


## Attach role to Cloud9 instance

Go to [EC2 Console](https://us-east-2.console.aws.amazon.com/ec2/home?region=us-east-2#Instances:sort=instanceId), right click
Cloud9 instance, select Instance Settings -> Attach / Replace IAM Role, then select *Cloud9Admin* as role name


##### Change Cloud9 instance role
<img width="1038" alt="Screenshot 2019-11-24 21 44 59" src="https://user-images.githubusercontent.com/1170273/69493587-8b534f00-0f04-11ea-8f4c-a3a24d722fc9.png">


<img width="1068" alt="Screenshot 2019-11-24 21 45 49" src="https://user-images.githubusercontent.com/1170273/69493596-9efeb580-0f04-11ea-8fd6-16a6656171c7.png">

[>> Workshop home page >> ](../README.md)
