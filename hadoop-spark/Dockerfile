# -------------------------------------------------------------
# Base Image Arguments
# -------------------------------------------------------------
ARG HADOOP_RUNNER_IMAGE=apache/hadoop
ARG HADOOP_RUNNER_VERSION=3.5.0
FROM ${HADOOP_RUNNER_IMAGE}:${HADOOP_RUNNER_VERSION}


# -------------------------------------------------------------
# Metadata
# -------------------------------------------------------------
LABEL maintainer="Mbogol Touye Achille" \
    email="touyejunior@gmail.com" \
    version="0.1.0" \
    description="Single-node-hadoop-cluster"



WORKDIR /opt/hadoop


COPY ../../ /opt/hadoop


USER root

# -------------------------------------------------------------
# System Dependencies Installation
# -------------------------------------------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    vim \
    curl \
    net-tools \
    iputils-ping \
    python3 \
    python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# -------------------------------------------------------------
# Python Environment Setup
# -------------------------------------------------------------    

RUN python3 -m venv ./workspace/venv
ENV VENV_PATH=./workspace/venv/bin

RUN ${VENV_PATH}/pip install --no-cache-dir --upgrade pip

RUN ${VENV_PATH}/pip install --no-cache-dir \
    jupyterlab \
    pyspark==4.1.1 \
    findspark \
    ipykernel 

RUN ${VENV_PATH}/python -m ipykernel install --name=venv --display-name "Python3 (venv)"

# -------------------------------------------------------------
# Datanode & NameNode Directories
# -------------------------------------------------------------    
RUN mkdir -p /opt/hadoop/data/namenode \
             /opt/hadoop/data/datanode \
             /opt/hadoop/logs    
             
             
# -------------------------------------------------------------
# Download Spark distribution
# -------------------------------------------------------------
ARG SPARK_VERSION=4.1.1
ENV SPARK_VERSION=${SPARK_VERSION}
RUN wget https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz && \
    tar -xzf spark-${SPARK_VERSION}-bin-hadoop3.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop3 /opt/spark && \
    rm spark-${SPARK_VERSION}-bin-hadoop3.tgz 

ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

RUN  mkdir -p /opt/spark/logs 

RUN chmod +x /opt/hadoop/start-all.sh \
    && chmod +x /opt/hadoop/start-hadoop.sh \
    && chmod +x /opt/hadoop/spark_conf/spark_init.sh

COPY spark_conf /opt/spark/conf/ 

 
# -------------------------------------------------------------
# Permissions Setup
# -------------------------------------------------------------
RUN chown -R hadoop:users /opt/hadoop /opt/spark

USER hadoop





