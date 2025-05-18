# 🧠 Crypto Agent Runtime Dashboard

A real-time backend system that fetches live cryptocurrency data and market sentiment using Python agents, orchestrated by Rust, and displayed via a FastAPI web dashboard.

## 📋 Project Overview

This project is designed to provide real-time insights into cryptocurrency markets by leveraging the power of Python agents for data fetching and Rust for orchestration. The system fetches live cryptocurrency prices from CoinGecko and the Fear & Greed Index from alternative.me, presenting the data through a clean and intuitive FastAPI web dashboard.

## 🚀 Features

- 🦀 **Rust Orchestrator**: Efficiently runs Python agents concurrently with retry mechanisms, ensuring robust data collection.
- 🐍 **Python Agents**: Fetch live cryptocurrency prices and market sentiment data, providing real-time insights.
- 🌐 **FastAPI Web Dashboard**: Displays live data through a clean and responsive HTML interface, making it easy to monitor market trends.
- 🔁 **One-Click Launcher**: Simplifies the process of starting the system on macOS, ensuring a seamless user experience.
- 📊 **Structured Logging**: Utilizes newline-delimited JSON (`snapshots.jsonl`) for organized and accessible logging.

## 📁 Folder Structure

```
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
```

## 🛠️ Setup & Usage

### 1️⃣ Install Python Dependencies

From the root directory (`agent_runtime/`), run:

```bash
pip install -r requirements.txt
```

This installs:
- **fastapi**: The web server framework.
- **uvicorn**: The ASGI server to run FastAPI.
- **jinja2**: Template engine for HTML rendering.
- **requests**: For API calls in the Python agents.

### 2️⃣ Launch the Web Dashboard

```bash
./launch.command
```

This will:
- Navigate to the web app folder.
- Launch the FastAPI server.
- Open the dashboard at [http://localhost:8000](http://localhost:8000).

### 3️⃣ Trigger Agents via Dashboard

Once you're on the dashboard:
- Click the **"Run Snapshot"** button.

This will:
- 🦀 Run the **Rust orchestrator**.
- 🐍 Launch all **Python agents in parallel**.
- 📄 Log output to `snapshots.jsonl`.
- 📊 Display the latest results directly in the dashboard.

✅ You now have a **live crypto monitoring system** powered by Rust and Python.

## 🤝 Contributing

We welcome contributions! If you have suggestions or improvements, please feel free to submit a pull request or open an issue.

---
