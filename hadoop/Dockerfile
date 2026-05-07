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
# Datanode & NameNode Directories
# -------------------------------------------------------------    
RUN mkdir -p /opt/hadoop/data/namenode \
             /opt/hadoop/data/datanode \
             /opt/hadoop/logs


# -------------------------------------------------------------
# Permissions Setup
# -------------------------------------------------------------
RUN chown -R hadoop:users /opt/hadoop

USER hadoop





