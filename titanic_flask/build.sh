#!/bin/sh

# fill this script with the steps required to
# - train and save your model. eg python model.py
# - dockerise the application hosting the model which will serve it as an api, docker build . -t 100edockerregistry.azurecr.io/aiap/{your_initial}:latest
# and finally push your docker image to the registry
# Build Docker image using Dockerfile
# Dockerfile will create an image containing the training script, trained model, and predict script

systemctl start docker

echo Building Docker image...
docker build -t 100edockerregistry.azurecr.io/aiap/arvin_febriyan:latest .

# Create a docker container, initialise training and predicting code
echo Creating docker container...
docker run -d -p 8080:8080 100edockerregistry.azurecr.io/aiap/arvin_febriyan:latest

# Show newly created container
docker ps -a

# Delay for 2 seconds
sleep 2

# Run training script using cUrl
echo Training model...
curl http://0.0.0.0:8080/train

# [Testing API] Run predict script using cUrl
echo Testing prediction functionality...
curl -d '{"PassengerId": 24,
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
             "Embarked": "S"}' -H 'Content-Type: application/json' http://0.0.0.0:8080/predict
echo API tested \!

# Push docker image to registry
# docker push 100edockerregistry.azurecr.io/aiap/arvin_febriyan

