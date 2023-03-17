FROM python:3.10-slim

RUN apt update && mkdir callout && python -m pip install --upgrade pip && pip install --upgrade pip setuptools

WORKDIR /callout

RUN apt install -y libgl1-mesa-glx

COPY ./src ./src
COPY ./.black.toml ./.black.toml
COPY ./commands ./commands
COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

EXPOSE 8008

CMD ["bash"]

