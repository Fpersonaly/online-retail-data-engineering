# Online Retail Data Engineering Project

## Overview

This project demonstrates an end-to-end data engineering workflow using the Online Retail dataset from the UCI Machine Learning Repository.

The project covers data inspection, data cleaning, data transformation, loading data into PostgreSQL, and data validation.

## Tech Stack

- Python 3.12
- Pandas
- OpenPyXL
- SQLAlchemy
- PostgreSQL
- pgAdmin 4

## Project Workflow

1. **Data Inspection** – Inspect the dataset structure, missing values, duplicates, and anomalies.
2. **Data Cleaning** – Remove exact duplicates and classify cancellation and adjustment records.
3. **Data Transformation** – Calculate sales values and aggregate data by month, country, and product.
4. **Data Loading** – Load 524,878 cleaned transaction rows into PostgreSQL.
5. **Data Validation** – Validate row counts, sales totals, and aggregation results.

## Database Tables

| Table | Description |
|---|---|
| `sales` | Cleaned transaction-level sales data |
| `monthly_sales` | Sales aggregation by month |
| `country_sales` | Sales aggregation by country |
| `product_sales` | Sales aggregation by product code and description |
| `product_sales_merchandise` | Product aggregation excluding DOT, POST, and M codes |

## Key Results

- 541,909 original records.
- 5,268 exact duplicate rows removed.
- 524,878 normal sales records loaded into PostgreSQL.
- 38 countries represented in the country-level analysis.
- 4,161 product groups in the product-level analysis.
- Total sales: **£10,642,110.804**.
- Merchandise sales after excluding DOT, POST, and M: **£10,280,009.884**.

## Data Validation

The total sales were reconciled as follows:

| Category | Total Sales |
|---|---:|
| All sales | £10,642,110.804 |
| Merchandise sales | £10,280,009.884 |
| Excluded codes (DOT, POST, M) | £362,100.920 |
| Difference | £0 |

## Project Structure

```text
online-retail-data-engineering/
├── scripts/
│   ├── inspect_data.py
│   ├── investigate_anomalies.py
│   ├── clean_data.py
│   ├── transform_data.py
│   ├── test_connection.py
│   └── load_data.py
├── sql/
│   ├── create_tables.sql
│   └── analysis_queries.sql
├── outputs/
│   ├── country_sales.csv
│   ├── monthly_sales.csv
│   ├── online_retail_clean.csv
│   ├── online_retail_processed_all.csv
│   ├── product_sales.csv
│   └── product_sales_merchandise.csv
├── .gitignore
├── README.md
└── requirements.txt
```

The `.venv/` directory contains the local Python virtual environment and is excluded from version control.

The raw dataset `Online Retail.xlsx` is also excluded from version control.

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd online-retail-data-engineering
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the dataset

Download the Online Retail dataset from the UCI Machine Learning Repository and place `Online Retail.xlsx` in the project root directory.

### 5. Run the data inspection scripts

```bash
python scripts/inspect_data.py
python scripts/investigate_anomalies.py
```

### 6. Clean and transform the data

```bash
python scripts/clean_data.py
python scripts/transform_data.py
```

### 7. Set up PostgreSQL

- Create a PostgreSQL database named `online_retail_db`.
- Execute the `sales` table definition from `sql/create_tables.sql` using pgAdmin.
- Configure the PostgreSQL connection in the Python loading script as required.

### 8. Test the database connection

```bash
python scripts/test_connection.py
```

### 9. Load the cleaned data

```bash
python scripts/load_data.py
```

### 10. Create aggregation tables and run analysis queries

After loading the transaction data, execute the remaining aggregation statements in `sql/create_tables.sql`.

Use `sql/analysis_queries.sql` to run the analysis and validation queries.

## Notes

- December 2011 is a partial month because the dataset ends on December 9, 2011.
- Missing `CustomerID` values are retained in the transaction data.
- DOT, POST, and M are excluded from the merchandise-only analysis. This does not establish that every non-merchandise code has been identified.
- Total sales represent `Quantity × UnitPrice` for the filtered normal sales records, not necessarily accounting revenue or profit.

## Data Source

UCI Machine Learning Repository – Online Retail Dataset.