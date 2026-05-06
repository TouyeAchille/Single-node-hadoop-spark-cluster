# Single-node-hadoop-cluster
A **Hadoop single-node cluster** is the simplest way to run Hadoop, where all its core components run on one machine instead of being distributed across multiple servers. it’s a **mini Hadoop cluster** running on one computer, mainly for practice or experimentation.

In a typical Hadoop setup, you have:

* **NameNode** → manages metadata (file system structure, file locations)
* **DataNode** → stores the actual data blocks
* Other services like **ResourceManager** and **NodeManager** (for processing)

In a **single-node cluster**, all of these run on the same system. That means:

* The **NameNode and DataNode are on the same machine**
* Hadoop behaves like a distributed system, but without actual distribution

### Why use it?

* Learning and testing Hadoop
* Development and debugging
* Running small workloads without needing multiple machines

### Limitations

* No fault tolerance (if the machine fails, everything is lost)
* Not scalable
* Not suitable for production use


