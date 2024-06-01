import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    sns = boto3.client('sns')

    bucket_from = s3.Bucket("s3-start")
    bucket_to = "s3-finish"

    for obj in bucket_from.objects.filter(Prefix=''):
        copy_source = {'Bucket': "s3-start", 'Key': obj.key}

        bucket_to_name = obj.key
        s3.meta.client.copy(copy_source, bucket_to, bucket_to_name)

        # Publish a message to SNS topic
        sns.publish(
            TopicArn=os.environ['SNS_TOPIC_ARN'],
            Message=f"File {obj.key} has been copied from s3-start to s3-finish"
        )

    