
import pandas as pd

# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_excel("Online Retail.xlsx")

print("DATA BERHASIL DIMUAT")
print("Total baris:", len(df))


# ==========================================
# 2. INVESTIGASI INVOICE PEMBATALAN
# ==========================================

cancelled = df["InvoiceNo"].astype(str).str.startswith("C")
negative_qty = df["Quantity"] < 0

print("\n=== 1. INVESTIGASI INVOICE PEMBATALAN ===")

print("Total baris invoice pembatalan:",
      cancelled.sum())

print("Pembatalan dengan Quantity negatif:",
      (cancelled & negative_qty).sum())

print("Pembatalan dengan Quantity positif atau nol:",
      (cancelled & ~negative_qty).sum())

print("Quantity negatif tanpa awalan C:",
      (~cancelled & negative_qty).sum())


# ==========================================
# 3. INVESTIGASI QUANTITY NEGATIF
# ==========================================

print("\n=== 2. CONTOH QUANTITY NEGATIF ===")

negative_data = df[negative_qty]

print("Jumlah baris:", len(negative_data))

print(
    negative_data[
        ["InvoiceNo", "StockCode", "Description",
         "Quantity", "UnitPrice", "CustomerID"]
    ].head(10).to_string(index=False)
)


# ==========================================
# 4. INVESTIGASI UNITPRICE NOL
# ==========================================

print("\n=== 3. INVESTIGASI UNITPRICE NOL ===")

zero_price = df[df["UnitPrice"] == 0]

print("Jumlah baris:", len(zero_price))

print(
    zero_price[
        ["InvoiceNo", "StockCode", "Description",
         "Quantity", "UnitPrice"]
    ].head(10).to_string(index=False)
)


# ==========================================
# 5. INVESTIGASI UNITPRICE NEGATIF
# ==========================================

print("\n=== 4. INVESTIGASI UNITPRICE NEGATIF ===")

negative_price = df[df["UnitPrice"] < 0]

print(
    negative_price[
        ["InvoiceNo", "StockCode", "Description",
         "Quantity", "UnitPrice", "CustomerID"]
    ].to_string(index=False)
)


# ==========================================
# 6. INVESTIGASI DUPLIKAT
# ==========================================

print("\n=== 5. INVESTIGASI DATA DUPLIKAT ===")

duplicates = df[df.duplicated(keep=False)]

print("Total baris dalam kelompok duplikat:",
      len(duplicates))

print(
    duplicates.sort_values(
        by=["InvoiceNo", "StockCode"]
    ).head(10).to_string(index=False)
)



# ==========================================
# 7. INVESTIGASI QUANTITY NEGATIF TANPA C
# ==========================================

print("\n=== QUANTITY NEGATIF TANPA INVOICE C ===")

negative_without_c = df[
    (~cancelled) & negative_qty
]

print("Total:", len(negative_without_c))

print("\nContoh data:")
print(
    negative_without_c[
        ["InvoiceNo", "StockCode", "Description",
         "Quantity", "UnitPrice"]
    ].head(20).to_string(index=False)
)

print("\nDeskripsi yang paling sering muncul:")
print(
    negative_without_c["Description"]
    .value_counts(dropna=False)
    .head(10)
)


# ==========================================
# 8. INVESTIGASI UNITPRICE NOL
# ==========================================

print("\n=== ANALISIS UNITPRICE NOL ===")

zero_price = df[df["UnitPrice"] == 0]

print("Jumlah baris:", len(zero_price))

print("\nDeskripsi yang paling sering muncul:")
print(
    zero_price["Description"]
    .value_counts(dropna=False)
    .head(15)
)

print("\nApakah Quantity positif atau negatif?")
print(
    zero_price["Quantity"]
    .apply(lambda x: "Positif" if x > 0 else
           "Negatif" if x < 0 else "Nol")
    .value_counts()
)


# ==========================================
# 9. VERIFIKASI DUPLIKAT IDENTIK
# ==========================================

print("\n=== VERIFIKASI DUPLIKAT IDENTIK ===")

print("Duplikat tambahan:",
      df.duplicated().sum())

print("Baris dalam kelompok duplikat:",
      df.duplicated(keep=False).sum())

print("\nContoh duplikat identik:")
print(
    df.loc[df.duplicated(keep=False)]
    .sort_values(by=["InvoiceNo", "StockCode"])
    .head(20)
    .to_string(index=False)
)

# ==========================================
# 10. HUBUNGAN QUANTITY NEGATIF DAN HARGA NOL
# ==========================================

print("\n=== HUBUNGAN QUANTITY NEGATIF DAN HARGA NOL ===")

negative_without_c = df[
    (~cancelled) & negative_qty
]

zero_price = df[df["UnitPrice"] == 0]

print(
    "Quantity negatif tanpa C dan harga nol:",
    ((~cancelled) & negative_qty & (df["UnitPrice"] == 0)).sum()
)

print(
    "Quantity negatif tanpa C dan harga tidak nol:",
    ((~cancelled) & negative_qty & (df["UnitPrice"] != 0)).sum()
)

print("\n=== CONTOH QUANTITY POSITIF DENGAN HARGA NOL ===")

print(
    df.loc[
        (df["UnitPrice"] == 0) & (df["Quantity"] > 0),
        ["InvoiceNo", "StockCode", "Description",
         "Quantity", "UnitPrice"]
    ].head(15).to_string(index=False)
)
