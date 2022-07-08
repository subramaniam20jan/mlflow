FROM python:3.10-slim

WORKDIR /mlflow

COPY .env /mlflow/.env
COPY startup_mlflow.sh /mlflow/startup_mlflow.sh

COPY requirements.txt  /mlflow/requirements.txt
RUN pip install -r requirements.txt

CMD ["bash", "startup_mlflow.sh"]