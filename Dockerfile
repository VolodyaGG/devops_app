FROM python:3.12-slim@sha256:e31013b9573989b2dc2f0cb688044c9e650c2721dd52c54d0fd3c669d3548bb6 as base
WORKDIR /project
RUN adduser --disabled-password --gecos "" user
ENV PORT=8000


FROM base as builder
ENV POETRY_VERSION=2.3.3 \
    POETRY_PLUGIN_EXPORT_VERSION=1.9.0
COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION" "poetry-plugin-export==$POETRY_PLUGIN_EXPORT_VERSION" \
    && poetry export -f requirements.txt --output requirements.txt --without-hashes --only main \
    && poetry export -f requirements.txt --output requirements-dev.txt --without-hashes --with dev

FROM base as development
COPY --from=builder /project/requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

USER user
COPY --chown=user:user app ./app/
COPY --chown=user:user main.py .
COPY --chown=user:user tests ./tests/


FROM base as production
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

COPY --from=builder /project/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

USER user
COPY --chown=user:user app ./app/
COPY --chown=user:user main.py .

EXPOSE $PORT
CMD ["python", "main.py"]