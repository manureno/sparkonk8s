
FROM pyspark-3.1.3

# Reset to root to run installation tasks
USER 0

RUN mkdir -p /opt/hello_pyspark

# Install the hello_pyspark package and its dependencies
COPY ./dist/hello_pyspark-1.0-py2.py3-none-any.whl /opt/hello_pyspark
RUN pip3 install --no-cache-dir /opt/hello_pyspark/hello_pyspark-1.0-py2.py3-none-any.whl

# Add a launcher to be referenced by spark-submit command
COPY ./src/launcher.py /opt/hello_pyspark

# Specify the User that the actual main process will run as
ARG spark_uid=185
USER ${spark_uid}
