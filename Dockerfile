FROM python:3.7

EXPOSE 9876

COPY . /app

WORKDIR /app

RUN pip install -v -r requirements.txt

CMD ["uvicorn", "application:app", "--host", "0.0.0.0", "--port", "9876"]