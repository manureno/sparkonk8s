
## Create a PySpark Docker Image

### Pre-Requisite
You've completed the [Create a Docker image containing Spark Samples](../2_create_sparksample_image/README.md) chapter.

### PySpark Docker Image Creation Steps
1. [Build the PySpark Docker image](#build-pyspark-docker-image)
2. [Push the Image to a Container Registry Namespace](#push-image-to-a-container-registry-namespace)

### Build PySpark Docker Image

* Build the PySpark Docker image
  + -t pyspark-3.1.3 : the tag given to the new image
  + -f %SPARK_HOME%\kubernetes\dockerfiles\spark\bindings\python\Dockerfile : the PySpark Docker file
  + --build-arg base_img=spark-3.1.3 : the base image to use (it relies on the spark-3.1.3 image built in previous section)
  + %SPARK_HOME% : Context used to build the image 
```
>docker build -t pyspark-3.1.3 -f %SPARK_HOME%\kubernetes\dockerfiles\spark\bindings\python\Dockerfile --build-arg base_img=spark-3.1.3 %SPARK_HOME%
```

* Run an interactive container to inspect the new image
```
>docker run -it pyspark-3.1.3 bash

$ python3 --version
Python 3.9.2
$java -version
openjdk version "11.0.14.1" 2022-02-08
OpenJDK Runtime Environment 18.9 (build 11.0.14.1+1)
OpenJDK 64-Bit Server VM 18.9 (build 11.0.14.1+1, mixed mode, sharing)
$ ls -l $SPARK_HOME
total 48
-rw-r--r-- 1 root root     0 Mar 14 11:23 RELEASE
drwxr-xr-x 2 root root  4096 Mar 17 14:34 bin
drwxr-xr-x 5 root root  4096 Mar 17 14:34 data
drwxr-xr-x 1 root root  4096 Mar 17 14:34 examples
drwxr-xr-x 2 root root 20480 Mar 17 14:34 jars
drwxr-xr-x 1 root root  4096 Mar 18 13:51 python
drwxr-xr-x 2 root root  4096 Mar 17 14:34 sbin
drwxr-xr-x 2 root root  4096 Mar 17 14:34 tests
drwxrwxr-x 1 root root  4096 Mar 14 11:23 work-dir
$ ls -l $SPARK_HOME/python/pyspark
[...]
exit
```

### Push Image to a Container Registry Namespace

* Connect to IBM Cloud and check the available namespaces
```
ibmcloud login
ibmcloud cr namespace-list -v
```
* Tag the Spark image to allow its deployment in one of the IBM Container Registry Namespaces
```
docker tag pyspark-3.1.3 de.icr.io/CR-NAMESPACE/pyspark-3.1.3
```
* Check that the image tagged de.icr.io/CR-NAMESPACE/pyspark-3.1.3 appears in your local repository
```
docker images
```
* If not already done, log local docker daemon to IBM Cloud Container Registry
```
ibmcloud cr login -client docker
```
* Push the image to the namespace
```
docker push de.icr.io/CR-NAMESPACE/pyspark-3.1.3
```
* Check the image is in the namespace
```
ibmcloud cr image-list
```

### Congratulations !

Let's summarize your achievements :

- [x] You've built a Docker image containing PySpark 
- [x] You've inspected it with a Docker interactive session
- [x] This image has been pushed to an IBM Cloud CR Namespace