from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Endpoint name for SageMaker
ENDPOINT_NAME = 'iris-endpoint'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    # Send request to Lambda endpoint or directly to SageMaker
    response = requests.post('https://<lambda-url>', json={'data': data})
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
