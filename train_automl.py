import pandas as pd
from supervised import AutoML

# Read data
df = pd.read_csv("data/train.csv")
    
X_train = df.drop(columns=["charges"])
y_train = df["charges"]

# Train AutoML
automl = AutoML(
    results_path="AutoML_Results",
)
automl.fit(X_train, y_train)

# Create App
automl.app(
    path="AutoML_App",
    title="Insurance Charges Predictor",
)

# Start App locally
# automl.local_app()

# Deploy App on platform.mljar.com
# automl.publish_app()
