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

-- COMMAND ----------

show databases;

-- COMMAND ----------

use mydb;
show tables;

-- COMMAND ----------

select * from mydb.employee;

-- COMMAND ----------

select * from legsim.stocks limit 10

-- COMMAND ----------

select count(*) from mydb.sales_data4;

-- COMMAND ----------

select * from mydb.sales_data4 limit 20;

-- COMMAND ----------

select year, quarter, count(*) from mydb.sales_data4 group by year,quarter;

-- COMMAND ----------

