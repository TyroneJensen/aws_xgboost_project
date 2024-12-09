import sagemaker
from sagemaker import get_execution_role
from sagemaker.inputs import TrainingInput
from sagemaker.estimator import Estimator

# Set up SageMaker session and role
sagemaker_session = sagemaker.Session()
role = get_execution_role()

# Define the XGBoost container
container = sagemaker.image_uris.retrieve("xgboost", sagemaker_session.boto_region_name, "latest")

# Set up the estimator
xgboost_estimator = Estimator(
    image_uri=container,
    role=role,
    instance_count=1,
    instance_type="ml.m5.large",
    volume_size=5,
    max_run=3600,
    sagemaker_session=sagemaker_session
)

# Set hyperparameters
xgboost_estimator.set_hyperparameters(
    objective="binary:logistic",
    num_round=100
)

# Updated S3 paths for processed data
train_input = TrainingInput("s3://your-bucket-name/data/processed_train.csv", content_type="csv")
validation_input = TrainingInput("s3://your-bucket-name/data/processed_validation.csv", content_type="csv")

# Start training
xgboost_estimator.fit({"train": train_input, "validation": validation_input})
