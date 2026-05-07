#!/usr/bin/env bash
set -euo pipefail

echo "----------------------------------------"
echo "Starting Hadoop cluster..."
echo "----------------------------------------"

# INIT HDFS ONLY IF NEEDED
if [ ! -d "/opt/hadoop/data/namenode/current" ]; then
  echo "Formatting HDFS..."
  hdfs namenode -format -force
fi

echo "Starting HDFS services..."

hdfs namenode &
NAMENODE_PID=$!

hdfs datanode &
DATANODE_PID=$!

echo "Starting YARN services..."

yarn resourcemanager &
RM_PID=$!

yarn nodemanager &
NM_PID=$!

echo "All services started."

jps

# Monitor processes 
wait $NAMENODE_PID $DATANODE_PID $RM_PID $NM_PID