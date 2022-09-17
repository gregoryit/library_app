FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3.10 python3.10-dev
RUN apt install -y python3-pip
COPY . .
RUN pip install -r requirements.txt
CMD ["python3", "./main.py"]
