# indicators/signals.py
import pandas as pd
import numpy as np

def add_indicators(df):
    df['MA50'] = df['Close'].rolling(50).mean()
    df['MA200'] = df['Close'].rolling(200).mean()

    # RSI
    delta = df['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))

    # Momentum
    df['Momentum'] = df['Close'] / df['Close'].shift(20) - 1

    # Realized Vol
    returns = np.log(df['Close'] / df['Close'].shift(1))
    df['RealizedVol'] = returns.rolling(30).std() * np.sqrt(252)

    return df
