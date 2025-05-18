#!/bin/bash

# Move to the directory containing this script
cd "$(dirname "$0")"

echo "📁 Moving into orchestrator folder..."
cd rust_runtime || { echo "❌ Failed to cd into rust_runtime"; exit 1; }

# Clear previous snapshot log
> snapshots.jsonl

echo "🛠️  Running Rust Orchestrator..."
cargo run || { echo "❌ Rust orchestration failed"; exit 1; }

echo ""
echo "🎨 Launching Snapshot Viewer..."
python3 view_snapshots.py || { echo "❌ Viewer failed"; exit 1; }
