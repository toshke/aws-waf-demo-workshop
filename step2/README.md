## Load test your API

### Install GoAd

This tutorial assumes you are running Cloud9 w/Amazon Linux2, however
if you are running this tutorial from Mac or Windows, head to 
[GOAS website for download url](https://goad.io/#install)


```
$ pip install beeswithmachineguns
```

### Generate an KeyPair for BeesToUse

Generate a keypair using ssh-keygen utility. Use empty String (no passphrase)
when prompted for one, for the sake of the workshop simplicity. Bees use this
ssh key to spin up ec2 instances

```
$ ssh-keygen -f ~/.ssh/beeskey.pem
$ aws ec2 import-key-pair --key-name beeskey --public-key-material file://~/.ssh/beeskey.pem.pub --region us-east-1
```
### Create SG for bees

Security groups work on AWS a little bit like traditional firewall - they
block any unwanted traffic. When new security group is created, it will by
default block all traffic, and required ports are whitelisted thereafter.
As bees work by issuing commands via SSH on port 22,  they will need security
group with port 22 open to the web. Use command below to create one

```
$ VPC_ID=$(aws ec2 describe-vpcs --query Vpcs[].VpcId --output text --region us-east-1)
$ aws ec2 create-security-group --region us-east-1 --vpc-id $VPC_ID --group-name beesgroup --description 'SG For Bees w/MachineGuns'
```

You should see output such as
```
{
    "GroupId": "sg-02b380c13a3765279"
}
```

Allow for inbound connections on ssh port

```
aws ec2 authorize-security-group-ingress --region us-east-1 --group-name beesgroup --port 22  --protocol tcp --cidr 0.0.0.0/0
```

GroupId is not relevant, as security group is given to bees via name

### Spin up 4 bees

As beeswithmachinegunes is relatively old tool (there has been no update in 2 years),
it uses old boto to spin up bees, with default region being us-east-1 (hence, in
previous step, you created key pair in that region)


```
$ bees up -s 4 -k beeskey
```

You should see output similar to following

```
New bees will use the "default" EC2 security group. Please note that port 22 (SSH) is not normally open on this group. You will need to use to the EC2 tools to open it before you will be able to attack.
Connecting to the hive.
Attempting to call up 4 bees.
Waiting for bees to load their machine guns...
.
.
.
Bee i-0ed35b6ea3631cc28 is ready for the attack.
.
Bee i-01305be4e7722e501 is ready for the attack.
.
Bee i-0781d57768c7e07f6 is ready for the attack.
.
Bee i-0643feff021a471cc is ready for the attack.
The swarm has assembled 4 bees.
```
