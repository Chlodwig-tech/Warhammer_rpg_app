#!/bin/bash
echo "actualising databases..."

echo "python db_create/magic_item_db_create/magic_item_create_db.py"
python db_create/magic_item_db_create/magic_item_create_db.py

echo "python db_create/magic_item_db_create/magic_item_insert_db.py"
python db_create/magic_item_db_create/magic_item_insert_db.py

echo "python db_create/professions_db_create/profession_create_db.py"
python db_create/professions_db_create/profession_create_db.py

echo "python db_create/professions_db_create/profession_insert_db.py"
python db_create/professions_db_create/profession_insert_db.py

echo "python db_create/character_db_create/character_create_db.py"
python db_create/character_db_create/character_create_db.py
