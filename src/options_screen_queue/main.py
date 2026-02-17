# main.py

from .data.loader import load_data
from .indicators.signals import add_indicators
from .screener.screener import generate_signal
from .backtest.backtester import backtest


def main():
	df = load_data("SPY", "2018-01-01", "2024-01-01")
	df = add_indicators(df)
	df = generate_signal(df)

	trades, stats = backtest(df, min_confidence=1)

	print("Backtest stats:")
	print(stats)

	if not trades.empty:
		print(f"First 5 trades:\n{trades.head()}")


if __name__ == "__main__":
	main()