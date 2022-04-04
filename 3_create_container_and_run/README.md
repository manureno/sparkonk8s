## Create a Container and Run Spark Samples
### Pre-Requisites
* Docker is installed on your workstation
* ibmcloud CLI is installed on your workstation
* Your local Docker environment is connected to IBM Cloud Kubernetes : [initialisation procedure](../0_cheat_sheets/connect_local_docker_to_cloud_k8s.md)
* A Container Registry Namespace, called _CR-NAMESPACE_ in this document, has been created on IBM Cloud
* A Kubernetes cluster, named _K8S-CLUSTER_ in this document, has been created on IBM Cloud
* A Spark Docker image has been pushed to the _CR-NAMESPACE_
* A Service account named _sa-spark_ and an associated role binding have been added to _K8S-CLUSTER_ 

### Container Creation and Execution Steps
* Check the available images
```
ibmcloud cr image-list
```

* Show Kubernetes cluster information : the "control plane" URL will be used to submit the Spark job
```
kubectl cluster-info
```
```
Kubernetes control plane is running at https://CONTROL-PLANE-HOST:CP-PORT
CoreDNS is running at https://CONTROL-PLANE-HOST:CP-PORT/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
kubernetes-dashboard is running at https://CONTROL-PLANE-HOST:CP-PORT/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy
Metrics-server is running at https://CONTROL-PLANE-HOST:CP-PORT/api/v1/namespaces/kube-system/services/https:metrics-server:/proxy
NodeLocalDNS is running at https://CONTROL-PLANE-HOST:CP-PORT/api/v1/namespaces/kube-system/services/node-local-dns:dns/proxy
```

* Submit the spark job :
  + --master k8s://https://CONTROL-PLANE-HOST:CP-PORT : Spark will use Kubernetes as resource manager, the URL contains the control plane of the previous step.   
  + --deploy-mode cluster : The spark driver will run as a pod in the cluster
  + --conf spark.executor.instances=3 : 3 executors will run each as a Pod in the cluster
  + --conf spark.kubernetes.container.image=de.icr.io/ns-am-dh/spark-3.1.3 : the image to pull out of the CR
  + --conf spark.kubernetes.authenticate.driver.serviceAccountName=sa-spark : service account under which the Pods will run
  + local:///opt/spark/examples/jars/spark-examples_2.12-3.1.3.jar : the location of jars inside the container
```
spark-submit --master k8s://https://CONTROL-PLANE-HOST:CP-PORT ^
    --deploy-mode cluster ^
    --name spark-pi ^
    --class org.apache.spark.examples.SparkPi ^
    --conf spark.executor.instances=3 ^
    --conf spark.kubernetes.container.image=de.icr.io/ns-am-dh/spark-3.1.3 ^
    --conf spark.kubernetes.authenticate.driver.serviceAccountName=sa-spark ^
    local:///opt/spark/examples/jars/spark-examples_2.12-3.1.3.jar
```  
* After execution, the Spark Driver Pod named  "spark-pi-*-driver" remains accessible. You can list the pods to find the spark driver one :
```  
kubectl get pods
```  
* You can now use the driver pod name to show the output of the job where you should find a rough estimation of PI
```
kubectl logs -f spark-pi-ab44757f98cc928b-driver
```
### Congratulations !
Let's summarize your achievements: 
- [x] You've queried Kubernetes cluster informations
- [x] You've submitted a Spark job using a Kubernetes resource manager
- [x] You know how to list pods and query their output
- [x] And most of all you know now that PI is around 3.14 ;-)
