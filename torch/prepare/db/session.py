from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

engine_charon = create_engine("mysql+mysqlconnector://charon_user:charon-password@charon-db-mysql.c96i0s8w8kfk.eu-north-1.rds.amazonaws.com:3306/charon")
Session_charon = sessionmaker(bind=engine_charon)
session = Session_charon()

def get_last_data_by_symbol(symbol: str, until: str = "2025-12-31 00:00:00"):
    try:
        result = session.execute(text("SELECT lastPrice, volume24h, bid1Size, ask1Size, bid1Price, ask1Price, created_at FROM bybit_tickers where symbol = :symbol and created_at < :until order by created_at asc"), {"symbol": symbol, "until": until})
        return result
    finally:
        session.close()


def get_list_of_symbols():
    try:
        result = session.execute(text("SELECT DISTINCT symbol FROM bybit_tickers"))
        return [row[0] for row in result]
    finally:
        session.close()


def get_list_of_symbols_with_atr_last_price():
    try:
        result = session.execute(text("SELECT symbol, atr, lastPrice FROM bybit_tickers"))
        return [{"symbol": row[0], "atr": row[1], "lastPrice": row[2]} for row in result]
    finally:
        session.close()