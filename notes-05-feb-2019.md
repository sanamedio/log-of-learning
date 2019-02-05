# 05-feb-2019

### 4 - not python but useful for local projects

- ```docker network create docker-network```
- ```docker-compose up```
- sets up lot of useful tools for learning system design like kafka, mysql, zookeeper, cassandra, haproxy, nginx, spark, memcached, redis, activemq, elasticsearch, logstash, kibana, solr, mongo, postgres

```yaml
version: '3'

services:
 
  spark_master:
    image: sequenceiq/spark:1.4.0
    hostname: spark_master
    ports:
    - "4040:4040"
    - "8042:8042"
    - "7077:7077"
    - "8088:8088"
    - "8080:8080"
    restart: always
    #mem_limit: 1024m
    command: bash /usr/local/spark/sbin/start-master.sh && ping localhost > /dev/null

  spark_worker:
    image: sequenceiq/spark:1.4.0
    links:
    - spark_master:spark_master
    expose:
    - "8081"
    restart: always
    command: bash /usr/local/spark/sbin/start-slave.sh spark://master:7077 && ping localhost >/dev/null




  memcached:
    image: bitnami/memcached:latest

  cassandra:
    image: bitnami/cassandra:latest

  solr:
    image: solr
    ports:
      - "8983:8983"

  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    ports:
            - "2181:2181"
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000


  mongo:
    image: mongo
    ports:
        - "27017:27017"

  kafka:
    image: confluentinc/cp-kafka:latest
    depends_on:
      - zookeeper
    ports:
            - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1

  mysql:
    image: mysql:5.7
    environment:
      MYSQL_DATABASE: 'db'
      MYSQL_USER: 'user'
      MYSQL_PASSWORD: 'password'
      MYSQL_ROOT_PASSWORD: 'password'
    ports:
      - '3306:3306'
    expose:
      - '3306'

  redis:
    image: redis
    ports:
      - "6379:6379"

  postgres:
      image: postgres
      ports:
          - "5432:5432"
      environment:
          POSTGRES_USER: "user"
          POSTGRES_PASSWORD: "password"

  haproxy:
    image: dockercloud/haproxy
    environment:
      - BALANCE=leastconn
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - 8099:80


  nginx: 
    image: nginx:latest
    ports:
      - 80:80
      - 443:443


  activemq:
    image: webcenter/activemq:5.14.3
    ports:
      # mqtt
      - "1883:1883"
      # amqp
      - "5672:5672"
      # ui
      - "8161:8161"
      # stomp
      - "61613:61613"
      # ws
      - "61614:61614"
      # jms
      - "61616:61616"
    environment:
      ACTIVEMQ_REMOVE_DEFAULT_ACCOUNT: "true"
      ACTIVEMQ_ADMIN_LOGIN: admin
      ACTIVEMQ_ADMIN_PASSWORD: password
      ACTIVEMQ_WRITE_LOGIN: write
      ACTIVEMQ_WRITE_PASSWORD: password
      ACTIVEMQ_READ_LOGIN: read
      ACTIVEMQ_READ_PASSWORD: password
      ACTIVEMQ_JMX_LOGIN: jmx
      ACTIVEMQ_JMX_PASSWORD: password
      ACTIVEMQ_STATIC_TOPICS: static-topic-1;static-topic-2
      ACTIVEMQ_STATIC_QUEUES: static-queue-1;static-queue-2
      ACTIVEMQ_ENABLED_SCHEDULER: "true"
      ACTIVEMQ_MIN_MEMORY: 512
      ACTIVEMQ_MAX_MEMORY: 2048

  elasticsearch:
    ulimits:
        nofile:
            soft: 65536
            hard: 65536
    image: docker.elastic.co/elasticsearch/elasticsearch-oss:6.2.2
    ports:
      - "9200:9200"
      - "9300:9300"
    environment:
      ES_JAVA_OPTS: "-Xms1g -Xmx1g"


  logstash:
    image: docker.elastic.co/logstash/logstash-oss:6.2.2
    ports:
      - "5000:5000"
    depends_on:
      - elasticsearch
    links:
      - elasticsearch

  kibana:
    image: docker.elastic.co/kibana/kibana-oss:6.2.2
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch
    links:
        - elasticsearch

networks:
  default:
      external:
        name: docker-network
```

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
