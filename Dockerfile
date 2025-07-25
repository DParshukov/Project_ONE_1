FROM python:3.12
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY pyproject.toml poetry.lock* README.md /app/
RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi
COPY . /app/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]