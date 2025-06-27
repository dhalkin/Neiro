import pandas as pd

from sqlalchemy import create_engine

# Use pandas to read the data from the MySQL database
# Create an SQLAlchemy engine
engine = create_engine('mysql+mysqlconnector://root:rootpassword@127.0.0.1:3301/catcher')

# Query to fetch data
query = "SELECT * FROM bybit_market_data where symbol = 'BTC'"

# Use pandas to read the data from the MySQL database
df = pd.read_sql(query, engine)

# Display the dataframe
print(df)
