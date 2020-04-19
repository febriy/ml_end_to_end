# Build a miniconda enabled image with python 3.6.7
FROM continuumio/miniconda3@sha256:d7ab0b98c5adad49ed5dabf11a93d53361f08445b998945d80d351b417d4e0ba

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./src/ /app

EXPOSE 8080

# run
ENV FLASK_APP=app.py
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
#CMD [ "python", "app.py" ]

