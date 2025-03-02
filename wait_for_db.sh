#!/bin/bash

until pg_isready -h ${DB_HOST} -p ${DB_PORT} -U ${DB_USER}; do
  echo "Waiting for database to be ready..."
  sleep 2
done

alembic upgrade head
uvicorn main:app --host 0.0.0.0 --port 8000
