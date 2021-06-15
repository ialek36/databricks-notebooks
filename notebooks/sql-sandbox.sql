-- Databricks notebook source
--  update 1
--  upate 2
-- update 3

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

