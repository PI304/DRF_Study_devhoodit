# DRF_Study_devhoodit
Django Rest Framework Study

# Initial Install
```
pip install django
pip install djangorestframework
pip install mysqlclient
pip install django-dotenv
django-admin startproject kchat
cd kchat
python manage.py startapp user
```

```
powershell> mysql -uroot -hlocalhost -p
mysql> create database kchat character set utf8mb4 collate utf8mb4_general_ci;
mysql> use kchat
mysql> show tables;
```

# Endpoints

### User

User Table
id (pk) nickname uuid (fk) profile_img_url profile_message last_login
UserPrivate Table
login_id password uuid (fk) email created_at updated_at