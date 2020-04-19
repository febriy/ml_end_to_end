from flask import Flask, request, jsonify, make_response, render_template
import os
import joblib
import pandas as pd
from datapipeline import *

app = Flask(__name__)

my_path = os.path.abspath(os.path.dirname(__file__))
print("my_path: ", my_path)
model_path = os.path.join(my_path, "model/model.pkl")
print("model_path:", model_path)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Load model and columns
    model = joblib.load(model_path)
    input_dict = request.form.to_dict()
    print(input_dict)

    prediction = predict_dict(input_dict, model)

    return render_template(
        "index.html",
        prediction_text="Will you survive? {0}".format(prediction),
        survival_status=prediction,
    )


def predict_dict(input_dict, model):
    input_df = pd.DataFrame(input_dict, index=[0])
    encoded_df = encode(input_df, ["Pclass", "Sex"])

    model_columns = [
        "Age",
        "SibSp",
        "Parch",
        "Fare",
        "Pclass_1",
        "Pclass_2",
        "Pclass_3",
        "Sex_female",
        "Sex_male",
    ]

    empty_input = pd.DataFrame(columns=model_columns)
    full_input = empty_input.append(encoded_df).fillna(0)
    prediction = int(model.predict(full_input))
    return prediction


if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
