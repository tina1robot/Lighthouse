#!/bin/bash
#bash back up

#!/bin/bash

# Directory where logs are stored
LOG_DIR="/OneDrive/Desktop/P3 lhls/log_file.txt"
# Directory where backups will be stored
BACKUP_DIR="/OneDrive/Desktop/P3 lhls"
# Current date for backup naming
DATE=$(date +"%Y-%m-%d")

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Backup the logs
tar -czf "$BACKUP_DIR/logs_backup_$DATE.tar.gz" "$LOG_DIR"

# Read logs and save to a single file for Python script
cat "$LOG_DIR"/* > "$BACKUP_DIR/combined_logs_$DATE.txt"

echo "Logs have been backed up and combined into $BACKUP_DIR/combined_logs_$DATE.txt"
