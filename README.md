# Monero payer

### Prerequisites
Единоразово необходимо установить все зависимости командой `poetry install`

### Запуск
`make up` - поднимает бд рядом в докере
`poetry run uvicorn app.main:app --reload` - стартует приложение на 8000 порту
`docker-compose up -d` - запустить контейнер
`poetry shell` - `C:\Proct\Monero_payer\app`
    `alembic upgrade head` - миграция БД
