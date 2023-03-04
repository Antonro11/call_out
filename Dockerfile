FROM python:3.10-slim

RUN apt update && mkdir callout && python -m pip install --upgrade pip && pip install --upgrade pip setuptools

WORKDIR /callout

COPY ./src ./src
COPY ./.black.toml ./.black.toml
COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

EXPOSE 8008

CMD ["python", "src/manage.py", "runserver", "0:8008"]

