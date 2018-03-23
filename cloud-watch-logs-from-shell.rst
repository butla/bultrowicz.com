
Quickly scanning CloudWatch logs from the shell
===============================================

.. post::
   :author: Michal Bultrowicz
   :tags: Python

I think I have a useful tool and workflow for browsing cloud watch logs.
The tool's called awslogs.
Can be installed with `pip3 install --user awslogs`
Yeah, it's a Python tool. Just remember to have ~/.local/bin on your PATH.

Also, I've added aliases like these
```alias awslogsprodtracker='awslogs get /aws/lambda/prod_tracker_events_kinesis_worker'
alias awslogsprodapi='awslogs get iteriodata-prod-iteriodata-api/iteriodata-api'
alias awslogsdevtracker='awslogs get /aws/lambda/dev_tracker_events_kinesis_worker'
alias awslogsdevapi='awslogs get iteriodata-dev-iteriodata-api/iteriodata-api'```

So now, to get all calls to /v1/intercom_hooks I just put this in the shell: `awslogsprodapi -f intercom_hook -s 10m`
The `-f` parameter takes values conforming to the CloudWatch filter syntax https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html
