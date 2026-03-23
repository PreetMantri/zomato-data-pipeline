# Zomato Data Pipeline

End-to-end data engineering pipeline built on Zomato restaurant data.

## Phase 1 — Python Data Cleaner
- Reads raw Zomato CSV data
- Removes duplicates and null values
- Modular structure using Python classes, functions and modules
- Outputs clean CSV ready for Databricks ingestion

## Tech Stack
Python | Pandas | PySpark (upcoming) | Databricks | Delta Lake

## Pipeline Architecture (In Progress)
Raw CSV → Python Cleaner → DBFS → PySpark Transforms → Delta Table → SQL Analytics