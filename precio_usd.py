import requests
import time

def fetch_crypto_prices():
    """Fetch current prices for BTC, ETH, and XRP in USD"""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum,ripple',
        'vs_currencies': 'usd',
        'include_last_updated_at': 'true'
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        
        # Extract prices and timestamps
        prices = {
            'BTCUSD': data['bitcoin']['usd'],
            'ETHUSD': data['ethereum']['usd'],
            'XRPUSD': data['ripple']['usd']
        }
        last_updated = data['bitcoin']['last_updated_at']
        
        return prices, last_updated
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None, None
    except KeyError as e:
        print(f"Unexpected data format. Missing key: {e}")
        return None, None

def main():
    print("Fetching cryptocurrency prices...")
    prices, timestamp = fetch_crypto_prices()
    
    if prices:
        print("\nCurrent Prices (USD):")
        print(f"BTC/USD: ${prices['BTCUSD']:,.2f}")
        print(f"ETH/USD: ${prices['ETHUSD']:,.2f}")
        print(f"XRP/USD: ${prices['XRPUSD']:,.4f}")
        
        # Convert timestamp to readable format
        updated_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(timestamp))
        print(f"\nLast updated: {updated_time} UTC")
    else:
        print("Failed to retrieve prices. Please try again later.")

if __name__ == "__main__":
    main()
