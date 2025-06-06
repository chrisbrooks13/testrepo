# backend/main.py
# Starts a FastAPI server with a simple healthcheck route.
# Does not contain business logic; only demo endpoints.

from fastapi import FastAPI
from supabase import create_client, Client
import os

app = FastAPI()

# create Supabase client using env vars
SUPABASE_URL = os.getenv('SUPABASE_URL', '')
SUPABASE_KEY = os.getenv('SUPABASE_KEY', '')

def get_client() -> Client:
    """Return an authenticated Supabase client."""
    return create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/health")
def health():
    """Simple healthcheck endpoint."""
    return {"status": "ok"}

