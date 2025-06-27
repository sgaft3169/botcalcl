# Telegram Tariff Bot (Replit + PostgreSQL Ready)

Этот бот рассчитывает выгоду от смены тарифа, генерирует Excel и PDF-отчёты и сохраняет историю в PostgreSQL.

## ⚙️ Настройка

1. Клонируй репозиторий или загрузи архив
2. Укажи переменные окружения:
   - BOT_TOKEN
   - ADMIN_ID
   - CHANNEL_ID
   - DATABASE_URL (из Railway)

## 🚀 Запуск (Replit)

- Replit автоматически устанавливает зависимости из `requirements.txt`
- Flask-сервер нужен для поддержки UptimeRobot (бот не уснёт)
- Запусти файл `main.py`

## 🗃 История сохраняется в PostgreSQL

Если базы нет, создай на https://railway.app и вставь `DATABASE_URL` в `.env`.

## ✅ Команды бота

- `/start` — запуск расчёта
- `/cancel` — отмена
- `/history` — выгрузка истории
- `/help` — описание всех команд
