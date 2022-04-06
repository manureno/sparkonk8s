# Spark On Kubernetes

This project is a step-by-step guide to get a Spark workload running on an IBM Cloud Kubernetes cluster.   
It is inspired by the official Spark documentation : https://spark.apache.org/docs/latest/running-on-kubernetes.html

**Pre Requisite**  
A Kubernetes Cluster and a Container Registry Namespace have been provisioned on IBM Cloud.   
See dedicated project for more information about provisioning these elements : https://github.com/manureno/infra-ibm.tf

**Steps**  
1. [Configure Kubernetes Cluster for Spark usage](1_configure_k8s/README.md)
2. Run a "Compute PI" Spark Sample on Kubernetes    
   1. [Create a Docker image with Spark Samples](2_create_sparksample_image/README.md)
   2. [Create a Container and run a Spark Sample](3_create_container_and_run/README.md)
3. Run a PySpark Workload
   1. [Create a PySpark Docker Image](4_create_pyspark_image/README.md)
   2. [Create and run a "Hello PySpark" workload](5_hello_pyspark/README.md)

**Cheat Sheet**   
- [Connect Local Docker to IBM Cloud Cluster](0_cheat_sheets/connect_local_docker_to_cloud_k8s.md)
- [Miscellaneous helpers](0_cheat_sheets/miscellaneous.md)


