FROM python:3.6

RUN apt-get update

RUN mkdir /storage_project
WORKDIR /storage_project

RUN apt-get install git
RUN git clone https://github.com/Amankaium/storage.git
RUN pip install -r storage/req.txt

CMD python storage/manage.py runserver 0.0.0.0:8080
