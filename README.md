# Spark On Kubernetes

This project is a step-by-step guide to get a PySpark workload running on an IBM Cloud Kubernes cluster.

**Pre Requisite**  
A Kubernetes Cluster and a Container Registry Namespace have been provisioned on IBM Cloud.   
See dedicated project for more information about provisioning these elements : https://github.com/manureno/infra-ibm.tf

**Steps**  
1. [Configure Kubernetes Cluster for Spark usage](1_configure_k8s/README.md)
2. [Create a Docker image with Spark Samples](2_create_sparksample_image/README.md) 
3. [Create a Container and run a Spark Sample](3_create_container_and_run/README.md)
   
