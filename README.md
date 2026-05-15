## Окружение

```bash
python3 -m venv venv
source venv/bin/activate
```

## Запуск

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Тесты

```bash
pytest tests/ -v
```

## Docker

Сборка образа (для сервера на AMD64):

```bash
docker buildx build --platform linux/amd64 -t zxckartoplya52/car-factory-api --push .
```

Запуск локально:

```bash
docker run -d -p 8000:8000 --name car-factory zxckartoplya52/car-factory-api
```

Обновление на сервере:

```bash
docker stop car-factory
docker rm car-factory
docker pull zxckartoplya52/car-factory-api
docker run -d -p 8000:8000 --name car-factory zxckartoplya52/car-factory-api
```
