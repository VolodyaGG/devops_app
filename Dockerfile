FROM python:3.12-slim@sha256:3d5ed973e45820f5ba5e46bd065bd88b3a504ff0724d85980dcd05eab361fcf4 as base

ENV POETRY_VERSION=2.3.2 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=true \
    PORT=8000

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

WORKDIR /project

RUN adduser --disabled-password --gecos "" user

COPY --chown=user:user pyproject.toml poetry.lock ./


FROM base as development

RUN poetry install --no-root

USER user

COPY --chown=user:user app ./app/
COPY --chown=user:user main.py /project/
COPY --chown=user:user tests ./tests/


FROM base as production

RUN poetry install --no-root --only main

USER user

COPY --chown=user:user app ./app/
COPY --chown=user:user main.py /project/

EXPOSE $PORT

CMD ["python", "main.py"]