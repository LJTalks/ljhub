# Run this script with ./backup_db.sh to back up the entire database (schema and data)
#!/bin/bash

# Database connection details
HOST="ep-gentle-mountain-a23bxz6h-pooler.eu-central-1.aws.neon.tech"
PORT="5432"
USER="u8phdpprpgk"
DATABASE="taco_scoop_bless_2747"
BACKUP_FILE="/workspace/backup_$(date +'%Y%m%d_%H%M%S').dump"  # Save directly to root

# Prompt for database password if not already set
if [ -z "$PGPASSWORD" ]; then
    read -sp "Enter database password: " PGPASSWORD
    echo
fi

# Run pg_dump to back up the entire database, including schema and data
docker run --rm -v "/workspace":/workspace -e PGPASSWORD="$PGPASSWORD" postgres:15 \
    pg_dump -h "$HOST" -p "$PORT" -U "$USER" -d "$DATABASE" -F c -b -v -f "$BACKUP_FILE"

echo "Backup completed: $BACKUP_FILE"
