import joblib
import pandas as pd

# Load the model
def model_fn(model_dir):
    model = joblib.load(f'{model_dir}/model.joblib')
    return model

# Predict function
def predict_fn(input_data, model):
    data = pd.DataFrame(input_data)
    return model.predict(data).tolist()
