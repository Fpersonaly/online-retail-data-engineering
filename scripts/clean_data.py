
import pandas as pd

# ==========================================
# 1. LOAD DATA MENTAH
# ==========================================

df = pd.read_excel("Online Retail.xlsx")

print("=== DATA AWAL ===")
print("Jumlah baris:", len(df))


# ==========================================
# 2. HAPUS DUPLIKAT IDENTIK
# ==========================================

duplicate_count = df.duplicated().sum()

df = df.drop_duplicates()

print("\n=== DUPLIKAT ===")
print("Duplikat yang dihapus:", duplicate_count)
print("Sisa baris:", len(df))


# ==========================================
# 3. IDENTIFIKASI JENIS TRANSAKSI
# ==========================================

# Invoice dengan awalan C = pembatalan
df["IsCancellation"] = (
    df["InvoiceNo"].astype(str).str.startswith("C")
)

# Quantity negatif tanpa awalan C
df["IsStockAdjustment"] = (
    (~df["IsCancellation"]) &
    (df["Quantity"] < 0) &
    (df["UnitPrice"] == 0)
)

# Harga negatif = penyesuaian akuntansi
df["IsAccountingAdjustment"] = df["UnitPrice"] < 0


# ==========================================
# 4. PISAHKAN DATA TRANSAKSI NORMAL
# ==========================================

normal_sales = df[
    (~df["IsCancellation"]) &
    (~df["IsStockAdjustment"]) &
    (~df["IsAccountingAdjustment"]) &
    (df["Quantity"] > 0) &
    (df["UnitPrice"] > 0)
].copy()


# ==========================================
# 5. HITUNG NILAI PENJUALAN
# ==========================================

normal_sales["TotalSales"] = (
    normal_sales["Quantity"] *
    normal_sales["UnitPrice"]
)


# ==========================================
# 6. SIMPAN HASIL
# ==========================================

normal_sales.to_csv(
    "outputs/online_retail_clean.csv",
    index=False
)

df.to_csv(
    "outputs/online_retail_processed_all.csv",
    index=False
)


# ==========================================
# 7. VALIDASI HASIL
# ==========================================

print("\n=== HASIL DATA CLEANING ===")

print("Total data setelah hapus duplikat:", len(df))
print("Total transaksi penjualan normal:", len(normal_sales))
print("Total nilai penjualan:", normal_sales["TotalSales"].sum())

print("\n=== PEMERIKSAAN DATA HASIL ===")
print("Quantity <= 0:", (normal_sales["Quantity"] <= 0).sum())
print("UnitPrice <= 0:", (normal_sales["UnitPrice"] <= 0).sum())
print("Duplikat:", normal_sales.duplicated().sum())

print("\nFile berhasil disimpan:")
print("- online_retail_clean.csv")
print("- online_retail_processed_all.csv")
