# Развёртывание через docker:
Убедитесь, что на машине есть [docker]

### Создайте папку, где должен лежать проект:
$ mkdir storage_project
$ cd storage_project

### Создайте Dockerfile и вставьте следующее (для локали):
```
FROM python:3.6
RUN apt-get update
RUN mkdir /storage_project
WORKDIR /storage_project
RUN apt-get install git
RUN git clone https://github.com/Amankaium/storage.git
RUN pip install -r storage/req.txt
CMD python storage/manage.py runserver 0.0.0.0:8080
````
Для деплоя на сервере поменяйте последнюю строку:
```
CMD python storage/manage.py runserver 0.0.0.0:80
```

### Создайте образ:
```
$ sudo docker build -t storage .
```

И запустите его на локальной машине:
```
$ sudo docker run -d -p 8080:8080 storage 
```

или на сервере:
```
$ sudo docker run -d -p 80:80 storage 
```
Вы получите ID контейнера (guid)

### Для выключения/запуска/остановки/удаления контейнера:
```
$ sudo docker stop/start/kill/rm <guid контейнера>
```

[docker]: <https://docs.docker.com/install/linux/docker-ce/ubuntu/>
