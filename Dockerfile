FROM python:3.6
MAINTAINER Shekhar Gulati "devs@getritmo.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
