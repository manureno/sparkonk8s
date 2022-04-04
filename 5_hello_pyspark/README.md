## Build and Run a Hello Spark Python Workload
In this chapter we'll go through the steps required to build, package and run a simple "Hello PySpark" application, 
which basically create and print a Spark Dataframe, in a Kubernetes environment.
.

Project Content :
```
5_hello_pyspark
  +- requirements : Pyhon dependencies
  +- src          : Code of the application
  +- Dockerfile   : Instructions to create a Docker Image including PySpark and the application 
  +- setup.py     : Instructions to create a Python wheel package
```


### Pre-Requisite
* Docker is installed on your workstation
* ibmcloud CLI is installed on your workstation
* Your local Docker environment is connected to IBM Cloud Kubernetes : [initialisation procedure](../0_cheat_sheets/connect_local_docker_to_cloud_k8s.md)
* You've completed the [Create a PySpark Docker Image](../4_create_pyspark_image/README.md) chapter.   
* Python is installed and on your PATH.   
* An IBM Cloud Container Registry Namespace, named _CR-NAMESPACE_ in this document, have been created.

### Run HelloSpark Steps
1. [Create a "Hello PySpark" wheel package](#create-a-hello-pyspark-wheel-package)
2. [Publish a "Hello PySpark" Docker image](#publish-a-hello-pyspark-docker-image)
3. [Run a container out of the image](#run-a-container-out-of-the-image)

### Create a "Hello PySpark" wheel package

* Create & activate a virtual env, upgrade pip and install modules required by the project and the packaging process
```
python -m venv venv
```
```
.\venv\Scripts\activate
```
```
python -m pip install --upgrade pip
```
```
pip install -r requirements\package.requirements.txt
```
```
pip install -r requirements\development.requirements.txt
``` 

* Build the Python package
```
python setup.py bdist_wheel --universal
```

* The package should have been created under the dist folder : 
```
dir dist
```
```
03/18/2022  04:26 PM             1,051 hello_pyspark-1.0-py2.py3-none-any.whl
```

### Publish a "Hello PySpark" Docker image

* Build the docker image
```
docker build -t hello-pyspark -f Dockerfile .
```

* Tag the image for publishing
```
docker tag hello-pyspark de.icr.io/CR-NAMESPACE/hello-pyspark
```

* Publish the image
```
docker push de.icr.io/CR-NAMESPACE/hello-pyspark
```

* Check the image is available in the namespace 
```
ibmcloud cr image-list
```

### Run a container out of the image
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
  + --conf spark.kubernetes.container.image=de.icr.io/CR-NAMESPACE/spark-3.1.3 : the image to pull out of the CR
  + --conf spark.kubernetes.authenticate.driver.serviceAccountName=sa-spark : service account under which the Pods will run
  + local:///opt/hello_pyspark/launcher.py : the python script to be executed
```
spark-submit --master k8s://https://CONTROL-PLANE-HOST:CP-PORT ^
    --deploy-mode cluster ^
    --name hello-pyspark ^
    --conf spark.executor.instances=3 ^
    --conf spark.kubernetes.container.image=de.icr.io/CR-NAMESPACE/hello-pyspark ^
    --conf spark.kubernetes.authenticate.driver.serviceAccountName=sa-spark ^
    local:///opt/hello_pyspark/launcher.py
```  
* List the pods to find the driver named hello-pyspark-*-driver
```
kubectl get pods
```

* Retrieve the standard output of the driver Pod where you should read the Spark Dataframe containing the welcome messages 
```
kubectl logs -f hello-pyspark-5b742d7f9e2bbaf5-driver
```
```
[...]
+-----+----------+-------------------+
|  say|        to|               when|
+-----+----------+-------------------+
|Hello|     World|2000-01-01 12:00:00|
|Hello|   PySpark|2000-01-02 12:00:00|
|Hello| IBM Cloud|2000-01-03 12:00:00|
|Hello|Kubernetes|2000-01-04 12:00:00|
+-----+----------+-------------------+
[...]
```

### Congratulations !
Let's summarize your achievements: 
- [x] You've created a wheel package for a PySpark Application
- [x] Created a Docker image includin the PySpark application
- [x] Run a PySpark container in Kubernetes for this application