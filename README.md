# 🧠 Crypto Agent Runtime Dashboard

A real-time backend system that fetches live cryptocurrency data and market sentiment using Python agents, orchestrated by Rust, and displayed via a FastAPI web dashboard.

---

## 🚀 Features

- 🦀 **Rust orchestrator** runs Python agents concurrently with retries
- 🐍 **Python agents** fetch:
  - ✅ Live crypto prices from CoinGecko
  - ✅ Fear & Greed Index from alternative.me
- 🌐 **FastAPI web dashboard** shows live data via a clean HTML interface
- 🔁 **One-click launcher** for macOS
- 📊 Structured logging via newline-delimited JSON (`snapshots.jsonl`)

---

## 📁 Folder Structure

agent_runtime/
├── rust_runtime/
│   ├── python_agents/
│   │   ├── snapshot_crypto.py
│   │   └── fear_greed_fetcher.py
│   ├── src/
│   │   └── main.rs
│   ├── Cargo.toml
│   ├── Cargo.lock
│   ├── run_all.sh
│   └── snapshots.jsonl
├── web/
│   ├── main.py
│   └── templates/
│       └── dashboard.html
├── requirements.txt
├── README.md
└── launch.command

## 🛠️ Setup & Usage

Follow these steps to install dependencies, run the project, and view your live dashboard.

---

### 1️⃣ Install Python Dependencies

From the root directory (`agent_runtime/`), run:

```bash
pip install -r requirements.txt
```
# **This installs:

- fastapi – the web server framework

- uvicorn – the ASGI server to run FastAPI

- jinja2 – template engine for HTML rendering

- requests – for API calls in the Python agents

Launch the Web Dashboard

```bash
./launch.command
```

# **This will

- Navigate to the web app folder

- Launch the FastAPI server

- Open the dashboard at http://localhost:8000

### 3️⃣ Trigger Agents via Dashboard

Once you're on the dashboard:

- Click the **“Run Snapshot”** button

This will:

- 🦀 Run the **Rust orchestrator**
- 🐍 Launch all **Python agents in parallel**
- 📄 Log output to `snapshots.jsonl`
- 📊 Display the latest results directly in the dashboard

✅ You now have a **live crypto monitoring system** powered by Rust and Python.
