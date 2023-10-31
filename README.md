### Склонируйте репозиторий

```sh
$ git clone https://github.com/zakhep66/polytech_project.git
```

### Настройка Django

В корне проекта создайте виртуальное окружение и активируйте его.

1) Вы можете использовать любое имя при создании виртуального окружения:
```sh
$ python -m venv yovenv (для Linux: python3 -m venv yovenv)
```

2) Активируйте виртуальное окружение:
```
$ .\yovenv\Scripts\activate.bat (для Linux: source ./yovenv/bin/activate)
```

![Важно](https://img.shields.io/badge/-Важно-red) ❗ <em>Вам необходимо запускать виртуальное окружение  **КАЖДЫЙ&nbsp;РАЗ** когда Вы открываете новую командную строку или терминал для работы с проектом!</em>


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
