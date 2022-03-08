-- Databricks notebook source
-- update 55 in feature13

-- COMMAND ----------


show databases;

-- COMMAND ----------

select * from heart2.employee2;

-- COMMAND ----------

use default;
show tables;

-- COMMAND ----------

alter table default.diamonds rename to default.diamonds2;

-- COMMAND ----------

alter table heart2.employee2 rename to heart2.employee3;

-- COMMAND ----------

|use default;
create table delta_sales
using delta
location 's3://databricks2-data-bucket/sales_delta5'
as select * from mydb.sales_data4;

-- COMMAND ----------

select * from default.delta_sales;

-- COMMAND ----------

select * from delta.`s3://databricks2-data-bucket/sales_delta`

-- COMMAND ----------

select count(*) from mydb.sales_data4;

-- COMMAND ----------

select * from mydb.sales_data4 limit 20;

-- COMMAND ----------

select year, quarter, count(*) from mydb.sales_data4 group by year,quarter;

-- COMMAND ----------

select * from delta.`s3://databricks2-data-bucket/stock_quotes_partitioned/core8` limit 10;

-- COMMAND ----------

select * from delta.`s3://databricks2-data-bucket/sp500red/core/`

-- COMMAND ----------

select * from delta.`s3://databricks2-data-bucket/sp500red/core`

-- COMMAND ----------


