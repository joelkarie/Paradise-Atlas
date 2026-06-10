#!/bin/bash
# python3 get_flat_files.py
DOWNLOAD=false

while getopts "d" opt; do
  case $opt in
    d)
      DOWNLOAD=true
      ;;
    *)
      echo "Usage: $0 [-d]"
      exit 1
      ;;
  esac
done

if [ "$DOWNLOAD" = true ]; then
  echo "Downloading latest flat files..."
  python3 get_flat_files.py
fi

echo "\nReseting db atlas_paradiso\n"
dropdb atlas_paradiso
createdb atlas_paradiso
psql -d atlas_paradiso -f 001_initial_schema.sql     
psql -d atlas_paradiso -f 002_add_types.sql
psql -d atlas_paradiso -f 003_import_paradise_voyage.sql
psql -d atlas_paradiso -f 004_create_views.sql