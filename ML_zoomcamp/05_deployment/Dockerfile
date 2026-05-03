FROM python:3.14.4

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --system --deploy

COPY ["predict.py", "./"]
COPY ["model/model_C=1.0.bin", "./model/"]

EXPOSE 2909

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:2909", "predict:app"]
