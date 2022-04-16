#!/usr/bin/env sh

set -e

echo "Starting up Api server of ${PROJECT_NAME} project in $PROJECT_ENV environment"

echo "Waiting for Postgres"
./wait-for-it.sh \
    --host=${POSTGRES_HOST} \
    --port=${POSTGRES_PORT} \
    --timeout=15 \
    -- echo "Postgres is up"

echo "Applying migrations"
alembic upgrade head

echo "API prepareing completed"
exit 0
