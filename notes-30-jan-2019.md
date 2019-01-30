# 30-jan-2019

### 3 - amazon sqs, sns and s3

- on file upload to s3, a notification is published to sns to whom a sqs and an email service has subscribed.

```python
import boto3, json

s3BucketName="trawler-urls-bucket-lokilokiloki111"




sns_topic_name = "s3-object-created-" + s3BucketName.replace (" ", "_")
sqs_queue_name = "trawlerDataProcessor"


s3_client = boto3.resource('s3')
s3_client.create_bucket(Bucket= s3BucketName )


sns_client = boto3.client('sns')
sns_topic_arn = sns_client.create_topic( Name = sns_topic_name)['TopicArn']


s3PubToSnsPolicy = {'Version': '2008-10-17',
                    'Id': 'Policy-S3-publish-to-sns', 'Statement': [{
    'Effect': 'Allow',
    'Principal': {'AWS': '*'},
    'Action': ['sns:Publish'],
    'Resource': sns_topic_arn,
    'Condition': {'ArnLike': {'aws:SourceArn': 'arn:aws:s3:*:*:'
                  + s3BucketName + ''}},
    }]}


sns_client.set_topic_attributes( TopicArn = sns_topic_arn ,
                                 AttributeName = "Policy" ,
                                 AttributeValue = json.dumps(s3PubToSnsPolicy)
                                )


sns_client.set_topic_attributes( TopicArn = sns_topic_arn ,
                                 AttributeName = "DisplayName" ,
                                 AttributeValue = 'Urls2Crawl'
                                )



bucket_notifications_configuration = {
    "TopicConfigurations" : [{
        "Events" : [ "s3:ObjectCreated:*" ],
        "TopicArn" : sns_topic_arn
        }
        ]
    }


s3_client.BucketNotification( s3BucketName).put(
                                   NotificationConfiguration = bucket_notifications_configuration )


#import pdb; pdb.set_trace()

sns_client.subscribe( TopicArn = sns_topic_arn , Protocol = "email", Endpoint="l.s.1[at]gmail.com" )


sqs_client = boto3.client('sqs')

sqs_policy = {
    "Version":"2012-10-17",
    "Statement":[
      {
        "Effect" : "Allow",
        "Principal" : { "AWS": "*" },
        "Action" : "sqs:SendMessage",
        "Resource" : "*",
        "Condition" : {
          "ArnEquals" : {
            "aws:SourceArn" : sns_topic_arn
          }
        }
      }
    ]
}


sqs_attributes = {  'DelaySeconds':'3',
                    'ReceiveMessageWaitTimeSeconds' : '20',
                    'VisibilityTimeout' : '300',
                    'MessageRetentionPeriod':'86400',
                    'Policy' : json.dumps(sqs_policy)
                }

resp = sqs_client.create_queue( QueueName = sqs_queue_name, Attributes = sqs_attributes )
sqs_queue_url = resp['QueueUrl']


resp = sqs_client.get_queue_attributes( QueueUrl = sqs_queue_url, AttributeNames=[ 'QueueArn' ] )
sqs_queue_arn = resp['Attributes']['QueueArn']

sns_client.subscribe(
    TopicArn = sns_topic_arn,
    Protocol = "sqs",
    Endpoint = sqs_queue_arn
)


s3Up = boto3.resource('s3')
s3Up.meta.client.upload_file('SOME_FILE.TXT', s3BucketName, 'hello.txt')
```

### 2 - amazon sqs

- https://lobster1234.github.io/2017/06/25/boto-and-sqs/
- unordered delivery

```python
#!/usr/local/bin/python3
import boto3
# create a boto3 client
client = boto3.client('sqs')
# create the test queue
# for a FIFO queue, the name must end in .fifo, and you must pass FifoQueue = True
client.create_queue(QueueName='test_queue')
# get a list of queues, we get back a dict with 'QueueUrls' as a key with a list of queue URLs
queues = client.list_queues(QueueNamePrefix='test_queue') # we filter to narrow down the list
test_queue_url = queues['QueueUrls'][0]
# send 100 messages to this queue
for i in range(0,100):
    # we set a simple message body for each message
    # for FIFO queues, a 'MessageGroupId' is required, which is a 128 char alphanumeric string
    enqueue_response = client.send_message(QueueUrl=test_queue_url, MessageBody='This is test message #'+str(i))
    # the response contains MD5 of the body, a message Id, MD5 of message attributes, and a sequence number (for FIFO queues)
    print('Message ID : ',enqueue_response['MessageId'])
# next, we dequeue these messages - 10 messages at a time (SQS max limit) till the queue is exhausted.
# in production/real setup, I suggest using long polling as you get billed for each request, regardless of an empty response
while True:
    messages = client.receive_message(QueueUrl=test_queue_url,MaxNumberOfMessages=10) # adjust MaxNumberOfMessages if needed
    if 'Messages' in messages: # when the queue is exhausted, the response dict contains no 'Messages' key
        for message in messages['Messages']: # 'Messages' is a list
            # process the messages
            print(message['Body'])
            # next, we delete the message from the queue so no one else will process it again
            client.delete_message(QueueUrl=test_queue_url,ReceiptHandle=message['ReceiptHandle'])
    else:
        print('Queue is now empty')
        break

```


### 1 - dynamodb flask counter

- https://medium.freecodecamp.org/how-to-create-a-serverless-service-in-15-minutes-b63af8c892e5
- this code has problems :) concurrency issues. need to think! TODO

```python
import boto3
from flask import Flask, jsonify

app = Flask(__name__)

# Initialize dynamodb access
dynamodb = boto3.resource('dynamodb')
db = dynamodb.Table('myservice-dev')

@app.route('/counter', methods=['GET'])
def counter_get():
  res = db.get_item(Key={'id': 'counter'})
  return jsonify({'counter': res['Item']['counter_value']})

@app.route('/counter/increase', methods=['POST'])
def counter_increase():
  res = db.get_item(Key={'id': 'counter'})
  value = res['Item']['counter_value'] + 1
  res = db.update_item(
    Key={'id': 'counter'},
    UpdateExpression='set counter_value=:value',
    ExpressionAttributeValues={':value': value},
  )
  return jsonify({'counter': value})
```
