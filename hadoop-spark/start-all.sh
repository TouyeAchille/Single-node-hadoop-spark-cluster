#!/bin/bash

set -e

echo "Running Spark init..."
/opt/hadoop/spark_conf/spark_init.sh

echo "Starting Spark Master..."
/opt/spark/sbin/start-master.sh

echo "Starting Spark Worker..."
/opt/spark/sbin/start-worker.sh spark://single-node-hadoop:7077

echo "Starting History Server..."
/opt/spark/sbin/start-history-server.sh


echo "Cluster ready."

echo "----------------------------------------"
echo "Running jps to verify Spark processes..."
echo "----------------------------------------"
jps