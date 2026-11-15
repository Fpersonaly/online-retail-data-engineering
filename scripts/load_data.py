import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from getpass import getpass


# Membaca data CSV
df = pd.read_csv(
    "outputs/online_retail_clean.csv",
    dtype={
        "InvoiceNo": "string",
        "StockCode": "string"
    }
)

# Mengubah nama kolom agar sesuai dengan PostgreSQL
df = df.rename(columns={
    "InvoiceNo": "invoice_no",
    "StockCode": "stock_code",
    "Description": "description",
    "Quantity": "quantity",
    "InvoiceDate": "invoice_date",
    "UnitPrice": "unit_price",
    "CustomerID": "customer_id",
    "Country": "country",
    "TotalSales": "total_sales"
})

# Menghapus kolom flag yang tidak ada di tabel sales
df = df.drop(columns=[
    "IsCancellation",
    "IsStockAdjustment",
    "IsAccountingAdjustment"
])

# Mengubah tipe data
df["invoice_date"] = pd.to_datetime(df["invoice_date"])

df["customer_id"] = pd.to_numeric(
    df["customer_id"], errors="coerce"
).map(lambda x: int(x) if pd.notna(x) else None)

print("Jumlah data:", len(df))
print("Kolom:", df.columns.tolist())


# 3. Membuat koneksi database
password = getpass("Masukkan password PostgreSQL: ")

connection_url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password=password,
    host="localhost",
    port=5432,
    database="online_retail_db"
)

engine = create_engine(connection_url)

try:
    with engine.begin() as connection:
        # 4. Memastikan tabel masih kosong
        existing_rows = connection.execute(
            text("SELECT COUNT(*) FROM sales")
        ).scalar()

        if existing_rows > 0:
            raise Exception(
                "Tabel sales sudah berisi data. "
                "Proses dihentikan agar tidak terjadi duplikasi."
            )

        # 5. Memasukkan data ke PostgreSQL
        df.to_sql(
            name="sales",
            con=connection,
            if_exists="append",
            index=False,
            chunksize=5000
        )

    # 6. Memverifikasi jumlah data
    with engine.connect() as connection:
        total_rows = connection.execute(
            text("SELECT COUNT(*) FROM sales")
        ).scalar()

    print("Data berhasil dimasukkan!")
    print("Jumlah baris di PostgreSQL:", total_rows)

except Exception as e:
    print("Proses gagal:")
    print(e)

finally:
    engine.dispose()
