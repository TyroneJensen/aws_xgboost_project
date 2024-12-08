import sagemaker
import numpy as np

# Set up SageMaker session
sagemaker_session = sagemaker.Session()

# Define the predictor
xgboost_predictor = sagemaker.predictor.Predictor(endpoint_name="xgboost-endpoint")

# Example data for prediction
sample_data = np.array([[30, 1, 1, 130, 250, 0, 0, 187, 0, 3.5, 0, 0, 2]])

# Make prediction
response = xgboost_predictor.predict(sample_data)
print("Prediction:", response)
