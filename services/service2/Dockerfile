FROM python:3.9

WORKDIR /tmp

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

WORKDIR /app

COPY src/ .

EXPOSE 80

ENTRYPOINT ["python", "app.py"]