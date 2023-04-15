FROM python:3.10-slim

RUN apt update && apt upgrade -y python3 && mkdir callout && apt-get install -y build-essential && python -m pip install --upgrade pip && pip install --upgrade pip setuptools


WORKDIR /callout

COPY ./src ./src
COPY ./.black.toml ./.black.toml
COPY ./commands ./commands
COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

EXPOSE 8008

CMD ["bash"]

