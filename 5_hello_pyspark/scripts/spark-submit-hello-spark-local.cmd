@rem
@rem spark submit looks for "   python3" executable which is not available on Windows
@rem Override this default behavior with PYSPARK_PYTHON and PYSPARK_DRIVER_PYTHON environment variables
@rem
set PYSPARK_PYTHON=python.exe
set PYSPARK_DRIVER_PYTHON=python.exe

spark-submit --conf spark.hadoop.fs.s3a.endpoint=%COS_ENDPOINT% --conf spark.hadoop.fs.s3a.access.key=%COS_ACCESS_KEY% --conf spark.hadoop.fs.s3a.secret.key=%COS_SECRET_KEY% --jars ..\jars\hadoop-aws-3.2.0.jar,..\jars\aws-java-sdk-bundle-1.11.375.jar ..\src\launcher.py -b %COS_BUCKET%