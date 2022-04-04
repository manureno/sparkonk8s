
"""Run a spark job that creates a "hello world" DataFrame.
Print the DataFrame to stdout, write to Bucket according to command line options.

Usage:
    launcher.py
    launcher.py [-b BUCKET_NAME]
    launcher.py (-h | --help)

Options:
    -b --bucket_name BUCKET_NAME  Write the DataFrame to BUCKET_NAME, only putput to stdout if no bucket specified.
    -h --help                     Show This help message and exits
"""

from hello_pyspark import hello_pyspark_s3
from docopt import docopt

def launch():
    arguments = docopt(__doc__)

    bucket_name = arguments["--bucket_name"]

    print("Bucket : {}".format(bucket_name))

    hello_pyspark_s3.run(bucket_name=bucket_name)


if __name__ == "__main__":
    launch()