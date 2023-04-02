FROM python:3.10-slim

RUN apt update && mkdir callout && python -m pip install --upgrade pip && pip install --upgrade pip setuptools

RUN apt install -y libavdevice-dev -y libavfilter-dev -y libopus-dev -y libvpx-dev -y pkg-config

RUN apt install -y libsrtp2-dev

RUN apt-get install -y \
    python3-pip

RUN pip3 install aiortc

WORKDIR /callout

COPY ./src ./src
COPY ./.black.toml ./.black.toml
COPY ./commands ./commands
COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

EXPOSE 8008

CMD ["bash"]

