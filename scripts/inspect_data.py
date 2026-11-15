import pandas as pd

file_path = "Online Retail.xlsx"

df = pd.read_excel(file_path)

print("=== 5 BARIS PERTAMA ===")
print(df.head())

print("\n=== UKURAN DATASET ===")
print(df.shape)

print("\n=== TIPE DATA ===")
print(df.dtypes)

print("\n=== NILAI KOSONG ===")
print(df.isnull().sum())

print("\n=== DATA DUPLIKAT ===")
print(df.duplicated().sum())


print("\n=== PEMERIKSAAN KUALITAS DATA ===")

# 1. Invoice pembatalan
cancelled = df["InvoiceNo"].astype(str).str.startswith("C")
print("\nInvoice pembatalan:", cancelled.sum())

# 2. Quantity negatif
print("Quantity negatif:", (df["Quantity"] < 0).sum())

# 3. UnitPrice nol atau negatif
print("UnitPrice nol:", (df["UnitPrice"] == 0).sum())
print("UnitPrice negatif:", (df["UnitPrice"] < 0).sum())

# 4. Distribusi negara
print("\n=== 10 NEGARA DENGAN TRANSAKSI TERBANYAK ===")
print(df["Country"].value_counts().head(10))

# 5. Statistik numerik
print("\n=== STATISTIK DATA NUMERIK ===")
print(df[["Quantity", "UnitPrice"]].describe())