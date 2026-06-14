FROM python:3.12-slim-bookworm AS build

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Minimal base image：slim 版本，攻擊面最小
FROM python:3.12-slim-bookworm AS run

WORKDIR /app

COPY --from=build /install /usr/local

COPY src/main/ ./src/main/

ARG USER=devops
ENV HOME=/home/$USER

RUN adduser --disabled-password --gecos "" $USER && \
    chown -R $USER:$USER /app

HEALTHCHECK --interval=30s --timeout=10s --retries=2 --start-period=20s \
    CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

USER $USER

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "src.main.app:app", "--host", "0.0.0.0", "--port", "8000"]
