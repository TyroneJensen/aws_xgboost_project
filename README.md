# AWS XGBoost Project

This project demonstrates how to use AWS SageMaker to train and deploy an XGBoost model. The project utilizes built-in SageMaker datasets for training, validation, and testing.

## Project Structure
- **train.py**: Script to train the XGBoost model using SageMaker.
- **deploy.py**: Script to deploy the trained model as an endpoint.
- **predict.py**: Script to make predictions using the deployed model.
- **requirements.txt**: List of required Python packages.

## Getting Started
1. Set up AWS credentials and configure SageMaker.
2. Run `train.py` to train the model.
3. Run `deploy.py` to deploy the model.
4. Use `predict.py` to make predictions.

## Requirements
- AWS Account
- SageMaker Role with necessary permissions
- Python 3.x
- Boto3
- Sagemaker Python SDK

## Notes
- Ensure your AWS credentials are configured correctly.
- The project uses SageMaker's built-in datasets for simplicity.

## License
This project is licensed under the MIT License.
