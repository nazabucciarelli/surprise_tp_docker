FROM python:alpine3.18
COPY . /docker-flask
WORKDIR /docker-flask

RUN pip install -r requirements.txt
EXPOSE 5005
ENTRYPOINT ["python3"]
CMD ["app.py"]