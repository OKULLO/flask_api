FROM python:3.6.9

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD . /app

CMD [ "uwsgi", "app.ini" ]