from pyspark.sql import SparkSession
from datetime import datetime
from pyspark.sql import Row
import os


def run(bucket_name):
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


    spark_builder = (
        SparkSession
            .builder
            .appName('Spark2COS-WithS3'))


    spark = spark_builder.getOrCreate()

    df = spark.createDataFrame([
        Row(say='Hello', to='World', when=datetime(2000, 1, 1, 12, 0)),
        Row(say='Hello', to='PySpark', when=datetime(2000, 1, 2, 12, 0)),
        Row(say='Hello', to='IBM Cloud', when=datetime(2000, 1, 3, 12, 0)),
        Row(say='Hello', to='Kubernetes',  when=datetime(2000, 1, 4, 12, 0))
    ])
    df.show()

    if bucket_name is not None:
        # Bucket name : cos-bucket-am-dh-dev
        print('Write Dataframe as Parquet in a bucket {} using S3 API'.format(bucket_name))
        try:
            pass
            df.write.parquet("s3a://{}/hello_pyspark.parquet".format(bucket_name), mode="overwrite")
        except BaseException as e:
            print (e)

        print('Write Dataframe as CSV in a bucket {} using S3 API'.format(bucket_name))
        try:
            pass
            df.write.csv("s3a://{}/hello_pyspark.csv".format(bucket_name), mode="overwrite")
        except BaseException as e:
            print (e)

    print('End HELLO PYSPARK')
