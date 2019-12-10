## Additional tasks

These tasks are left open ended, without perspective way of
implementing the solution. Feel free to play around, through
the AWS console or provisioning tools such as CloudFormation,
Terraform, AWS CDK etc. Purpose of the tasks is to give ideas for self paced and exploratory practice of using AWS WAF service.

### Payload size.

**Situation:** You are working as an engineer on a popular
website for posting travel photography that's using AWS Api Gateway.
You are asked to report on number of uploads smaller then 2MB, number of uploads
sized between 2 and 10MB, and number of uploads greater than 10MB.

Implement solution using AWS WAF.

*Tip:* Look at [Size Constraint Statement](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-size-constraint-match.html)

### Browser detection

**Situation:**  Your corporate policy mandates that intranet pages can be only
accessed from Internet Explorer / Edge browser. Solution is not expected to
detected spoofed User-Agent headers. Intranet portal runs on EC2 instances fronted
with ALB.

Implement solution using AWS WAF.

*Tip* To test your solution use [User Agent Switcher Plugin For Chrome](https://chrome.google.com/webstore/detail/user-agent-switcher-for-c/djflhoibgkdhkhhcedjiklpkjnoahfmg) 

### GeoIP detection

*Situation* You are working as cloud engineer in charge of infrastructure for
investigative journalism website. After controversial article on international
arms deal, your website is under layer 7 DDoS attack. After analysing ALB logs you
conclude that most of the IPs are coming from particular geogrpahic region.

How do you protect your infrastructure using aws WAF?
