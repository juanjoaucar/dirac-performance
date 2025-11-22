import streamlit as st
import requests
from datetime import datetime, timedelta, timezone
from supabase import create_client, Client

# --- Get IP ---
def get_ip():
    try:
        return requests.get("https://api64.ipify.org?format=json").json()["ip"]
    except:
        return "0.0.0.0"

# --- Get country ---
def get_country(ip):
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        return data.get("country", "Unknown")
    except:
        return "Unknown"


# ---------- MAIN ----------
def register_visitor():
    # --- Supabase client ---
    SUPABASE_URL = st.secrets["supabase_url"]
    SUPABASE_KEY = st.secrets["supabase_anon_key"]
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


    ip = get_ip()
    country = get_country(ip)

    # ---- Check last visit from this IP ----
    result = (
        supabase.table("visits")
        .select("timestamp")
        .eq("ip", ip)
        .order("timestamp", desc=True)
        .limit(1)
        .execute()
    )

    should_register = False

    if not result.data:
        # No previous visits ⇒ register
        should_register = True
    else:
        last_ts = datetime.fromisoformat(result.data[0]["timestamp"].replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)

        # Was the last visit more than 1 day ago?
        if last_ts.date() < now.date():
            should_register = True

    # ---- Record visit if needed ----
    if should_register:
        supabase.table("visits").insert({"ip": ip, "country": country}).execute()

    # ---- Count total visits ----
    total_visits = supabase.table("visits").select("id", count="exact").execute().count


    return total_visits, country