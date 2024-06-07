import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')

    source = 's3-start'
    destination = 's3-finish'

    # Extract key from the event
    key = event['Records'][0]['s3']['object']['key']

    # Copy object from source to destination
    copy_object = {'Bucket': source, 'Key': key}
    s3.meta.client.copy(copy_object, destination, key)

    return {
        'statusCode': 200,
        'body': 'Objects copied successfully!'
    }
