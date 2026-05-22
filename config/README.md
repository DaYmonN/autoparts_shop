# Конфигурационные файлы для развертывания

## Структура

config/
├── nginx/
│ └── autoparts.conf # Конфигурация сайта для nginx
├── uwsgi/
│ ├── autoparts.ini # Конфигурация uWSGI
│ └── autoparts.service # systemd сервис для автозапуска
└── README.md


## Установка конфигураций

### 1. Nginx
```bash
# Копирование конфигурации
sudo cp config/nginx/autoparts.conf /etc/nginx/sites-available/autoparts

# Активация сайта
sudo ln -s /etc/nginx/sites-available/autoparts /etc/nginx/sites-enabled/

# Удаление дефолтного сайта (опционально)
sudo rm -f /etc/nginx/sites-enabled/default

# Проверка конфигурации
sudo nginx -t

# Перезапуск nginx
sudo systemctl restart nginx
