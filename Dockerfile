FROM python:3.7

RUN pip install fastapi[all]

EXPOSE 80

COPY . /app

CMD ["uvicorn", "app.application:app", "--host", "0.0.0.0", "--port", "80"]