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

## Jenkins

Запуск Jenkins на сервере:

```bash
docker run -d \
  -p 8080:8080 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --name jenkins \
  jenkins/jenkins:lts
```

Получить пароль для первого входа:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Перезапуск Jenkins:

```bash
docker restart jenkins
```

## SSH

Генерация ключа и копирование на сервер:

```bash
ssh-keygen -t rsa
ssh-copy-id root@45.90.216.186
```

Конвертация ключа в PEM формат (для Jenkins):

```bash
ssh-keygen -p -m PEM -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa
```
