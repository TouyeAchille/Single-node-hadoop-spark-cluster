# Hadoop Single Node Installation Setup with Docker

This project sets up a Hadoop environment in a Docker container. It also includes a Spark and Jupyter Notebook installation for data processing and analysis. Follow the instructions below to build and run the Hadoop cluster in a single-node Docker container.

his Single node Hadoop installation can help to perform simple operations using Hadoop MapReduce and the Hadoop Distributed File System (HDFS).

## 1. Build Image and Create Hadoop Container
To start, build the Docker image and create the Hadoop container using Docker Compose.

mv compose/hadoop/hadoop

> docker compose up -d build

 2. Open a New Terminal and Access the Container
Once the container is up and running, execute the following command to access the container's shell:
 
> docker exec -it single-node-hadoop bash


4. Unzip Dataset for Practical Work
For the practical exercises, you will need to unzip the provided dataset file. Use the following command to unzip purchases.txt.gz:

> gunzip dataset/purchases.txt.gz

5 🛠️ Check if mapreduce job run well, use the following command
> ./scripts/run_wordcount.sh

