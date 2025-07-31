FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY pyproject.toml poetry.lock* README.md /app/
RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi
COPY . /app/
EXPOSE 8000
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers=3"]