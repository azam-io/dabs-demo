# Databricks notebook source

job_params = dbutils.widgets.getAll()

job_var = job_params.get("job_var", "job_var not fetched")

print("we pushed this via CI/CD")

print(job_var)
