"""
Pinterest API Service
Handles all Pinterest API interactions (PinClicks features)
"""
from typing import Optional, Dict, List
import requests
from datetime import datetime, timedelta
from app.core.config import settings

class PinterestService:
    BASE_URL = "https://api.pinterest.com/v5"

    def __init__(self, access_token: str):
        self.access_token = access_token
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

    async def get_user_profile(self) -> Dict:
        """Get authenticated user's profile"""
        url = f"{self.BASE_URL}/user_account"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    async def get_boards(self, page_size: int = 25) -> List[Dict]:
        """Get user's boards"""
        url = f"{self.BASE_URL}/boards"
        params = {"page_size": page_size}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json().get("items", [])

    async def create_board(
        self,
        name: str,
        description: str = "",
        privacy: str = "PUBLIC"
    ) -> Dict:
        """Create a new board"""
        url = f"{self.BASE_URL}/boards"
        data = {
            "name": name,
            "description": description,
            "privacy": privacy
        }
        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    async def create_pin(
        self,
        board_id: str,
        title: str,
        description: str,
        image_url: str,
        link: Optional[str] = None,
        alt_text: Optional[str] = None
    ) -> Dict:
        """Create a new pin"""
        url = f"{self.BASE_URL}/pins"

        data = {
            "board_id": board_id,
            "title": title,
            "description": description,
            "media_source": {
                "source_type": "image_url",
                "url": image_url
            }
        }

        if link:
            data["link"] = link

        if alt_text:
            data["alt_text"] = alt_text

        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    async def upload_pin_with_media(
        self,
        board_id: str,
        title: str,
        description: str,
        image_bytes: bytes,
        link: Optional[str] = None,
        alt_text: Optional[str] = None
    ) -> Dict:
        """Upload pin with media file"""
        url = f"{self.BASE_URL}/pins"

        files = {
            "media": ("pin_image.png", image_bytes, "image/png")
        }

        data = {
            "board_id": board_id,
            "title": title,
            "description": description,
        }

        if link:
            data["link"] = link

        if alt_text:
            data["alt_text"] = alt_text

        # Note: Pinterest API v5 requires multipart/form-data for media upload
        headers = {
            "Authorization": f"Bearer {self.access_token}",
        }

        response = requests.post(url, headers=headers, data=data, files=files)
        response.raise_for_status()
        return response.json()

    async def get_pin(self, pin_id: str) -> Dict:
        """Get pin details"""
        url = f"{self.BASE_URL}/pins/{pin_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    async def delete_pin(self, pin_id: str) -> bool:
        """Delete a pin"""
        url = f"{self.BASE_URL}/pins/{pin_id}"
        response = requests.delete(url, headers=self.headers)
        response.raise_for_status()
        return True

    async def get_analytics(
        self,
        start_date: datetime,
        end_date: datetime,
        metric_types: List[str] = None
    ) -> Dict:
        """Get account analytics"""
        if metric_types is None:
            metric_types = ["IMPRESSION", "SAVE", "PIN_CLICK", "OUTBOUND_CLICK"]

        url = f"{self.BASE_URL}/user_account/analytics"
        params = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "metric_types": ",".join(metric_types)
        }

        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    async def get_pin_analytics(
        self,
        pin_id: str,
        start_date: datetime,
        end_date: datetime
    ) -> Dict:
        """Get specific pin analytics"""
        url = f"{self.BASE_URL}/pins/{pin_id}/analytics"
        params = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "metric_types": "IMPRESSION,SAVE,PIN_CLICK,OUTBOUND_CLICK"
        }

        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    async def search_pins(self, query: str, limit: int = 20) -> List[Dict]:
        """Search pins (for trend research)"""
        # Note: Search API might be limited based on your Pinterest API access
        url = f"{self.BASE_URL}/search/pins"
        params = {
            "query": query,
            "limit": limit
        }

        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json().get("items", [])

    async def get_board_pins(self, board_id: str, page_size: int = 25) -> List[Dict]:
        """Get all pins from a board"""
        url = f"{self.BASE_URL}/boards/{board_id}/pins"
        params = {"page_size": page_size}

        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json().get("items", [])

    async def follow_user(self, username: str) -> Dict:
        """Follow a user (automation feature)"""
        # Note: Following features might be restricted
        url = f"{self.BASE_URL}/user_account/following"
        data = {"username": username}

        response = requests.post(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    async def get_trending_topics(self, region: str = "US") -> List[Dict]:
        """Get trending topics (for content ideas)"""
        # This is a conceptual endpoint - Pinterest API may not have this exact endpoint
        # You might need to use third-party services or web scraping
        url = f"{self.BASE_URL}/trends"
        params = {"region": region}

        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json().get("trends", [])
        except:
            # Fallback: return empty list if endpoint doesn't exist
            return []

def create_pinterest_service(access_token: str) -> PinterestService:
    """Factory function to create Pinterest service"""
    return PinterestService(access_token)
