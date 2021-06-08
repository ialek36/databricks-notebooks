# Databricks notebook source
# MAGIC %sql show databases;

# COMMAND ----------

# MAGIC %sql 
# MAGIC use mydb;
# MAGIC show tables;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employee limit 10

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW CREATE TABLE mydb.employee;

# COMMAND ----------

# MAGIC %sql
# MAGIC select country from mydb.sales_data limit 10;

# COMMAND ----------

dbutils.fs.ls("s3a://denisgor-databricks-storage/")

# COMMAND ----------

# MAGIC %scala 
# MAGIC val df = spark.read.format("csv")
# MAGIC //   .option("header", "true")
# MAGIC   .option("inferSchema", "true")
# MAGIC   .load("s3a://databricks2-data-bucket/wavelength/c.csv")
# MAGIC 
# MAGIC display(df)

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC df = spark.read.format("csv") \
# MAGIC .option("inferSchema", "true") \
# MAGIC .option("header", "true")\
# MAGIC .load("s3a://igor-databricks-storage/sales/Sampleout.csv")
# MAGIC display(df)

# COMMAND ----------

# MAGIC %sh
# MAGIC ls

# COMMAND ----------

# MAGIC %sh
# MAGIC mlflow

# COMMAND ----------

# MAGIC %sh
# MAGIC mlflow sagemaker build-and-push-container

# COMMAND ----------

df = spark.read.format("csv") \
.option("inferSchema", "true") \
.option("header", "true")\
.load("s3a://satish-databricks-data-storage/test/EMPLOYEE.csv")
display(df)