import requests
import sys
from datetime import datetime, timezone
import json

OUTPUT_FILE = "snapshots.jsonl"

def run():
    print("[AGENT] Fetching Fear & Greed Index...", flush=True)

    url = "https://api.alternative.me/fng/"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    index = data["data"][0]

    snapshot = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "agent": "fear_greed_fetcher",
        "data": {
            "score": index["value"],
            "classification": index["value_classification"]
        }
    }

    with open(OUTPUT_FILE, "a") as f:
        f.write(json.dumps(snapshot) + "\n")

    print("[AGENT] fear_greed_fetcher complete", flush=True)

if __name__ == "__main__":
    try:
        run()
        sys.exit(0)
    except Exception as e:
        print(f"[AGENT ERROR] {e}", flush=True)
        sys.exit(1)
