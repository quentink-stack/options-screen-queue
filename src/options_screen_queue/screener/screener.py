# screener/screener.py

def generate_signal(df):
    signals = []

    for i in range(len(df)):
        row = df.iloc[i]

        if (
            row['Close'] > row['MA200'] and
            row['RSI'] < 40 and
            row['Momentum'] > 0
        ):
            signals.append("CALL")

        elif (
            row['Close'] < row['MA200'] and
            row['RSI'] > 60 and
            row['Momentum'] < 0
        ):
            signals.append("PUT")

        else:
            signals.append(None)

    df['Signal'] = signals
    return df
