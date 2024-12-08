import sagemaker
from sagemaker import get_execution_role

# Set up SageMaker session and role
sagemaker_session = sagemaker.Session()
role = get_execution_role()

# Retrieve the latest training job
training_job_name = sagemaker_session.sagemaker_client.list_training_jobs(SortBy='CreationTime', SortOrder='Descending')['TrainingJobSummaries'][0]['TrainingJobName']

# Deploy the model
xgboost_predictor = sagemaker.predictor.Predictor(endpoint_name="xgboost-endpoint")
xgboost_predictor = sagemaker_session.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large",
    endpoint_name="xgboost-endpoint",
    model_name=training_job_name
)
