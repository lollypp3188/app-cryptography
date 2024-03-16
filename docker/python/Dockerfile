FROM python:3.10

ADD . /srv

WORKDIR /srv

RUN pip install -r requirements.txt

COPY . /srv

CMD ["python","app.py"]

