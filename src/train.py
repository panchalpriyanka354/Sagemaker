import sagemaker
from sagemaker.sklearn.estimator import SKLearn
from sagemaker import get_execution_role

# Define SageMaker execution role and session
role = get_execution_role()
session = sagemaker.Session()

# S3 bucket and data locations
bucket = 'ml-iris-demo-project-new-bucket'
train_data = f's3://{bucket}/data/iris_train.csv'

# Set up the SKLearn Estimator for training
sklearn_estimator = SKLearn(
    entry_point='train.py',
    role=role,
    instance_count=1,
    instance_type='ml.m5.large',
    framework_version='0.23-1',
    sagemaker_session=session,
    output_path=f's3://{bucket}/model/'
)

# Start the training job
sklearn_estimator.fit({'train': train_data})
