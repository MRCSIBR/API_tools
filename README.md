# Crypto Price Fetcher

A Python tool to fetch real-time prices for Bitcoin (BTC), Ethereum (ETH), and Ripple (XRP) against USD using the CoinGecko API.

## Features

- Fetches current prices for BTC/USD, ETH/USD, and XRP/USD
- Real-time data with last update timestamp
- Error handling for network issues and API failures
- Formatted output with appropriate decimal places
- No API key required (uses free public endpoint)
- Timeout protection (10 seconds)
- UTC timestamp display

## Requirements

- Python 3.6+
- `requests` library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/crypto-price-fetcher.git
cd crypto-price-fetcher
