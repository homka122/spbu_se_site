# Сайт кафедры cистемного программирования СПБГУ

Основная ветка - **ver2_dev**

## Установка

Для установки требуется *Python 3.8*

1. Клонировать репозиторий

2. Перейти в корневую папку

3. Переключиться на ветку *ver2_dev*
```bash
git checkout ver2_dev
```

4. Создать виртуальное окружение
```bash
python -m venv venv
```

5. Активировать виртуальное окружение
```bash
venv\Scripts\activate
```

6. Подключить необходимые пакеты
```bash
pip install -r requirements.txt
```

7. Перейти в папку *src*
```bash
cd src
```

8. Инициализировать базу данных
```
python flask_se.py init
```

8. Запустить сайт
```
python flask_se.py
```

9. Сайт запускается по адресу `http://127.0.0.1:5000`
