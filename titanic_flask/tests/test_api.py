import pytest
import time
import json
import requests
import multiprocessing as mp

from ..src.app import app

PORT = 5000
BASE_URL = 'http://localhost:%s' % PORT
DATA_FULL = {"PassengerId": 24,
             "Survived": 1,
             "Pclass": 1,
             "Name": "Sloper, Mr. William Thompson",
             "Sex": "male",
             "Age": 28,
             "SibSp": 0,
             "Parch": 0,
             "Ticket": 113788,
             "Fare": 35.5,
             "Cabin": "A6",
             "Embarked": "S"}
DATA_MISSING = {"PassengerId": 24,
                "Survived": 1,
                "Pclass": 1,
                "Name": "Sloper, Mr. William Thompson",
                "Sex": "male",
                "Age": 28,
                "SibSp": 0,
                "Parch": 0,
                # "Ticket": NaN,
                "Fare": 35.5,
                "Cabin": "A6",
                "Embarked": "S"}

proc = mp.Process(target=app.run)


@pytest.fixture(scope="module", autouse=True)
def setup():
    proc.start()
    time.sleep(1)  # sleep a little to make sure Flask app is up
    yield
    proc.terminate()


def test_train():

    res = requests.post(f"{BASE_URL}/train", json={})
    res_json = json.loads(res.text)
    assert res_json["success"] == 1


def test_predict():

    for data in [DATA_FULL, DATA_MISSING]:
        res = requests.post(f"{BASE_URL}/predict", json=data)
        res_json = json.loads(res.text)
        assert res_json["PassengerId"] == data["PassengerId"]
        assert res_json["Survived"] == data["Survived"]
