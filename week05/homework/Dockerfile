FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system

COPY ["app.py", "./"]

EXPOSE 8080

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
