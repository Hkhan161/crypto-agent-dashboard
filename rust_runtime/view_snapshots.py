import json
from pathlib import Path

# Path to the shared snapshot log (reset every orchestrator run)
LOG_FILE = "snapshots.jsonl"

# 📥 Load all lines from the snapshot log into memory
def load_snapshots():
    path = Path(LOG_FILE)
    if not path.exists():
        print(f"[VIEWER] No log file found: {LOG_FILE}")
        return []

    # Each line is a JSON object (agent output)
    with path.open() as f:
        return [json.loads(line) for line in f if line.strip()]

# 🪙 Display latest crypto price snapshot (from snapshot_crypto.py)
def show_latest_crypto(snapshot):
    print("\n🪙 Latest Crypto Prices")
    print("-" * 40)
    print(f"{'Name':<12} {'Symbol':<8} {'Price (USD)':>12}")
    print("-" * 40)
    for coin in snapshot["data"]:
        print(f"{coin['name']:<12} {coin['symbol'].upper():<8} {coin['price']:>12,.2f}")
    print("-" * 40)

# 😱 Display sentiment info (from fear_greed_fetcher.py)
def show_latest_sentiment(snapshot):
    data = snapshot["data"]
    print("\n😱 Crypto Sentiment")
    print("-" * 40)
    print(f"Classification: {data['classification']}")
    print(f"Score:         {data['score']} / 100")
    print("-" * 40)

# 🧠 Main CLI entry point
def main():
    snapshots = load_snapshots()
    if not snapshots:
        return

    # Create a map of agent name → most recent entry
    latest = {}
    for entry in snapshots:
        agent = entry.get("agent", "snapshot_crypto")  # fallback for legacy format
        latest[agent] = entry

    # Display results by agent
    if "snapshot_crypto" in latest:
        show_latest_crypto(latest["snapshot_crypto"])
    if "fear_greed_fetcher" in latest:
        show_latest_sentiment(latest["fear_greed_fetcher"])

# 🚀 Run it
if __name__ == "__main__":
    main()
