#!/bin/bash

set -e

echo "[Spark Init] Creating HDFS directories..."

hdfs dfs -mkdir -p /spark/logs

hdfs dfs -chmod -R 777 /spark

echo "[Spark Init] Done."