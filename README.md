# Supernote Converter

Web API endpoint for converting Supernote .note files into PDF/Text.

## Configuring build environment

```
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
```

## Running service locally

```
uvicorn app.main:app --reload
```

## Building Docker container

```
docker build -t supernote-converter .
```
