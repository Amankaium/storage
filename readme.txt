Убедитесь что у вас есть python3 (желательно python 3.6.5).
Развёртывание на virtual environment:


На windows (python по умолчанию python3.6)
1) Создайте пустую папку, внутри создайте виртульное окружение:
mkdir storage
virtualenv venv
2) Вставьте папку с проектом (storage) рядом с venv
git clone https://github.com/Amankaium/storage.git
3) Активация venv
call venv\Scripts\activate
4) Либы (requirements)
cd storage
pip install -r req.txt
5) Миграция таблиц БД
python manage.py migrate
6) Запуск сайта
python manage.py runserver


Если на ubuntu с python (2.x) и python3, то
1) Создайте пустую папку, внутри создайте виртульное окружение:
mkdir storage
virtualenv -p python3 virtualenv
2) Вставьте папку с проектом (storage) рядом с venv
https://github.com/Amankaium/storage.git
3) Активация venv
source venv/bin/activate
4) Либы (requirements)
cd storage
pip install -r req.txt
5) Миграция таблиц БД
python manage.py migrate
6) Запуск сайта
python manage.py runserver
