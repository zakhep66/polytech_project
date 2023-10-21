### Склонируйте репозиторий

```sh
$ git clone https://github.com/zakhep66/polytech_project.git
```

### Настройка Django

В корне проекта создайте виртуальное окружение и активируйте его

```sh
$ python -m venv venv (для Linux: python3 -m venv venv)
$ .\venv\Scripts\activate (для Linux: source ./venv/bin/activate)
```

#### Все последующие действия производить внутри виртуального окружения

Установите все необходимые зависимости для работы Django

```sh
$ pip install -r req.txt
```

Установите все необходимые миграции, убедитесь, что был создан файл db.sqlite3

```sh
$ python manage.py makemigrations (для Linux: python3 manage.py makemigrations)
$ python manage.py migrate (для Linux: python3 manage.py migrate)
```

Создайте суперпользователя для работы с админкой

```sh
$ python manage.py createsuperuser (для Linux: python3 manage.py createsuperuser)
```

Запустите проект

```sh
$ python manage.py runserver (для Linux: python3 manage.py runserver)
```
