
-- =========================================
-- 1. TABEL TRANSAKSI UTAMA
-- =========================================

CREATE TABLE sales (
    id BIGSERIAL PRIMARY KEY,
    invoice_no VARCHAR(20),
    stock_code VARCHAR(20),
    description TEXT,
    quantity INTEGER,
    invoice_date TIMESTAMP,
    unit_price NUMERIC(12, 4),
    customer_id BIGINT,
    country VARCHAR(100),
    total_sales NUMERIC(14, 4)
);


-- =========================================
-- 2. AGREGASI PENJUALAN BULANAN
-- =========================================

CREATE TABLE monthly_sales AS
SELECT
    DATE_TRUNC('month', invoice_date)::DATE AS year_month,
    SUM(total_sales) AS total_sales,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT invoice_no) AS total_invoices,
    COUNT(DISTINCT customer_id) AS total_customers
FROM sales
GROUP BY DATE_TRUNC('month', invoice_date)
ORDER BY year_month;


-- =========================================
-- 3. AGREGASI PENJUALAN PER NEGARA
-- =========================================

CREATE TABLE country_sales AS
SELECT
    country,
    SUM(total_sales) AS total_sales,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT invoice_no) AS total_invoices,
    COUNT(DISTINCT customer_id) AS total_customers
FROM sales
GROUP BY country
ORDER BY total_sales DESC;


-- =========================================
-- 4. AGREGASI PENJUALAN PER PRODUK
-- =========================================

CREATE TABLE product_sales AS
SELECT
    stock_code,
    description,
    SUM(total_sales) AS total_sales,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT invoice_no) AS total_invoices,
    COUNT(DISTINCT customer_id) AS total_customers
FROM sales
GROUP BY stock_code, description
ORDER BY total_sales DESC;


-- =========================================
-- 5. AGREGASI KHUSUS MERCHANDISE
-- =========================================

CREATE TABLE product_sales_merchandise AS
SELECT *
FROM product_sales
WHERE stock_code NOT IN ('DOT', 'POST', 'M')
ORDER BY total_sales DESC;
