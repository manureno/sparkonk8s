
set PYSPARK_PYTHON=
set PYSPARK_DRIVER_PYTHON=

spark-submit --master k8s://https://c111.eu-de.containers.cloud.ibm.com:31288 ^
    --deploy-mode cluster ^
    --name hello-pyspark ^
    --conf spark.executor.instances=1 ^
    --conf spark.hadoop.fs.s3a.endpoint=%COS_ENDPOINT% ^
    --conf spark.hadoop.fs.s3a.access.key=%COS_ACCESS_KEY% ^
    --conf spark.hadoop.fs.s3a.secret.key=%COS_SECRET_KEY% ^
    --jars local:///opt/hello_pyspark/jars/hadoop-aws-3.2.0.jar,local:///opt/hello_pyspark/jars/aws-java-sdk-bundle-1.11.375.jar ^
    --conf spark.kubernetes.container.image=de.icr.io/ns-am-dh/hello-pyspark:16 ^
    --conf spark.kubernetes.authenticate.driver.serviceAccountName=sa-spark ^
    local:///opt/hello_pyspark/launcher.py
	