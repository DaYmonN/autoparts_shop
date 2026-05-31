================================================================================
                    АВТОЗАПЧАСТИ - ИНТЕРНЕТ-МАГАЗИН
                          Руководство по развертыванию
================================================================================

ОГЛАВЛЕНИЕ:
1. Системные требования
2. Установка и настройка
3. Запуск проекта
4. Работа с сайтом
5. Устранение неполадок
6. Структура проекта

================================================================================
1. СИСТЕМНЫЕ ТРЕБОВАНИЯ
================================================================================

Минимальные требования:
- Операционная система: Windows 10/11, macOS, Linux
- Python: версия 3.8 или выше
- MySQL: версия 8.0 или выше (или SQLite для разработки)
- Оперативная память: 4 ГБ
- Дисковое пространство: 500 МБ

Необходимое ПО:
- Python (https://www.python.org/downloads/)
- MySQL (https://dev.mysql.com/downloads/mysql/)
- Git (опционально, для клонирования репозитория)

================================================================================
2. УСТАНОВКА И НАСТРОЙКА
================================================================================

2.1. Установка Python и зависимостей

# Проверьте версию Python:
python --version

# Установите необходимые пакеты:
pip install django
pip install mysqlclient
pip install pillow
pip install pymysql

# Или установите все зависимости из файла (если есть requirements.txt):
pip install -r requirements.txt

2.2. Настройка базы данных

ВАРИАНТ A: MySQL (для production)

# 1. Установите MySQL Server
#    - Скачайте с https://dev.mysql.com/downloads/installer/
#    - Выберите "Developer Default"
#    - Задайте пароль root (запомните его!)

# 2. Создайте базу данных:
mysql -u root -p
CREATE DATABASE autoparts_shop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;

# 3. Настройте подключение в файле autoparts_shop/settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'autoparts_shop',
        'USER': 'root',
        'PASSWORD': 'ВАШ_ПАРОЛЬ',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# 4. Создайте файл autoparts_shop/__init__.py с содержимым:
import pymysql
pymysql.install_as_MySQLdb()

ВАРИАНТ B: SQLite (для разработки, проще)

# Просто оставьте настройки по умолчанию в settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

2.3. Миграции базы данных

# Создайте миграции:
python manage.py makemigrations
python manage.py migrate

# Создайте суперпользователя (администратора):
python manage.py createsuperuser
# Следуйте инструкциям: введите логин, email, пароль

2.4. Загрузка тестовых данных (опционально)

# Загрузите тестовые бренды и товары:
python manage.py load_data

# Или добавьте больше товаров:
python manage.py generate_parts  # если есть такая команда

2.5. Статические файлы

# Соберите статические файлы:
python manage.py collectstatic

================================================================================
3. ЗАПУСК ПРОЕКТА
================================================================================

3.1. Локальный запуск (для разработки)

# Перейдите в папку с проектом:
cd путь_к_папке/autoparts_shop

# Запустите сервер разработки:
python manage.py runserver

# Откройте браузер и перейдите по адресу:
http://127.0.0.1:8000/

3.2. Запуск на другом порту

python manage.py runserver 8080

3.3. Доступ с других устройств в сети

python manage.py runserver 0.0.0.0:8000

# Затем откройте на другом устройстве: http://IP_вашего_компьютера:8000/

================================================================================
4. РАБОТА С САЙТОМ
================================================================================

4.1. Доступные URL-адреса:

Главная страница (каталог):      http://127.0.0.1:8000/
Админ-панель:                    http://127.0.0.1:8000/admin/
Корзина:                         http://127.0.0.1:8000/cart/
Вход:                            http://127.0.0.1:8000/users/login/
Регистрация:                     http://127.0.0.1:8000/users/register/
Личный кабинет:                  http://127.0.0.1:8000/users/profile/

4.2. Функциональность:

- Просмотр каталога автозапчастей
- Фильтрация по марке автомобиля
- Фильтрация по категории товара
- Поиск по артикулу или названию
- Добавление товаров в корзину
- Регистрация и авторизация пользователей
- Личный кабинет с историей заказов
- Админ-панель для управления товарами

4.3. Доступ в админ-панель:

- Перейдите на http://127.0.0.1:8000/admin/
- Введите логин и пароль суперпользователя (созданного в п.2.3)

================================================================================
5. УСТРАНЕНИЕ НЕПОЛАДОК
================================================================================

5.1. Ошибка "ModuleNotFoundError: No module named 'pymysql'"

Решение:
pip install pymysql

5.2. Ошибка "Error loading MySQLdb module"

Решение:
# В файле autoparts_shop/__init__.py добавьте:
import pymysql
pymysql.install_as_MySQLdb()

5.3. Ошибка "Access denied for user 'root'@'localhost'"

Решение:
# Проверьте пароль в settings.py
# Или создайте нового пользователя MySQL:
mysql -u root -p
CREATE USER 'shop_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON autoparts_shop.* TO 'shop_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;

# Затем обновите данные в settings.py

5.4. Ошибка "Can't connect to MySQL server"

Решение:
# Запустите MySQL сервер:
# Windows: services.msc -> MySQL80 -> Запустить
# Linux: sudo systemctl start mysql
# macOS: brew services start mysql

5.5. Ошибка "Table doesn't exist"

Решение:
# Выполните миграции заново:
python manage.py migrate

5.6. Ошибка "No module named 'catalog'"

Решение:
# Убедитесь, что приложения catalog, cart, users добавлены в INSTALLED_APPS
# в файле settings.py

5.7. Статические файлы не отображаются

Решение:
# Убедитесь, что в settings.py есть:
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# И выполните:
python manage.py collectstatic

5.8. Картинки не загружаются

Решение:
# Проверьте настройки MEDIA в settings.py:
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# И в urls.py добавьте:
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

================================================================================
6. СТРУКТУРА ПРОЕКТА
================================================================================

autoparts_shop/
├── autoparts_shop/          # Основная конфигурация проекта
│   ├── __init__.py
│   ├── settings.py          # Настройки проекта
│   ├── urls.py              # Главные URL-адреса
│   ├── wsgi.py              # WSGI конфигурация
│   └── asgi.py              # ASGI конфигурация
│
├── catalog/                 # Приложение каталога
│   ├── migrations/          # Миграции БД
│   ├── admin.py             # Настройка админ-панели
│   ├── models.py            # Модели данных (Brand, Part)
│   ├── views.py             # Контроллеры
│   ├── urls.py              # URL-адреса каталога
│   └── management/          # Управляющие команды
│
├── cart/                    # Приложение корзины
│   ├── migrations/
│   ├── models.py            # Модели (Order, OrderItem)
│   ├── views.py             # Корзина и заказы
│   └── context_processors.py # Переменные для шаблонов
│
├── users/                   # Приложение пользователей
│   ├── views.py             # Регистрация, вход, профиль
│   ├── forms.py             # Формы регистрации
│   └── urls.py
│
├── templates/               # HTML-шаблоны
│   ├── base.html            # Базовый шаблон
│   ├── catalog/
│   │   ├── catalog.html     # Список товаров
│   │   └── part_detail.html # Детальная страница
│   ├── cart/
│   │   └── cart.html        # Корзина
│   └── users/
│       ├── login.html
│       ├── register.html
│       └── profile.html
│
├── static/                  # Статические файлы (CSS, JS)
├── media/                   # Загруженные изображения
├── db.sqlite3              # База данных SQLite (если используется)
├── manage.py               # Управляющий скрипт Django
└── README.txt              # Этот файл

================================================================================
7. ДОПОЛНИТЕЛЬНЫЕ КОМАНДЫ
================================================================================

# Очистка базы данных и создание заново:
python manage.py flush

# Создание резервной копии данных:
python manage.py dumpdata > backup.json

# Восстановление из резервной копии:
python manage.py loaddata backup.json

# Проверка целостности проекта:
python manage.py check

# Просмотр всех URL-адресов:
python manage.py show_urls

# Запуск тестов:
python manage.py test

# Создание нового приложения:
python manage.py startapp app_name

================================================================================
8. ПЕРЕХОД НА ПРОДАКШН
================================================================================

Для развертывания на production сервере:

1. Установите DEBUG = False в settings.py
2. Настройте ALLOWED_HOSTS = ['ваш-домен.com']
3. Используйте переменные окружения для секретных ключей
4. Настройте HTTPS (SSL/TLS)
5. Используйте uWSGI + Nginx
6. Настройте регулярные резервные копии базы данных

Пример настройки для production (nginx + uWSGI):

# Конфигурация uWSGI (файл uwsgi.ini):
[uwsgi]
chdir = /путь/к/проекту
module = autoparts_shop.wsgi:application
home = /путь/к/venv
master = true
processes = 4
socket = /путь/к/проекту/autoparts.sock
chmod-socket = 666
vacuum = true

# Конфигурация nginx (/etc/nginx/sites-available/autoparts):
server {
    listen 8000;
    server_name localhost;
    
    location /static/ {
        alias /путь/к/проекту/staticfiles/;
    }
    
    location / {
        include uwsgi_params;
        uwsgi_pass unix:///путь/к/проекту/autoparts.sock;
    }
}

# Запуск uWSGI:
uwsgi --ini uwsgi.ini --daemonize=/tmp/uwsgi.log

# Запуск nginx:
sudo systemctl restart nginx

Конфигурационные файлы находятся в папке config/:
- config/nginx/autoparts.conf - настройки nginx
- config/uwsgi/autoparts.ini - настройки uWSGI
- config/uwsgi/autoparts.service - systemd сервис

================================================================================
9. ПОЛЕЗНЫЕ ССЫЛКИ
================================================================================

Документация Django:        https://docs.djangoproject.com/
Документация Bootstrap:     https://getbootstrap.com/docs/5.3/
MySQL документация:         https://dev.mysql.com/doc/
Bootstrap иконки:           https://icons.getbootstrap.com/

================================================================================
10. КОНТАКТНАЯ ИНФОРМАЦИЯ
================================================================================

Разработчик: [Ваше имя]
Проект: Интернет-магазин автозапчастей
Версия: 1.0
Дата: 2026

================================================================================
                     © 2026 АвтоЗапчасти. Анима.
================================================================================
