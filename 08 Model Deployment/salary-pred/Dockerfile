
FROM python:3.9

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD exec gunicorn --bind :$PORT --workers 1 --thread 8 --timeout 0 app:app 

