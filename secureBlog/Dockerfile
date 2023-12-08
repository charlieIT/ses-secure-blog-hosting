FROM python:3.8.10-buster

RUN apt install -y libcairo2-dev pkg-config 
RUN apt install -y libz-dev libjpeg-dev libfreetype6-dev python-dev
RUN apt install -y sqlite3 libsqlite3-dev
#python3-dev python3-venv

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./secureblog /app

EXPOSE 8000

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
