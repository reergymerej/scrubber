import json
import urllib.parse
import boto3

s3 = boto3.resource('s3')


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key'],
        encoding='utf-8'
    )

    try:
        copy_source = bucket + "/" + key
        print("source:", copy_source)
        destintation_key = key.replace("in/", "out/")
        s3.Object(bucket, destintation_key).copy_from(
            CopySource = copy_source
        )
        s3.Object(bucket, key).delete()
        print("moved")
        return 0
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

