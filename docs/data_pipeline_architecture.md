# Data Pipeline Architecture

## 1. Project Overview

This project implements an end-to-end data engineering pipeline using the Online Retail dataset from the UCI Machine Learning Repository.

The pipeline processes raw retail transaction data using Python and Pandas, stores structured data in PostgreSQL, and prepares the data for business intelligence analysis using Power BI.

## 2. Pipeline Architecture

The data pipeline consists of the following stages:

1. **Data Source:** Raw Online Retail Excel dataset.
2. **Data Inspection:** Inspect data structure, missing values, duplicates, and anomalies.
3. **Data Cleaning:** Remove exact duplicate records and classify transaction types.
4. **Data Transformation:** Calculate total sales and generate monthly, country, and product aggregations.
5. **Data Storage:** Save processed datasets as CSV files.
6. **Data Loading:** Load cleaned transaction data into PostgreSQL.
7. **Data Validation:** Verify row counts and reconcile sales totals.
8. **Data Visualization:** Connect Power BI to PostgreSQL for dashboard development.

## 3. Technologies

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Git and GitHub
- Power BI

## 4. Data Flow

Raw Excel Dataset → Python Processing → CSV Outputs → PostgreSQL → Power BI

## 5. Data Processing Results

- Original records: 541,909
- Exact duplicate records removed: 5,268
- Normal sales records: 524,878
- Total sales: £10,642,110.804
- Merchandise sales: £10,280,009.884

## 6. Data Validation

Sales reconciliation:

- All sales: £10,642,110.804
- Merchandise sales: £10,280,009.884
- Excluded codes (DOT, POST, M): £362,100.920

The reconciliation difference is effectively zero, confirming consistency between the sales totals and merchandise classification.

## 7. Expected Output

The final output of this project is a structured PostgreSQL database and a Power BI dashboard that provides insights into retail sales performance.


flowchart TD
    A["Online Retail.xlsx<br/>541,909 Records"]

    B["Data Inspection<br/>inspect_data.py"]
    C["Anomaly Investigation<br/>investigate_anomalies.py"]

    D["Data Cleaning<br/>clean_data.py"]
    E["Data Transformation<br/>transform_data.py"]

    F["Processed CSV Files<br/>Cleaned Transactions"]
    G["Aggregated CSV Files<br/>Monthly, Country, Product"]

    H[("PostgreSQL Database")]
    I["SQL Analysis<br/>analysis_queries.sql"]
    J["Power BI Dashboard"]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    E --> G
    F --> H
    G --> H
    H --> I
    I --> J

    K["Data Validation"]
    F -.-> K
    G -.-> K
    H -.-> K
