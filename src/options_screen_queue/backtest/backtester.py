import pandas as pd
import numpy as np


def backtest(
    df,
    hold_days=5,
    leverage=6,
    min_confidence=2
):
    """
    Simulate buying ATM options based on screener signals.

    Parameters:
    - df: DataFrame with Close, FinalSignal, Confidence
    - hold_days: how long to hold trade
    - leverage: option leverage multiplier
    - min_confidence: minimum stacked signal score to trade
    """

    trades = []

    for i in range(len(df) - hold_days):

        # Support both 'FinalSignal' (older code) and 'Signal' (current screener).
        signal = None
        if 'FinalSignal' in df.columns:
            signal = df['FinalSignal'].iloc[i]
        elif 'Signal' in df.columns:
            signal = df['Signal'].iloc[i]

        # Confidence may not exist; default to 1 so signals are traded.
        confidence = df['Confidence'].iloc[i] if 'Confidence' in df.columns else 1

        if signal is None or confidence < min_confidence:
            continue

        entry_price = df['Close'].iloc[i]
        exit_price = df['Close'].iloc[i + hold_days]

        underlying_return = (exit_price - entry_price) / entry_price

        # Approximate ATM delta
        delta = 0.5 if signal == "CALL" else -0.5

        option_return = delta * underlying_return * leverage

        trades.append({
            "EntryDate": df.index[i],
            "ExitDate": df.index[i + hold_days],
            "Signal": signal,
            "Confidence": confidence,
            "UnderlyingReturn": underlying_return,
            "OptionReturn": option_return
        })

    trades_df = pd.DataFrame(trades)

    if trades_df.empty:
        return trades_df, {}

    # Performance Metrics
    returns = trades_df["OptionReturn"]

    total_return = (1 + returns).prod() - 1
    sharpe = np.sqrt(252) * returns.mean() / returns.std()
    win_rate = (returns > 0).mean()
    max_dd = calculate_max_drawdown(returns)

    stats = {
        "Total Return": total_return,
        "Sharpe Ratio": sharpe,
        "Win Rate": win_rate,
        "Max Drawdown": max_dd,
        "Number of Trades": len(returns)
    }

    return trades_df, stats


def calculate_max_drawdown(returns):
    equity_curve = (1 + returns).cumprod()
    rolling_max = equity_curve.cummax()
    drawdown = equity_curve / rolling_max - 1
    return drawdown.min()
