-- Databricks notebook source
--  update 1
--  upate 2
-- update 3
-- update 4
-- update 5
-- update 6
-- update 7
-- up8
--up9
--up10
--up11
--up12
-- up13
-- up14
-- up15
--up16
--up17
--up18
--up19
--up20
-- up21
--up22
--up23
--up24
--up25
--up26
--up27
--up28
--up30
--31
--32

-- COMMAND ----------


show databases;

-- COMMAND ----------

use mydb;
show tables;

-- COMMAND ----------

select * from mydb.employee;

-- COMMAND ----------

use default;
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

