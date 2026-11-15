
-- =========================================
-- 1. TOTAL TRANSAKSI
-- =========================================

SELECT
    COUNT(*) AS total_transactions
FROM sales;


-- =========================================
-- 2. TOTAL PENJUALAN
-- =========================================

SELECT
    SUM(total_sales) AS total_sales
FROM sales;


-- =========================================
-- 3. TREN PENJUALAN BULANAN
-- =========================================

SELECT *
FROM monthly_sales
ORDER BY year_month;


-- =========================================
-- 4. 10 NEGARA DENGAN PENJUALAN TERTINGGI
-- =========================================

SELECT *
FROM country_sales
ORDER BY total_sales DESC
LIMIT 10;


-- =========================================
-- 5. 10 PRODUK DENGAN PENJUALAN TERTINGGI
-- =========================================

SELECT *
FROM product_sales
ORDER BY total_sales DESC
LIMIT 10;


-- =========================================
-- 6. 10 PRODUK MERCHANDISE TERATAS
-- =========================================

SELECT *
FROM product_sales_merchandise
ORDER BY total_sales DESC
LIMIT 10;


-- =========================================
-- 7. REKONSILIASI PENJUALAN
-- =========================================

SELECT
    (SELECT SUM(total_sales) FROM sales) AS all_sales,

    (SELECT SUM(total_sales)
     FROM product_sales_merchandise) AS merchandise_sales,

    (SELECT SUM(total_sales)
     FROM product_sales
     WHERE stock_code IN ('DOT', 'POST', 'M')) AS excluded_sales;


-- =========================================
-- 8. PEMERIKSAAN DATA KOSONG
-- =========================================

SELECT
    COUNT(*) AS total_rows,
    COUNT(*) FILTER (WHERE customer_id IS NULL)
        AS missing_customer_id,
    COUNT(*) FILTER (WHERE description IS NULL)
        AS missing_description
FROM sales;
