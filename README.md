# PySpark Basics
## Apache Spark
Apache Spark is one of the hottest new trends in the technology domain. It is the framework with probably the highest potential to realize the fruit of the marriage between Big Data and Machine Learning. It runs fast (up to 100x faster than traditional MapReduce) due to in-memory operation, offers robust, distributed, fault-tolerant data objects (called RDD), and integrates beautifully with the world of machine learning and graph analytics through supplementary packages like Mlib and GraphX.

Spark is implemented on Hadoop/HDFS and written mostly in Scala, a functional programming language, similar to Java. In fact, Scala needs the latest Java installation on your system and runs on JVM. However, for most of the beginners, Scala is not a language that they learn first to venture into the world of data science. Fortunately, Spark provides a wonderful Python integration, called PySpark, which lets Python programmers to interface with the Spark framework and learn how to manipulate data at scale and work with objects and algorithms over a distributed file system.

## Basics of the `DataFrame`
### DataFrame
In Apache Spark, a DataFrame is a distributed collection of rows under named columns. It is conceptually equivalent to a table in a relational database, an Excel sheet with Column headers, or a data frame in R/Python, but with richer optimizations under the hood. DataFrames can be constructed from a wide array of sources such as: structured data files, tables in Hive, external databases, or existing RDDs. It also shares some common characteristics with RDD:

* __Immutable in nature__ : We can create DataFrame / RDD once but can’t change it. And we can transform a DataFrame / RDD  after applying transformations.
* __Lazy Evaluations__: Which means that a task is not executed until an action is performed.
* __Distributed__: RDD and DataFrame both are distributed in nature.

### Advantages of the DataFrame

* DataFrames are designed for processing large collection of structured or semi-structured data.
* Observations in Spark DataFrame are organised under named columns, which helps Apache Spark to understand the schema of a DataFrame. This helps Spark optimize execution plan on these queries.
* DataFrame in Apache Spark has the ability to handle petabytes of data.
* DataFrame has a support for wide range of data format and sources.
* It has API support for different languages like Python, R, Scala, Java.
