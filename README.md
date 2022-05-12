# Тестовое задание для ООО РеРиКом

Кондрашов Даниил Андреевич

email: jollkill34@gmail.com

## Задание

Структура проекта:
  - api_service_messages (api сервис сообщений)
  - listener_messages (listener сообщений из kafka)
  - docker compose (содержит все для быстрого развертывания проекта)
  - база данных Postgresql

Для подтверждения между собой api service и listener используют JWT токен.

## Проверка

Адрес для проверки: http://127.0.0.1:8000/api/v1/message

Также есть админка: http://127.0.0.1:8000/admin

user: admin
password: pass
