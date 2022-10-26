FROM python:3.10-alpine

COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip\
 && pip install --no-cache-dir -r ./src/requirements.txt

CMD ["python3", "auto_test.py"]
