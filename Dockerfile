FROM python:3.9-slim

COPY ./src /app/src

WORKDIR /app

RUN pip install fastapi redis pandas uvicorn docker

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--reload"]