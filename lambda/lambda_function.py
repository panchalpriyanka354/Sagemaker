import boto3
import json

sagemaker_runtime = boto3.client('sagemaker-runtime')

def lambda_handler(event, context):
    # Example input data for prediction
    payload = event['data']

    # SageMaker endpoint name
    endpoint_name = 'iris-endpoint'

    # Call the SageMaker endpoint
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='application/json',
        Body=json.dumps(payload)
    )

    result = json.loads(response['Body'].read().decode())
    return {'statusCode': 200, 'body': json.dumps(result)}
