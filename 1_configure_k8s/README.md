## Configure a Kubernetes Cluster for Spark usage

### Pre-Requisite
* A Kubernetes cluster, named _K8S-CLUSTER_ in this document, has been created on IBM Cloud
* A Container Registry Namespace, called _CR-NAMESPACE_ in this document, has been created on IBM Cloud
* ibmcloud CLI is installed on your workstation
* Docker is installed on your workstation

### Configuration Steps

1. [Connect Local Docker to IBM Cloud Cluster](#connect-local-docker-to-ibm-cloud-cluster)
2. [Create a service account on the IBM Cloud Cluster](#create-a-service-account-on-the-ibm-cloud-cluster)


### Connect Local Docker to IBM Cloud Cluster
These steps allow to connect your local environment to the IBM Cloud.  
This is useful to deploy Docker images to the IBM Container Registry Namespace and to use local kubectl CLI to interact with the IBM Cloud cluster.

* Log in to IBM Cloud
```
$ ibmcloud login
```
* Check available namespaces 
```
$ ibmcloud cr namespace-list -v
```
* Log local docker daemon to IBM Cloud Container Registry
```
$ ibmcloud cr login -client docker
```
* Connect local docker daemon to IBM Cloud cluster
```
$ ibmcloud ks cluster config --cluster K8S-CLUSTER
```

### Create a service account on the IBM Cloud Cluster
These steps allow to create a service account named "sa-spark" which will be used by spark containers.  
This service account need to be allowed to pull images from the CR Namespace

* Create a _sa-spark_ service account 
```
$ kubectl create serviceaccount sa-spark
```
* List all service acccounts to check the proper creation of _sa-spark_
```
$ kubectl get serviceaccounts
```
* List the details of the _sa-spark_ service account 
```
$ kubectl get serviceaccounts/sa-spark -o yaml
```
* Create a ClusterRoleBinding object and grant this role to _sa-spark_ service account
```
$ kubectl create clusterrolebinding spark-role --clusterrole=edit --serviceaccount=default:sa-spark --namespace=default
```
* Give to _sa-spark_ service account the secret allowing to pull images from the Cnotainer Registry Namespaces   

The Linux way:
```
$ kubectl patch -n default serviceaccount/sa-spark -p '{"imagePullSecrets":[{"name": "all-icr-io"}]}'
```
The Windows way:

```
kubectl patch serviceaccounts/sa-spark -p "{\"imagePullSecrets\": [{\"name\": \"all-icr-io\"}]}"
```
* List the details of the _sa-spark_ service account in order to check it now knows the secret
```
$ kubectl get serviceaccounts/sa-spark -o yaml
``` 

### Congratulations !
Let's summarize your achievements :

- [x] Your local Docker environment is now connected to IBM Cloud Container Registry and to a Kubernetes cluster  
- [x] This cluster contains an  _sa-spark_ service account as well as a role binding that will be needed to run spark workloads.