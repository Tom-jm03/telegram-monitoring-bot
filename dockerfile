FROM python:3.10.6-slim-bullseye
WORKDIR /server-stats-telegram
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "main.py"]
