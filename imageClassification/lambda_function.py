import boto3
import json
import base64

ENDPOINT = "image-classification-2022-08-16-15-07-39-792"
runtime = boto3.Session().client('sagemaker-runtime')

def lambda_handler(event, context):
    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])

    # Make a prediction
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType='image/png', Body=image)

    inferences = json.loads(response['Body'].read().decode())

    # We return the data back to the Step Function
    event['body']['inferences'] = inferences
    return {
        'statusCode': 200,
        # 'body': json.dumps(event['body'])
        'body': event['body']
    }