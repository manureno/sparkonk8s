### Connect Local Docker to IBM Cloud Cluster
These steps allow to connect your local Docker environment to an IBM Cloud Container Registry and Kubernetes cluster.  
This is useful to deploy Docker images to the IBM Container Registry Namespace and to use local kubectl CLI to interact with the IBM Cloud cluster.

* Log in to IBM Cloud
```
ibmcloud login
```
* Check available Container Registry namespaces 
```
ibmcloud cr namespace-list -v
```
* Start Docker Desktop   
```
"C:\Program Files\Docker\Docker\Docker Desktop.exe"
```
* Log local docker daemon to IBM Cloud Container Registry
```
ibmcloud cr login -client docker
```
* Check available Kubernetes clusters
```
ibmcloud ks cluster ls
```
* Retrieve IBM Cloud cluster configuration    
```
ibmcloud ks cluster config --cluster K8S-CLUSTER
```
