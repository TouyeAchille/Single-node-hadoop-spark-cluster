#!/bin/bash

echo -e "Stop NameNode daemon and DataNode daemon\n"

$HADOOP_HOME/sbin/stop-dfs.sh

echo -e "Stop ResourceManager daemon and NodeManager daemon\n"

$HADOOP_HOME/sbin/stop-yarn.sh

echo -e "\n"

echo -e "Hadoop services stopped. Current JVM processes:\n"

jps