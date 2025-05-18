import requests
import time
import sys
from datetime import datetime, timezone
import json

OUTPUT_FILE = "snapshots.jsonl"

def run():
    print("[AGENT] Fetching top crypto prices...", flush=True)

    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 5,
        "page": 1,
        "sparkline": "false"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    snapshot = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "agent": "snapshot_crypto",
        "data": [  # <--- wrap your coin list inside "data"
            {"name": coin["name"], "symbol": coin["symbol"], "price": coin["current_price"]}
            for coin in data
        ]
    }

    with open(OUTPUT_FILE, "a") as f:
        f.write(json.dumps(snapshot) + "\n")

    print(f"[AGENT] snapshot_crypto complete", flush=True)

if __name__ == "__main__":
    try:
        run()
        sys.exit(0)
    except Exception as e:
        print(f"[AGENT ERROR] {e}", flush=True)
        sys.exit(1)


    
    
