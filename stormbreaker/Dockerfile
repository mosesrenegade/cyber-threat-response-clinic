FROM python:3.7

WORKDIR /app

COPY requirements.txt flask_app.py ./

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["/app/flask_app.py"]
