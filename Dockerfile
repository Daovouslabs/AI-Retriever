
FROM python:3.10 as requirements-stage

WORKDIR /tmp

RUN pip install poetry -i https://pypi.mirrors.ustc.edu.cn/simple/

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10

WORKDIR /app

COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r /app/requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/

COPY . /app/

# Heroku uses PORT, Azure App Services uses WEBSITES_PORT, Fly.io uses 8080 by default
CMD ["sh", "-c", "uvicorn server.main:app --host 0.0.0.0 --port ${PORT:-${WEBSITES_PORT:-8080}}"]
