from supabase import Client, create_client
from config import api, url

api_url: str = url
key: str = api

def create_supabase_client():
    supabase: Client = create_client(url, key)
    return supabase