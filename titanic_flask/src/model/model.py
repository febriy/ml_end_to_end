from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc
import joblib


class Model:
    """Create a Model instance to train random forests and return auc_roc score

    Attributes:
        params: Initial/ default parameters for model

    Methods:
        get_default_params: Return default parameters
        train: Train random forest and return auc_roc score
    """

    def __init__(self):
        # init your model here
        self.params = {
            "bootstrap": True,
            "class_weight": None,
            "criterion": "gini",
            "max_depth": None,
            "max_features": "auto",
            "max_leaf_nodes": None,
            "min_impurity_decrease": 0.0,
            "min_impurity_split": None,
            "min_samples_leaf": 1,
            "min_samples_split": 2,
            "min_weight_fraction_leaf": 0.0,
            "n_estimators": 100,
            "n_jobs": None,
            "oob_score": False,
            "random_state": None,
            "verbose": 0,
            "warm_start": False,
        }

    def train(self, params, data):
        """ This method takes in cleaned data and parameters,
            train a random forest model, and output roc_auc score.
        """
        # Create feature and target dataframe
        feat = data.drop("Survived", axis=1)
        target = data["Survived"]

        model_columns = list(feat.columns)
        joblib.dump(model_columns, "model-columns.pkl")

        # Splitting data
        feat_train, feat_test, target_train, target_test = train_test_split(
            feat, target, test_size=0.2, random_state=0
        )

        # Fitting
        rf = RandomForestClassifier()
        rf.set_params(**params)
        rf.fit(feat_train, target_train)
        target_pred = rf.predict(feat_test)

        # Return a evaluation metric (roc_auc in this case) as a single float so the caller can make use of it
        false_pos_rate, true_pos_rate, thresholds = roc_curve(target_test, target_pred)
        roc_auc = auc(false_pos_rate, true_pos_rate)
        return rf, roc_auc

    def get_default_params(self):
        # return the default params your model will use
        return self.params

    def predict(self, input_data):
        prediction = rf.predict(input_data)
        return prediction
