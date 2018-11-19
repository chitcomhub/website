# Сайт ИТ-сообщества Чечни
Данный сайт будет построен на Django-фреймворке версии 2.1.2.
Вы также можете помочь его доработать.


# Запуск приложения на локальном сервере

1. Скопировать репозиторий: 
   git clone https://github.com/chitcomhub/website.git
   
2. Перейти в папку website

3. Запустить команду с терминала:
    pip install -r requirements.txt

4. Развернуть БД:
    python manage.py migrate
    
5. Запустить приложение:
    python manage.py runserver
