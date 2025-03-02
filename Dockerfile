FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y postgresql-client

RUN chmod +x wait_for_db.sh

CMD ["./wait_for_db.sh"]
