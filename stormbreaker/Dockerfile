FROM python:3.6

WORKDIR /app

COPY ./ /app/

RUN pip install -r requirements.txt

ENV FLASK_APP="stormbreaker"

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
