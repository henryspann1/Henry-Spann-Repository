import argparse
from typing import Dict, Tuple

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


def fetch_overview(ticker: str) -> Dict[str, float]:
    """Return basic stock information."""
    stock = yf.Ticker(ticker)
    info = stock.info or {}
    return {
        "symbol": info.get("symbol", ticker),
        "name": info.get("longName"),
        "price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "dividend_yield": info.get("dividendYield"),
    }


def plot_chart(ticker: str, period: str = "1y", interval: str = "1d") -> str:
    """Download historical prices and generate a line chart.

    Returns the file path of the saved chart.
    """
    hist = yf.download(ticker, period=period, interval=interval, progress=False)
    plt.figure(figsize=(10, 5))
    plt.plot(hist.index, hist["Close"], label="Close")
    plt.title(f"{ticker} Price History")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    filename = f"{ticker}_chart.png"
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    return filename


def trading_ratios(ticker: str) -> Dict[str, float]:
    """Compute simple trading ratios for optimization."""
    hist = yf.download(ticker, period="1y", interval="1d", progress=False)
    hist["MA50"] = hist["Close"].rolling(50).mean()
    hist["MA200"] = hist["Close"].rolling(200).mean()
    ma50 = float(hist["MA50"].iloc[-1])
    ma200 = float(hist["MA200"].iloc[-1])
    ratio = ma50 / ma200 if ma200 else np.nan
    return {"ma50": ma50, "ma200": ma200, "ma_ratio": ratio}


def risk_analysis(ticker: str) -> Dict[str, float]:
    """Perform basic risk analysis based on historical returns."""
    hist = yf.download(ticker, period="1y", interval="1d", progress=False)
    returns = hist["Close"].pct_change().dropna()
    volatility = float(returns.std() * np.sqrt(252))
    avg_return = float(returns.mean() * 252)
    sharpe = avg_return / volatility if volatility else np.nan
    return {"annual_return": avg_return, "volatility": volatility, "sharpe": sharpe}


def analyze_stock(ticker: str) -> Tuple[Dict[str, float], str, Dict[str, float], Dict[str, float]]:
    overview = fetch_overview(ticker)
    chart_file = plot_chart(ticker)
    ratios = trading_ratios(ticker)
    risk = risk_analysis(ticker)
    return overview, chart_file, ratios, risk


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple stock analysis tool")
    parser.add_argument("ticker", help="Stock ticker symbol, e.g., AAPL")
    args = parser.parse_args()

    overview, chart_file, ratios, risk = analyze_stock(args.ticker)

    print("Overview:")
    for key, value in overview.items():
        print(f"  {key}: {value}")

    print(f"\nChart saved to: {chart_file}")

    print("\nOptimization Ratios:")
    for key, value in ratios.items():
        print(f"  {key}: {value}")

    print("\nRisk Analysis:")
    for key, value in risk.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
