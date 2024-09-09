import joblib
import boto3
import os

s3 = boto3.client('s3')
s3.download_file('ml-iris-demo-project-new-bucket', 'model/model.joblib', '/tmp/model.joblib')

model = joblib.load('/tmp/model.joblib')

def predict(data):
    return model.predict(data)
