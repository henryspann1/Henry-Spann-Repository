# Stock Analysis Tool

This repository includes a simple command-line stock analysis script located at `SpannCapital/stock_analysis.py`.
It fetches basic company information, generates a price chart, computes moving average ratios and runs a small risk analysis for a given ticker symbol.

## Setup

1. Ensure Python 3 is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with a stock ticker symbol:

```bash
python SpannCapital/stock_analysis.py AAPL
```

The script prints four sections:

1. **Overview** – current price, market cap, P/E ratio, etc.
2. **Chart** – saves `<TICKER>_chart.png` in the current directory.
3. **Optimization Ratios** – 50/200-day moving averages and their ratio.
4. **Risk Analysis** – annualized return, volatility, and Sharpe ratio.

You can replace `AAPL` with any ticker supported by Yahoo Finance.
