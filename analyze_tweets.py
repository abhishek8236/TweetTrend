%pyspark
from pyspark import SparkConf, SparkContext
from pyspark.sql import Row
from pyspark.sql import SparkSession
import datetime
#import boto3
#import sys
#import MySQLdb
#import mysql.connector
#import os
#import re
#from awscli.clidriver import create_clidriver
import json
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.column import Column, _to_java_column, _to_seq
#from pyspark.sql.functions import year, month, dayofmonth, sha1, sha2, hash, udf

##########################################
# initialize sc
sprkSession = SparkSession.builder.getOrCreate()
sprkSession.catalog.clearCache()

jsonFileLocation = "s3a://testcontrolstreamstage/tweet/"

jsonTweet = sprkSession.read.json(jsonFileLocation)
#jsonTweet.printSchema()
#jsonTweet.createOrReplaceTempView("tweetdata")
#sprkSession.sql("select * from tweetdata limit 10;").show()

s = jsonTweet.filter((col("created_at").isNotNull() ) & (col("lang") == 'en'))

s2 = s.withColumn('trend', explode(split(col('text'), ' ')))\
    .groupBy('trend')\
    .count()\
    .sort('count', ascending=False)\
    .select('trend','count')\
    .write.format('json').save('s3a://testcontrolstreamstage/trends/', mode='overwrite')
#.write.format('json').save('s3a://testcontrolstreamstage/trends/', mode='append')
#.show()

#s2.where(col("trend").like("#%")).show()


