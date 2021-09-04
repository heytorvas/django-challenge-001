FROM python:3.9
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/medium
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000