FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y graphviz graphviz-dev
RUN apt install -y netcat-traditional
RUN pip install --upgrade pip

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . /code

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh