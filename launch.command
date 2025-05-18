#!/bin/bash

# Ensure we start from the project root
cd "$(dirname "$0")"

# Move into the FastAPI web folder
cd web || {
  echo "❌ Could not find web/ directory."
  exit 1
}

# Launch the FastAPI dashboard
echo "🚀 Launching Crypto Dashboard at http://localhost:8000 ..."
uvicorn main:app --reload
