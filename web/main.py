from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import subprocess
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

SNAPSHOT_LOG = Path("../rust_runtime/snapshots.jsonl")  # Adjust path if needed

# 🧠 Utility to load latest snapshot per agent
def load_latest_snapshot():
    if not SNAPSHOT_LOG.exists():
        return {}

    lines = [json.loads(line) for line in SNAPSHOT_LOG.read_text().splitlines() if line.strip()]
    latest = {}
    for entry in lines:
        agent = entry.get("agent", "snapshot_crypto")
        latest[agent] = entry
    return latest

# 🏠 Dashboard route
@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    data = load_latest_snapshot()
    return templates.TemplateResponse("dashboard.html", {"request": request, "data": data})

# 🟢 Trigger agent orchestrator (calls ./run_all.sh)
@app.post("/run")
async def run_agents():
    subprocess.run(["bash", "../run_all.sh"])
    return RedirectResponse(url="/", status_code=303)
