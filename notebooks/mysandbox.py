# Databricks notebook source
# MAGIC %sql show databases;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from mydb.sales_data limit 10;

# COMMAND ----------

dbutils.fs.ls("s3a://igor-sa-launch-demo/")

# COMMAND ----------

