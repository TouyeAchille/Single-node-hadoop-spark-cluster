#!/bin/bash
set -e

echo "Stopping HDFS daemons..."
hdfs --daemon stop namenode || true
hdfs --daemon stop datanode || true

echo "Stopping YARN daemons..."
yarn --daemon stop resourcemanager || true
yarn --daemon stop nodemanager || true

sleep 2

echo -e "\nRemaining Java processes:"
jps