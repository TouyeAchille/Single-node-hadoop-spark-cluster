# Hadoop Single Node Setup with Docker (HDFS + YARN + Spark + Jupyter)

## Overview

This project sets up a **Hadoop Single Node Cluster inside Docker**, with optional **Spark** and **Jupyter Notebook** support for data processing and analytics.

It is designed for:

* learning Hadoop internals (HDFS, YARN, MapReduce)
* local big data development
* testing data pipelines
* academic and training environments

---

# What is Hadoop Single Node?

A **Hadoop Single Node cluster** is a setup where all Hadoop services run on a single machine.

It simulates a distributed system locally.

## Architecture

```
┌──────────────────────────────┐
│        Single Machine        │
├──────────────────────────────┤
│ NameNode (HDFS Master)       │
│ DataNode (Storage)           │
│ ResourceManager (YARN)       │
│ NodeManager (YARN Worker)    │
│ Secondary NameNode           │
└──────────────────────────────┘
```

---

# How it works

Everything runs:

* on a single OS
* inside a Docker container
* or a single virtual machine

So you can simulate a full Big Data ecosystem locally.

---

# Main Hadoop Components

## 1. HDFS (Hadoop Distributed File System)

HDFS is responsible for **distributed storage**.

### NameNode

* Metadata manager
* Tracks file structure
* Knows where data blocks are stored

###  DataNode

* Stores actual data blocks
* Handles read/write operations

---

## 2. YARN (Yet Another Resource Negotiator)

YARN manages **cluster resources and execution**.

### ResourceManager

* Global scheduler
* Allocates CPU and memory

### NodeManager

* Runs on worker nodes
* Executes and monitors tasks

---

## 3. MapReduce

A distributed computation model.

```
Input Data
   ↓
Mapper
   ↓
Shuffle & Sort
   ↓
Reducer
   ↓
Output
```

---

#  Why use Hadoop Single Node?

##  Learning

* HDFS fundamentals
* YARN scheduling
* MapReduce pipeline

##  Development & Testing

* Python / Java jobs
* ETL pipelines
* Big data workflows

##  Education

* University labs
* Hands-on training
* Data engineering practice

---

#  1. Setup Instructions

## 1. Clone the repository

```bash
git clone https://github.com/TouyeAchille/Single-node-hadoop-cluster.git
cd Single-node-hadoop-cluster
```

---

## 2. Go to Hadoop Docker setup

```bash
cd hadoop/compose/hadoop
```

---

## 3. Build and start the cluster

```bash
docker compose up -d --build
```

---

# 2. Access the container

```bash
docker exec -it single-node-hadoop-spark bash
```

# 2.1 Start spark

```bash

bash  start-all.sh 
```

---



# 3. Dataset preparation

Inside the container:

```bash
cd workspace
gunzip -v datasets/purchases.txt.gz
```

---

# 4. Verify cluster status



```bash
jps
```

Expected output:

* NameNode
* DataNode
* ResourceManager
* NodeManager
* Master
* Worker
* HistoryServer

---

# 5. Run Exercises

Start the practical exercises from the provided TP guide:

* Go to **ESME Moodle for TP Hadoop-Spark**
* Work in **JupyterLab** for experimentation

---

## Activate the virtual environment

```bash
source venv/bin/activate
```

---

## Launch JupyterLab

```bash
jupyter-lab --ip=0.0.0.0 --port=8888 --no-browser
```

---

## Access JupyterLab

Open your browser on the host machine and go to:

[http://localhost:8888](http://localhost:8888)

Then paste the authentication token displayed in the container terminal.






