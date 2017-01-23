#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DATA_DIR=$1
DB=$2

python3 $DIR/src/create_sqlite.py --input $DATA_DIR/entities.json  --name $DB --tablename entities
python3 $DIR/src/create_sqlite.py --input $DATA_DIR/events.json    --name $DB --tablename events
python3 $DIR/src/create_sqlite.py --input $DATA_DIR/sources.json   --name $DB --tablename sources
python3 $DIR/src/create_sqlite.py --input $DATA_DIR/topics.json    --name $DB --tablename topics
python3 $DIR/src/create_queries_table.py --name $DB