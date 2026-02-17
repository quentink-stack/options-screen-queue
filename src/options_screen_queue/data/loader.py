import yfinance as yf
import pandas as pd


def load_data(ticker, start, end):
    """Download OHLCV data and normalize columns for single-ticker use.

    yfinance can return a MultiIndex columns (e.g., when multiple tickers are
    requested). This function flattens the columns to simple names and returns
    a cleaned DataFrame with Open/High/Low/Close/Volume.
    """
    df = yf.download(ticker, start=start, end=end)

    # If yfinance returned MultiIndex columns (Ticker, Field), drop the top level
    if isinstance(df.columns, pd.MultiIndex):
        # keep only the first level (Open/High/Low/Close/Volume)
        df.columns = df.columns.get_level_values(0)

    # select and clean
    df = df[["Open", "High", "Low", "Close", "Volume"]]
    df.dropna(inplace=True)
    return df
