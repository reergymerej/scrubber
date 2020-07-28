import boto3
import json
import re
import urllib.parse

s3 = boto3.resource('s3')

def get_new_content(string):
    return "This is new.\n\n" + string

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key'],
        encoding='utf-8'
    )
    destintation_key = key.replace("in/", "out/")

    try:
        body = s3.Object(bucket, key).get()['Body'].read().decode()
        # print("body", body)

        new_body = get_new_content(body)
        print("new body", new_body)

        s3.Object(bucket, destintation_key).put(
            Body=new_body
        )

        # remove original
        s3.Object(bucket, key).delete()
        print("moved")
        return 0

    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}.'.format(key, bucket))
        raise e

def get_patterns():
    """
    returns a list of tuples, [regex, replacement]
    """
    blacklist = [
        'banana',
        'file',
    ]
    patterns = []
    for b in blacklist:
        pattern = re.compile(b, flags=re.IGNORECASE)
        replacement = len(b) * '*'
        patterns.append([pattern, replacement])
    return patterns

def replace_patterns(patterns, text):
    for [pattern, replacement] in patterns:
        text = re.sub(pattern, replacement, text)
    return text

if __name__ == '__main__':
    with open('../file.txt', 'r') as f:
        text = f.read()
        patterns = get_patterns()
        replaced = replace_patterns(patterns, text)
        print(replaced)
