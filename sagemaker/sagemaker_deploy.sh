#!/bin/bash

# Define the model name and endpoint
MODEL_NAME="iris-model"
ENDPOINT_NAME="iris-endpoint"

# Deploy model on SageMaker
aws sagemaker create-model --model-name $MODEL_NAME --primary-container Image=$IMAGE_URI

# Create an endpoint configuration
aws sagemaker create-endpoint-config --endpoint-config-name $ENDPOINT_NAME --model-name $MODEL_NAME

# Deploy endpoint
aws sagemaker create-endpoint --endpoint-name $ENDPOINT_NAME --endpoint-config-name $ENDPOINT_NAME
