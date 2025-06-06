# backend/supabase_client.py
# Provides a helper to create the Supabase client.
# No direct DB operations are implemented here.

from supabase import create_client, Client
import os

def create_supabase_client() -> Client:
    """Return an authenticated Supabase client."""
    url = os.getenv('SUPABASE_URL', '')
    key = os.getenv('SUPABASE_KEY', '')
    return create_client(url, key)
