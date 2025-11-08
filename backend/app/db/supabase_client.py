"""
Supabase Client Configuration
Alternative/Additional database option
"""
from supabase import create_client, Client
from app.core.config import settings
from typing import Optional

class SupabaseClient:
    """Supabase database client wrapper"""

    _instance: Optional[Client] = None

    @classmethod
    def get_client(cls) -> Client:
        """Get or create Supabase client singleton"""
        if cls._instance is None:
            if not settings.SUPABASE_URL or not settings.SUPABASE_ANON_KEY:
                raise ValueError("Supabase credentials not configured")

            cls._instance = create_client(
                settings.SUPABASE_URL,
                settings.SUPABASE_ANON_KEY
            )

        return cls._instance

    @classmethod
    def is_configured(cls) -> bool:
        """Check if Supabase is configured"""
        return bool(settings.SUPABASE_URL and settings.SUPABASE_ANON_KEY)

# Create global instance
try:
    supabase_client = SupabaseClient.get_client() if SupabaseClient.is_configured() else None
except Exception:
    supabase_client = None

def get_supabase() -> Client:
    """Dependency for getting Supabase client"""
    if supabase_client is None:
        raise ValueError("Supabase not configured")
    return supabase_client
