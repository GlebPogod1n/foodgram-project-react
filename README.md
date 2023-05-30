 ## Продуктовый помощник - foodgram

 ![workflow](https://github.com/HelloAgni/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

# Foodrgam

 Продуктовый помощник - дипломный проект курса Backend-разработки Яндекс.Практикум. Проект представляет собой онлайн-сервис и API для него. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Проект реализован на `Django` и `DjangoRestFramework`. Доступ к данным реализован через API-интерфейс. Документация к API написана с использованием `Redoc`.

## Особенности реализации

- Проект завернут в Docker-контейнеры;
- Образы foodgram_frontend и foodgram_backend запушены на DockerHub;
- Реализован workflow c автодеплоем на удаленный сервер и отправкой сообщения в Telegram;
- Проект был развернут на сервере: <http://158.160.27.148/recipes>

## Развертывание проекта

git clone git@github.com:GlebPogod1n/foodgram-project-react.git
```
- подключитесь к серверу
```
ssh <server user>@<server IP>
```
- Установите Docker
```
sudo apt install docker.io
```
- Установите Docker Compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
- Создайте файл env:
```
touch .env
```
- Заполните:
```
DEBUG=False
SECRET_KEY=<Your_some_long_string>
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<Your_password>
DB_HOST=db
DB_PORT=5432
```
- Скопируйте файлы из папки 'infra/' на ваш сервер
```
- Выполните команды
```
sudo docker compose exec backend python manage.py migrate
```
sudo docker compose exec backend python manage.py collectstatic --noinput
```
загрузите ингредиенты и основные люда(по желанию):
```
sudo docker compose exec backend python manage.py loaddata dump.json
```
sudo docker compose up -d
```
Готово!


## Автор

Глеб Погодин (gleb1915526@gmail.com)