
import pandas as pd

# 1. Membaca data hasil cleaning
df = pd.read_csv("outputs/online_retail_clean.csv",dtype={"InvoiceNo": "string"})

# 2. Mengubah InvoiceDate menjadi format tanggal
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# 3. Membuat kolom bulan
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M")

# 4. Mengelompokkan data berdasarkan bulan
monthly_sales = (
    df.groupby("YearMonth")
    .agg(
        TotalSales=("TotalSales", "sum"),
        TotalQuantity=("Quantity", "sum"),
        TotalInvoices=("InvoiceNo", "nunique"),
        TotalCustomers=("CustomerID", "nunique")
    )
    .reset_index()
)

# 5. Mengubah YearMonth menjadi teks
monthly_sales["YearMonth"] = monthly_sales["YearMonth"].astype(str)

# 6. Menyimpan hasil transformasi
monthly_sales.to_csv("outputs/monthly_sales.csv", index=False)

# 7. Menampilkan hasil
print("=== MONTHLY SALES ===")
print(monthly_sales)

print("\nJumlah bulan:", len(monthly_sales))
print("Total penjualan:", monthly_sales["TotalSales"].sum())

print("\nFile berhasil disimpan: monthly_sales.csv")

print("\n=== DATA VALIDATION ===")

print(
    "Total sales sebelum transformasi:",
    df["TotalSales"].sum()
)

print(
    "Total sales setelah transformasi:",
    monthly_sales["TotalSales"].sum()
)

print(
    "Selisih:",
    abs(
        df["TotalSales"].sum()
        - monthly_sales["TotalSales"].sum()
    )
)


# ==========================================
# 8. COUNTRY SALES TRANSFORMATION
# ==========================================

country_sales = (
    df.groupby("Country")
    .agg(
        TotalSales=("TotalSales", "sum"),
        TotalQuantity=("Quantity", "sum"),
        TotalInvoices=("InvoiceNo", "nunique"),
        TotalCustomers=("CustomerID", "nunique")
    )
    .reset_index()
)

# Mengurutkan negara berdasarkan penjualan tertinggi
country_sales = country_sales.sort_values(
    by="TotalSales",
    ascending=False
)

# Menyimpan hasil
country_sales.to_csv("outputs/country_sales.csv", index=False)


# ==========================================
# 9. PRODUCT SALES TRANSFORMATION
# ==========================================

product_sales = (
    df.groupby(["StockCode", "Description"], dropna=False)
    .agg(
        TotalSales=("TotalSales", "sum"),
        TotalQuantity=("Quantity", "sum"),
        TotalInvoices=("InvoiceNo", "nunique"),
        TotalCustomers=("CustomerID", "nunique")
    )
    .reset_index()
)

# Mengurutkan produk berdasarkan penjualan tertinggi
product_sales = product_sales.sort_values(
    by="TotalSales",
    ascending=False
)

# Menyimpan hasil
product_sales.to_csv("outputs/product_sales.csv", index=False)


# ==========================================
# 10. MENAMPILKAN HASIL
# ==========================================

print("\n=== TOP 10 COUNTRY SALES ===")
print(country_sales.head(10))

print("\n=== TOP 10 PRODUCT SALES ===")
print(product_sales.head(10))

print("\nJumlah negara:", len(country_sales))
print("Jumlah produk:", len(product_sales))

print("\nFile berhasil disimpan:")
print("- country_sales.csv")
print("- product_sales.csv")


# ==========================================
# 11. DATA QUALITY CHECK
# ==========================================

print("\n=== MISSING CUSTOMER ID BY COUNTRY ===")

customer_check = (
    df.groupby("Country")
    .agg(
        TotalRows=("InvoiceNo", "size"),
        MissingCustomerID=("CustomerID", lambda x: x.isna().sum()),
        UniqueCustomers=("CustomerID", "nunique")
    )
    .reset_index()
)

customer_check["MissingPercentage"] = (
    customer_check["MissingCustomerID"]
    / customer_check["TotalRows"] * 100
)

print(
    customer_check.sort_values(
        by="MissingPercentage",
        ascending=False
    ).head(10)
)


# ==========================================
# 12. INVESTIGATE NON-MERCHANDISE ITEMS
# ==========================================

print("\n=== NON-MERCHANDISE ITEMS ===")

non_merchandise = product_sales[
    product_sales["StockCode"].isin(["DOT", "POST", "M"])
]

print(non_merchandise[
    ["StockCode", "Description", "TotalSales", "TotalQuantity"]
])


# ==========================================
# 13. MERCHANDISE ONLY TRANSFORMATION
# ==========================================

non_merchandise_codes = ["DOT", "POST", "M"]

merchandise_df = df[
    ~df["StockCode"].isin(non_merchandise_codes)
].copy()

merchandise_sales = (
    merchandise_df.groupby(
        ["StockCode", "Description"],
        dropna=False
    )
    .agg(
        TotalSales=("TotalSales", "sum"),
        TotalQuantity=("Quantity", "sum"),
        TotalInvoices=("InvoiceNo", "nunique"),
        TotalCustomers=("CustomerID", "nunique")
    )
    .reset_index()
)

merchandise_sales = merchandise_sales.sort_values(
    by="TotalSales",
    ascending=False
)

merchandise_sales.to_csv(
    "outputs/product_sales_merchandise.csv",
    index=False
)

print("\n=== TOP 10 MERCHANDISE SALES ===")
print(merchandise_sales.head(10))

print("\nJumlah kelompok merchandise:", len(merchandise_sales))
print("Total merchandise sales:", merchandise_sales["TotalSales"].sum())

print("\nFile berhasil disimpan: product_sales_merchandise.csv")


# ==========================================
# 14. FINAL TRANSFORMATION VALIDATION
# ==========================================

all_sales = df["TotalSales"].sum()

merchandise_total = merchandise_df["TotalSales"].sum()

non_merchandise_total = df[
    df["StockCode"].isin(non_merchandise_codes)
]["TotalSales"].sum()

print("\n=== FINAL TRANSFORMATION VALIDATION ===")

print("All sales:", all_sales)
print("Merchandise sales:", merchandise_total)
print("Non-merchandise sales:", non_merchandise_total)

print(
    "Reconciliation difference:",
    abs(all_sales - (merchandise_total + non_merchandise_total))
)

print("\nJumlah transaksi sumber:", len(df))
print("Jumlah transaksi merchandise:", len(merchandise_df))
print("Jumlah kelompok produk:", len(merchandise_sales))
