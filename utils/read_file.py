"""
used to open and read a excel or csv file, return
"""

import pyspark
import pandas as pd
from pyspark.context import SparkContext
from pyspark.sql import SparkSession,SQLContext
spark = SparkSession.builder.appName("Basics").getOrCreate()
sc=spark.sparkContext
sqlContext = SQLContext(sc)
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()


def reading_daily_file(filename):#read csv file

    if filename.endswith('.csv'):
        df1=spark.read.csv(filename,header=True)
        df1.show()
    if filename.endswith('.xlsx'):#read excel file
        
        df1 = pd.read_excel(filename)
        df1 = sqlContext.createDataFrame(df1)
        df1.show()
    return df1


def reading_monthly_file(filename):#read csv file

    if filename.endswith('.csv'):
        df1=spark.read.csv(filename,header=True)
        df1.show()
    if filename.endswith('.xlsx'):#read excel file
        
        df1 = pd.read_excel(filename)
        df1 = sqlContext.createDataFrame(df1)
        df1.show()
    return df1

  
