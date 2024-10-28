FROM python:3.12-alpine
ENV DEBIAN_FRONTEND='noninteractive'
RUN pip install poetry
ENV PATH="${PATH}:/root/.local/bin"
COPY ./src /app/src
COPY migration /app/migration
COPY alembic.ini /app/
COPY pyproject.toml /app/
ENV PYTHONPATH /app/src
WORKDIR /app
RUN poetry config virtualenvs.create false \
    && poetry install --no-root
RUN chmod +x ./src/start.sh
EXPOSE 8000