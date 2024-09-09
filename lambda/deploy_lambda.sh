#!/bin/bash
zip function.zip lambda_function.py
aws lambda create-function --function-name iris-predictor \
--zip-file fileb://function.zip --handler lambda_function.lambda_handler \
--runtime python3.9 --role arn:aws:iam::<your-account-id>:role/<your-lambda-role> \
--timeout 30
