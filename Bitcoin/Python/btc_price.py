# Gets the current bitcoin price from Coingecko API and inserts to btc_prices table

import requests
import psycopg2
from datetime import datetime

# Fetch Bitcoin price from CoinGecko API
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
response = requests.get(url)
data = response.json()
price_usd = data['bitcoin']['usd']

# Connect to PostgreSQL
try:
    conn = psycopg2.connect("dbname=bitcoin_prices")
    cur = conn.cursor()

    # Insert price into the database
    timestamp = datetime.now()
    cur.execute("INSERT INTO btc_prices (timestamp, price_usd) VALUES (%s, %s)", (timestamp, price_usd))

    # Commit and close the connection
    conn.commit()
    cur.close()
    conn.close()

    print(f"Inserted price: ${price_usd} at {timestamp}")

except Exception as e:
    print(f"Error: {e}")