# Monero payer

### Prerequisites
Единоразово необходимо установить все зависимости командой `poetry install`

### Запуск
`make up` - поднимает бд рядом в докере
`poetry run uvicorn app.main:app --reload` - стартует приложение на 8000 порту
