# 05-feb-2019

### 3 - ec2 instance boto3 examples

```python
import boto3
ec2 = boto3.resource('ec2')


#describe instance
response = ec2.describe_instances()
print(response)



#monitor unmonitor instance
if sys.argv[1] == 'ON':
    response = ec2.monitor_instances(InstanceIds=['INSTANCE_ID'])
else:
    response = ec2.unmonitor_instances(InstanceIds=['INSTANCE_ID'])
print(response)








#create instance
ec2.create_instances(ImageId='<ami-image-id>', MinCount=1, MaxCount=5)



#stop terminate instance
ids = ['instance-id-1', 'instance-id-2', ...]


ec2.instances.filter(InstanceIds=ids).stop()
ec2.instances.filter(InstanceIds=ids).terminate()



## getting running isntances
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(instance.id, instance.instance_type)



# print  status
for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
    print(status)



# ebs snapshot
snapshot = ec2.create_snapshot(VolumeId='volume-id', Description='description')
volume = ec2.create_volume(SnapshotId=snapshot.id, AvailabilityZone='us-west-2a')
ec2.Instance('instance-id').attach_volume(VolumeId=volume.id, Device='/dev/sdy')
snapshot.delete()



# vpc configuration
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/24')
subnet = vpc.create_subnet(CidrBlock='10.0.0.0/25')
gateway = ec2.create_internet_gateway()


gateway.attach_to_vpc(VpcId=vpc.id)
gateway.detach_from_vpc(VpcId=vpc.id)

address = ec2.VpcAddress('eipalloc-35cf685d')
address.associate('i-71b2f60b')
address.association.delete()



##reboot instance

try:
    ec2.reboot_instances(InstanceIds=['INSTANCE_ID'], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You don't have permission to reboot instances.")
        raise

try:
    response = ec2.reboot_instances(InstanceIds=['INSTANCE_ID'], DryRun=False)
    print('Success', response)
except ClientError as e:
    print('Error', e)





#start and stop instances
if action == 'ON':
    # Do a dryrun first to verify permissions
    try:
        ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
else:
    # Do a dryrun first to verify permissions
    try:
        ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, call stop_instances without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
```

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
