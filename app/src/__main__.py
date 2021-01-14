from pyspark.sql import SparkSession


any_file = "tests/files/sample_file_01.txt"  # Should be some file on your system

spark = \
    SparkSession\
        .builder\
        .appName("Text Redacter")\
        .getOrCreate()

base_df = spark.read.csv(any_file, sep='|', header=True)
base_df.show()




# logData = spark.read.text(logFile).cache()
#
# numAs = logData.filter(logData.value.contains('a')).count()
# numBs = logData.filter(logData.value.contains('b')).count()
#
# print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()