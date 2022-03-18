## Build and Run a Hello Spark Python Workload

### Pre-Requisite
You've completed the [Create a PySpark Docker Image](../4_create_pyspark_image/README.md) chapter.   
Python is installed and on your PATH.
An IBM Cloud Container Registry Namespace, named _CS-NAMESPACE_ in this document, has been created.

### Run HelloSpark Steps
1. [Create a "Hello PySpark" wheel package](#create-a-hello-pyspark-wheel-package)
2. [Publish a "Hello PySpark" Docker image](#publish-a-hello-pyspark-docker-image)
3. [Run a container out of the image](#run-a-container-out-of-the-image)

### Create a "Hello PySpark" wheel package

* Create & activate a virtual env, upgrade pip and install modules required by the project and the packaging process
```
>python -m venv venv
[...]
>.\venv\Scripts\activate
(venv) >python -m pip install --upgrade pip
[...]
(venv) >pip install -r requirements\package.requirements.txt
[...]
(venv) >pip install -r requirements\development.requirements.txt
``` 

* Build the Python package
```
(venv) >python setup.py bdist_wheel --universal
```

* The package should have been created under the dist folder : 
```
> dir dist
[...]
03/18/2022  04:26 PM             1,051 hello_pyspark-1.0-py2.py3-none-any.whl
[...]          
```

### Publish a "Hello PySpark" Docker image

* Build the docker image
```
docker build -t hello-pyspark -f Dockerfile .
```

* Tag the image for publishing
```
docker tag hello-pyspark de.icr.io/CS-NAMESPACE/hello-pyspark .
```

* Log in to IBM Cloud
```
ibmcloud login
```

* Link local docker and remote Container Registry
```
ibmcloud cr login -client docker
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

* Submit the spark job :
  + --master k8s://https://c111.eu-de.containers.cloud.ibm.com:30249 : Spark will use Kubernetes as resource manager, the URL contains the control plane of the previous step.   
  + --deploy-mode cluster : The spark driver will run as a pod in the cluster
  + --conf spark.executor.instances=3 : 3 executors will run each as a Pod in the cluster
  + --conf spark.kubernetes.container.image=de.icr.io/ns-am-dh/spark-3.1.3 : the image to pull out of the CR
  + --conf spark.kubernetes.authenticate.driver.serviceAccountName=sa-spark : service account under which the Pods will run
  + local:///opt/hello_pyspark/launcher.py : the python script to be executed
```
spark-submit --master k8s://https://c111.eu-de.containers.cloud.ibm.com:30249 ^
    --deploy-mode cluster ^
    --name hello-pyspark ^
    --conf spark.executor.instances=3 ^
    --conf spark.kubernetes.container.image=de.icr.io/ns-am-dh/hello-pyspark ^
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
- [x] You've done a lot of stuff