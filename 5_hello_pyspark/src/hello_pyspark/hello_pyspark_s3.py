from pyspark import SparkConf
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from datetime import datetime
from pyspark.sql import Row
import os


def run():
    print('Start HELLO PYSPARK')

#    try:
#        print('ls -al /etc/secrets/cos_secrets :')
#        os.system('ls -al /etc/secrets/cos_secrets')
#    except BaseException as e:
#        print (e)

#    try:
#        print('Open Secret File /etc/secrets/cos_secrets/apikey:')
#        with open('/etc/secrets/cos_secrets/apikey', 'r') as cos_secret:
#            print(cos_secret.read())
#    except BaseException as e:
#        print (e)

    # Read COS connection parameters from environment variables
    s3_url = os.getenv('COS_ENDPOINT')
    s3_access_key = os.getenv('COS_ACCESS_KEY')
    s3_secret_key = os.getenv('COS_SECRET_KEY')
    bucket_name = os.getenv('COS_BUCKET')

    spark_builder = (
        SparkSession
            .builder
            .appName('Spark2COS-WithS3'))

    spark_builder.config('fs.s3a.access.key', s3_access_key)
    spark_builder.config('fs.s3a.secret.key', s3_secret_key)
    spark_builder.config('fs.s3a.endpoint', s3_url)

    spark = spark_builder.getOrCreate()

    df = spark.createDataFrame([
        Row(say='Hello', to='World', when=datetime(2000, 1, 1, 12, 0)),
        Row(say='Hello', to='PySpark', when=datetime(2000, 1, 2, 12, 0)),
        Row(say='Hello', to='IBM Cloud', when=datetime(2000, 1, 3, 12, 0)),
        Row(say='Hello', to='Kubernetes',  when=datetime(2000, 1, 4, 12, 0))
    ])
    df.show()

    # Bucket name : cos-bucket-am-dh-dev
    print('Write Dataframe as Parquet in a bucket using S3 API')
    try:
        df.write.parquet("s3a://cos-bucket-am-dh-dev2/hello_pyspark.parquet", mode="overwrite")
    except BaseException as e:
        print (e)

    print('Write Dataframe as CSV in a bucket using S3 API')
    try:
        df.write.csv("s3a://cos-bucket-am-dh-dev2/hello_pyspark.csv", mode="overwrite")
    except BaseException as e:
        print (e)

    print('End HELLO PYSPARK')
