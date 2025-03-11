
# Тестовое задание в Farpost
С использованием фреймворка Flask поднял на localhost веб сервер, который имеет два эндпоинта: 
```
api/comments
api/general
```
Оба в качестве get-параметра принимают login пользователя, по которому затем достают выданную в ТЗ информацию и отдают ее в формате JSON пользователю
 

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Команда проекта](#команда-проекта)

## Технологии
- [Flask](https://flask.palletsprojects.com/). Данный фреймворка использован для создания API 
- [peewee](https://docs.peewee-orm.com/). Данная библиотека использована для  работы с БД при помощи технологии ORM

## Использование
 1. Склонируйте репозиторий: 
	 ```sh
	 git clone https://github.com/yshelev/python_dev_shelevoi_yaroslav.git
	 cd https://github.com/yshelev/python_dev_shelevoi_yaroslav.git
	 ```
 2. Создайте и активируйте виртуальное окружение: 
	 ```sh
	 python3 -m venv .venv
	 .venv/Scripts/activate
	```
3. Установите необходимые зависимости:  	
	 ```sh
	 pip install -r requirements.txt
	 ```
 4. В папку scripts/databases добавьте ваши БД. 
 5. В папке scripts/constants создайте файл .env. Шаблон файла: 
	```python
	 logs_database="your_logs_db_filename"
	 authors_database="your_authors_db_filename"
	 ```
4. Запустите сервер:
	```sh
	 python app.py 
	 ```

## Команда проекта


- [Шелевой Ярослав](https://github.com/yshelev) — Front-End Engineer
