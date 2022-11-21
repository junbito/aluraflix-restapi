FROM ubuntu:22.10

RUN apt update && \
    apt upgrade -y && \
    apt install -y python3-pip && \
    apt install -y gunicorn

WORKDIR /challenge_backend5

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY aluraflix/ aluraflix/
COPY restapi/ restapi/
COPY db.sqlite3 .

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "aluraflix.wsgi"]
