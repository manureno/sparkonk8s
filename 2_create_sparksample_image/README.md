## Create a Docker image containing Spark Samples

### Pre-Requisite
* Docker is installed on your workstation
* ibmcloud CLI is installed on your workstation
* Your local Docker environment is connected to IBM Cloud Kubernetes : [initialisation procedure](../0_cheat_sheets/connect_local_docker_to_cloud_k8s.md)
* A Container Registry Namespace, called _CR-NAMESPACE_ in this document, has been created on IBM Cloud
* A Kubernetes cluster, named _K8S-CLUSTER_ in this document, has been created on IBM Cloud

### Spark Docker Image Creation Steps
1. [Install Spark on Windows](#install-spark-on-windows)
2. [Build the Spark Docker image](#build-spark-docker-image)
3. [Push the Image to a Container Registry Namespace](#push-docker-image-to-a-container-registry-namespace)

### Install Spark on Windows
* At the time of writing this document, Spark 3.2.1 is the latest but has an issue on Windows, Spark 3.1.3 will thus be used
* Download spark 3.1.3 from https://spark.apache.org/downloads.html
* Unzip in a location without space in the path (C:\Applications\spark\spark-3.1.3-bin-hadoop3.2 in this document)
* Create spark-related environment variables and update PATH (example below for Windows)
```
set HADOOP_HOME=C:\Applications\spark\spark-3.1.3-bin-hadoop3.2
set SPARK_HOME=C:\Applications\spark\spark-3.1.3-bin-hadoop3.2
set PATH=%SPARK_HOME%\bin;%PATH%
```
* Download winutils.exe from https://github.com/steveloughran/winutils
* Copy winutils.exe in a folder declared in the PATH (ex : under %SPARK_HOME%\bin)
* Install Java 8 and set environment variables
```
set JAVA_HOME=C:\Applications\Java\jdk1.8.0_181
set PATH=%JAVA_HOME%\bin;%PATH%
```
* Start a spark shell to check install is successful
```
spark-shell
```   
```
22/03/17 15:20:53 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Spark context Web UI available at http://xxxxx:4040
Spark context available as 'sc' (master = local[*], app id = local-1647526878117).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.1.3
      /_/

Using Scala version 2.12.10 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_181)
Type in expressions to have them evaluated.
Type :help for more information.
scala>
```

### Build Spark Docker Image
Spark comes with Docker files under %SPARK_HOME%\kubernetes\dockerfiles\spark  
We will build an image from one of these Docker files :
* Build the image
```
docker build -t spark-3.1.3 -f %SPARK_HOME%\kubernetes\dockerfiles\spark\Dockerfile %SPARK_HOME%
```

* Check that the image tagged spark-3.1.3 appears in your local repository
```
docker images
```

### Push Docker Image to a Container Registry Namespace

* Check the available namespaces
```
ibmcloud cr namespace-list -v
```
* Tag the Spark image to allow its deployment in one of the IBM Container Registry Namespaces
```
docker tag spark-3.1.3 de.icr.io/CR-NAMESPACE/spark-3.1.3
```
* Check that the image tagged de.icr.io/CR-NAMESPACE/spark-3.1.3 appears in your local repository
```
docker images
```
* Push the image to the namespace
```
docker push de.icr.io/CR-NAMESPACE/spark-3.1.3
```
* Check the image is in the namespace
```
ibmcloud cr image-list
```

### Congratulations !

Let's summarize your achievements :

- [x] You've installed Spark
- [x] You've built a Docker image containing Spark 
- [x] This image has been pushed to an IBM Cloud CR Namespace