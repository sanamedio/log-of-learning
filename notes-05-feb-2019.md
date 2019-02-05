# 05-feb-2019


### 2 - cloudwatch amazon examples

```python
import boto3


# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')


def list_alarms():
    # List alarms of insufficient data through the pagination interface
    paginator = cloudwatch.get_paginator('describe_alarms')
    for response in paginator.paginate(StateValue='INSUFFICIENT_DATA'):
        print(response['MetricAlarms'])



def create_alarm():
    # Create alarm
    cloudwatch.put_metric_alarm(
        AlarmName='Web_Server_CPU_Utilization',
        ComparisonOperator='GreaterThanThreshold',
        EvaluationPeriods=1,
        MetricName='CPUUtilization',
        Namespace='AWS/EC2',
        Period=60,
        Statistic='Average',
        Threshold=70.0,
        ActionsEnabled=False,
        AlarmDescription='Alarm when server CPU exceeds 70%',
        Dimensions=[
            {
              'Name': 'InstanceId',
              'Value': 'INSTANCE_ID'
            },
        ],
        Unit='Seconds'
    )

def delete_alarm():
    # Delete alarm
    cloudwatch.delete_alarms(
      AlarmNames=['Web_Server_CPU_Utilization'],
    )


def alarm_action():
    cloudwatch.put_metric_alarm(
    AlarmName='Web_Server_CPU_Utilization',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=60,
    Statistic='Average',
    Threshold=70.0,
    ActionsEnabled=True,
    AlarmActions=[
      'arn:aws:swf:us-west-2:{CUSTOMER_ACCOUNT}:action/actions/AWS_EC2.InstanceId.Reboot/1.0'
    ],
    AlarmDescription='Alarm when server CPU exceeds 70%',
    Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': 'INSTANCE_ID'
        },
    ],
    Unit='Seconds'
    )


def disable_alarm():

    # Disable alarm
    cloudwatch.disable_alarm_actions(
      AlarmNames=['Web_Server_CPU_Utilization'],
    )



def list_metrics():
    # List metrics through the pagination interface
    paginator = cloudwatch.get_paginator('list_metrics')
    for response in paginator.paginate(Dimensions=[{'Name': 'LogGroupName'}],
                                   MetricName='IncomingLogEvents',
                                   Namespace='AWS/Logs'):
    print(response['Metrics'])



def publish_custom_metrics():
    # Put custom metrics
    cloudwatch.put_metric_data(
    MetricData=[
        {
            'MetricName': 'PAGES_VISITED',
            'Dimensions': [
                {
                    'Name': 'UNIQUE_PAGES',
                    'Value': 'URLS'
                },
            ],
            'Unit': 'None',
            'Value': 1.0
        },
    ],
    Namespace='SITE/TRAFFIC'
    )


def create_rule():
    response = cloudwatch_events.put_rule(
    Name='DEMO_EVENT',
    RoleArn='IAM_ROLE_ARN',
    ScheduleExpression='rate(5 minutes)',
    State='ENABLED'
    
    print(response['RuleArn'])

def add_lambda_function_target():
    # Put target for rule
    response = cloudwatch_events.put_targets(
    Rule='DEMO_EVENT',
    Targets=[
        {
            'Arn': 'LAMBDA_FUNCTION_ARN',
            'Id': 'myCloudWatchEventsTarget',
        }
    ]
    )
    print(response)



def put_event():
    # Put an event
    response = cloudwatch_events.put_events(
        Entries=[
            {
                'Detail': json.dumps({'key1': 'value1', 'key2': 'value2'}),
                'DetailType': 'appRequestSubmitted',
                'Resources': [
                    'RESOURCE_ARN',
                ],
                'Source': 'com.company.myapp'
            }
        ]
    )
    print(response['Entries'])
```

### 1 - docker-compose and python development

https://dzone.com/articles/using-docker-compose-for-python-development
