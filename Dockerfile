# Utilisez une image de base Python
FROM python:3.10.14-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction

COPY . /app

EXPOSE 8494

CMD ["poetry", "run", "python", "main.py", "--host", "0.0.0.0"]

