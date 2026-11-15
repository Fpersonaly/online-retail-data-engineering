
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from getpass import getpass

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
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print("Koneksi berhasil!")
        print(result.fetchone()[0])
except Exception as e:
    print("Koneksi gagal:")
    print(e)
finally:
    engine.dispose()
