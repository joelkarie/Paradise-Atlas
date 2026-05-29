#!/bin/bash

echo "Reseting db atlas_paradiso"
dropdb atlas_paradiso
createdb atlas_paradiso
psql -d atlas_paradiso -f 001_initial_schema.sql     
psql -d atlas_paradiso -f 002_add_types.sql
psql -d atlas_paradiso -f 003_import_paradise_voyage.sql
