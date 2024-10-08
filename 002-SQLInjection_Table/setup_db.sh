#!/bin/bash

sudo apt-get install sqlite3
# Crear base de datos SQLite y tabla
sqlite3 DB_Lab002.db <<EOF
CREATE TABLE flag (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    value TEXT NOT NULL
);
INSERT INTO flag (value) VALUES ('fPqUzum4ky');
EOF

echo "Base de datos y tabla creadas con éxito."
