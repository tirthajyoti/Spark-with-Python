# Spark with Python
![](https://cdn-images-1.medium.com/max/1202/1*wiXLNwwMyWdyyBuzZnGrWA.png)
## Apache Spark
[Apache Spark](https://spark.apache.org/) is one of the hottest new trends in the technology domain. It is the framework with probably the **highest potential to realize the fruit of the marriage between Big Data and Machine Learning**. It runs fast (up to 100x faster than traditional [Hadoop MapReduce](https://www.tutorialspoint.com/hadoop/hadoop_mapreduce.htm)) due to in-memory operation, offers robust, distributed, fault-tolerant data objects (called [RDD](https://www.tutorialspoint.com/apache_spark/apache_spark_rdd.htm)), and integrates beautifully with the world of machine learning and graph analytics through supplementary packages like [Mlib](https://spark.apache.org/mllib/) and [GraphX](https://spark.apache.org/graphx/).
<br>
<p align='center'>
<img src="https://raw.githubusercontent.com/tirthajyoti/PySpark_Basics/master/Images/Spark%20ecosystem.png" width="400" height="400">
</p>
Spark is implemented on Hadoop/HDFS and written mostly in Scala, a functional programming language, similar to Java. In fact, Scala needs the latest Java installation on your system and runs on JVM. However, for most of the beginners, Scala is not a language that they learn first to venture into the world of data science. Fortunately, Spark provides a wonderful Python integration, called <b>PySpark, which lets Python programmers to interface with the Spark framework and learn how to manipulate data at scale and work with objects and algorithms over a distributed file system.</b>

## Setting up Apache Spark with Python 3 and Jupyter notebook
Unlike most Python libraries, getting PySpark to start working properly is not as straightforward as `pip install ...` and `import ...` Most of us with Python-based data science and Jupyter/IPython background take this workflow as granted for all popular Python packages. We tend to just head over to our CMD or BASH shell, type the pip install command, launch a Jupyter notebook and import the library to start practicing.
> But, PySpark+Jupyter combo needs a little bit more love :-)
<br>
<p align='center'>
<img src="https://raw.githubusercontent.com/tirthajyoti/PySpark_Basics/master/Images/Components.png" width="500" height="300">
</p>

#### Check which version of Python is running. Python 3.4+ is needed.
`python3 --version`

#### Update apt-get
`sudo apt-get update`

#### Install pip3 (or pip for Python3)
`sudo apt install python3-pip`

#### Install Jupyter for Python3
`pip3 install jupyter`

#### Augment the PATH variable to launch Jupyter notebook
`export PATH=$PATH:~/.local/bin`

#### Java 8 is shown to work with UBUNTU 18.04  LTS/SPARK-2.3.1-BIN-HADOOP2.7
```
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get install oracle-java8-installer
sudo apt-get install oracle-java8-set-default
```
#### Set Java related PATH variables
```
export JAVA_HOME=/usr/lib/jvm/java-8-oracle
export JRE_HOME=/usr/lib/jvm/java-8-oracle/jre
```
#### Install Scala
`sudo apt-get install scala`

#### Install py4j for Python-Java integration
`pip3 install py4j`

#### Download latest Apache Spark (with pre-built Hadoop) from [Apache download server](https://spark.apache.org/downloads.html). Unpack Apache Spark after downloading
`sudo tar -zxvf spark-2.3.1-bin-hadoop2.7.tgz`

#### Set variables to launch PySpark with Python3 and enable it to be called from Jupyter notebook. Add all the following lines to the end of your .bashrc file
```
export SPARK_HOME='/home/tirtha/Spark/spark-2.3.1-bin-hadoop2.7'
export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
export PYSPARK_DRIVER_PYTHON="jupyter"
export PYSPARK_DRIVER_PYTHON_OPTS="notebook"
export PYSPARK_PYTHON=python3
export PATH=$SPARK_HOME:$PATH:~/.local/bin:$JAVA_HOME/bin:$JAVA_HOME/jre/bin
```
### Source .bashrc
`source .bashrc`

## Basics of the `DataFrame`
![](https://www.ideata-analytics.com/wp-content/uploads/2016/06/ApacheSparkDataset1.jpg)
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

