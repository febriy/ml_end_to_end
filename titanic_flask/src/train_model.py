import os
import joblib
from datapipeline import *
from model.model import *


my_path = os.path.abspath(os.path.dirname(__file__))
print("my_path: ", my_path)
model_path = os.path.join(my_path, "model/model.pkl")
print("model_path:", model_path)

# Import and process data
titanic_clean = transform(
    "https://aisgaiap.blob.core.windows.net/aiap-assignments-data/titanic.csv"
)
# Instantiate, train, and save model
Model_1 = Model()
params = Model_1.get_default_params()
model, roc_auc = Model_1.train(params, titanic_clean)
joblib.dump(model, model_path)
print("Model saved at: ", model_path)
