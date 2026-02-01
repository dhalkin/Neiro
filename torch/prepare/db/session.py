from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

engine_charon = create_engine("mysql+mysqlconnector://root:rootpassword@localhost:3301/pluto")
Session_charon = sessionmaker(bind=engine_charon)
session = Session_charon()

def get_last_data_by_symbol(symbol: str, limit: int = 128):
    try:
        result = session.execute(text("SELECT * FROM bybit_tickers where symbol = :symbol order by created_at desc LIMIT :limit"), {"symbol": symbol, "limit": limit})
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