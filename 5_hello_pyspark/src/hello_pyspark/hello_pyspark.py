from pyspark.sql import SparkSession
from datetime import datetime
from pyspark.sql import Row

def run():
    spark = SparkSession.builder.getOrCreate()

    df = spark.createDataFrame([
        Row(say='Hello', to='World', when=datetime(2000, 1, 1, 12, 0)),
        Row(say='Hello', to='PySpark', when=datetime(2000, 1, 2, 12, 0)),
        Row(say='Hello', to='IBM Cloud', when=datetime(2000, 1, 3, 12, 0)),
        Row(say='Hello', to='Kubernetes',  when=datetime(2000, 1, 4, 12, 0))
    ])

    df.show()




