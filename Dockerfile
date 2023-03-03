FROM python:3.10

RUN apt update

RUN mkdir /callout

WORKDIR /callout

COPY ./src ./src
COPY ./.black.toml ./.black.toml

COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install --upgrade pip setuptools
RUN pip install -r ./requirements.txt

CMD ["python", "src/manage.py", "runserver", "0:8008"]

