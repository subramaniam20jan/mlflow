#!/bin/bash

# Set environment variables to default wherever neccesary
source .env

# Startup the mlflow ui server
mlflow ui --backend-store-uri $BACKEND_STORE_URI --default-artifact-root $DEFAULT_ARTIFACT_ROOT --artifacts-destination $ARTIFACTS_DESTINATION --port $PORT --host $HOST