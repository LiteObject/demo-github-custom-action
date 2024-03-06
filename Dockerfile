# Container image that runs your code
FROM python:3.11-slim

# Copies your code file from your action repository to the filesystem path `/` of the container
# COPY entrypoint.sh /entrypoint.sh
COPY action.py .

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["python", "action.py"]