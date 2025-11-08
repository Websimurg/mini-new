#!/usr/bin/env python3
"""
Pinterest Growth Platform - Replit Demo Server
Simplified version for quick testing without database
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv

# Load environment
load_dotenv('backend/.env')

# Import services (simplified versions)
import openai
import requests
import json

app = FastAPI(
    title="Pinterest Growth Platform - Demo",
    version="1.0.0",
    description="AI-powered Pinterest automation demo"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# ============================================================================
# Models
# ============================================================================

class GenerateDescriptionRequest(BaseModel):
    topic: str
    keywords: List[str]
    tone: str = "engaging"
    length: str = "medium"

class GenerateTitleRequest(BaseModel):
    topic: str
    keywords: List[str]
    count: int = 5

class GenerateHashtagsRequest(BaseModel):
    topic: str
    keywords: List[str]
    count: int = 15

class ChatRequest(BaseModel):
    message: str
    conversation_history: Optional[List[dict]] = None

class CreateStrategyRequest(BaseModel):
    niche: str
    current_followers: int
    target_followers: int
    timeline_months: int

# ============================================================================
# AI Content Endpoints
# ============================================================================

@app.post("/api/v1/ai/generate/description")
async def generate_description(request: GenerateDescriptionRequest):
    """Generate SEO-optimized pin description"""
    try:
        keywords_str = ", ".join(request.keywords)

        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a Pinterest marketing expert."},
                {"role": "user", "content": f"""Write a Pinterest pin description for: "{request.topic}"

Requirements:
- Tone: {request.tone}
- Keywords: {keywords_str}
- SEO-optimized
- Include call-to-action
- Add relevant hashtags

Write only the description."""}
            ],
            temperature=0.7,
            max_tokens=300
        )

        description = response.choices[0].message.content.strip()
        return {"description": description}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/ai/generate/titles")
async def generate_titles(request: GenerateTitleRequest):
    """Generate multiple pin title options"""
    try:
        keywords_str = ", ".join(request.keywords)

        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a Pinterest title expert."},
                {"role": "user", "content": f"""Generate {request.count} catchy Pinterest titles for: "{request.topic}"

Keywords: {keywords_str}
Make them SEO-friendly and under 100 characters.
Return only titles, one per line."""}
            ],
            temperature=0.8,
            max_tokens=200
        )

        titles_text = response.choices[0].message.content.strip()
        titles = [t.strip('- ').strip() for t in titles_text.split('\n') if t.strip()]

        return {"titles": titles}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/ai/generate/hashtags")
async def generate_hashtags(request: GenerateHashtagsRequest):
    """Generate relevant hashtags"""
    try:
        keywords_str = ", ".join(request.keywords)

        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a Pinterest hashtag expert."},
                {"role": "user", "content": f"""Generate {request.count} relevant Pinterest hashtags for: "{request.topic}"

Keywords: {keywords_str}
Mix popular and niche hashtags.
Return hashtags with # symbol, comma-separated."""}
            ],
            temperature=0.7,
            max_tokens=150
        )

        hashtags_text = response.choices[0].message.content.strip()
        hashtags = [tag.strip() for tag in hashtags_text.replace('#', '').split(',')]
        hashtags = ['#' + tag for tag in hashtags if tag]

        return {"hashtags": hashtags}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/ai/trends/{niche}")
async def analyze_trends(niche: str):
    """Analyze trends in a niche"""
    try:
        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a Pinterest trends analyst."},
                {"role": "user", "content": f"""Analyze current Pinterest trends for: "{niche}"

Provide:
1. Top 5 trending topics
2. Popular content types
3. Best posting times
4. Recommended keywords

Return as JSON."""}
            ],
            temperature=0.7,
            max_tokens=500,
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============================================================================
# Chatbot CEO Endpoints
# ============================================================================

@app.post("/api/v1/chatbot/chat")
async def chat(request: ChatRequest):
    """Chat with CEO bot"""
    try:
        messages = [
            {"role": "system", "content": """You are a Pinterest growth expert CEO with 10+ years experience.
Provide actionable advice, growth strategies, and Pinterest tips in Turkish."""}
        ]

        if request.conversation_history:
            messages.extend(request.conversation_history)

        messages.append({"role": "user", "content": request.message})

        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )

        return {"response": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/chatbot/create-strategy")
async def create_strategy(request: CreateStrategyRequest):
    """Create growth strategy"""
    try:
        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a Pinterest growth strategist."},
                {"role": "user", "content": f"""Create a Pinterest growth strategy:

Niche: {request.niche}
Current: {request.current_followers} followers
Target: {request.target_followers} followers
Timeline: {request.timeline_months} months

Provide detailed strategy with milestones, content plan, and tactics.
Return as JSON."""}
            ],
            temperature=0.7,
            max_tokens=1500,
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============================================================================
# Pinterest API Endpoints (Demo data)
# ============================================================================

@app.get("/api/v1/pinterest/profile")
async def get_profile():
    """Get Pinterest profile (demo)"""
    try:
        access_token = os.getenv('PINTEREST_ACCESS_TOKEN')
        if not access_token:
            return {
                "username": "demo_user",
                "profile_url": "https://pinterest.com/demo",
                "follower_count": 1500,
                "note": "Demo data - configure PINTEREST_ACCESS_TOKEN for real data"
            }

        response = requests.get(
            "https://api.pinterest.com/v5/user_account",
            headers={"Authorization": f"Bearer {access_token}"}
        )

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Pinterest API error", "status": response.status_code}
    except Exception as e:
        return {"error": str(e), "note": "Using demo data"}

@app.get("/api/v1/pinterest/boards")
async def get_boards():
    """Get Pinterest boards (demo)"""
    return {
        "items": [
            {
                "id": "demo_board_1",
                "name": "Healthy Recipes",
                "description": "Delicious and healthy meal ideas",
                "pin_count": 245
            },
            {
                "id": "demo_board_2",
                "name": "Home Decor",
                "description": "Interior design inspiration",
                "pin_count": 189
            }
        ],
        "note": "Demo data - configure Pinterest API for real boards"
    }

# ============================================================================
# Static Files & Root
# ============================================================================

@app.get("/")
async def root():
    """Serve test.html"""
    return FileResponse('frontend/public/test.html')

@app.get("/health")
async def health():
    return {"status": "healthy", "message": "Pinterest Growth Platform Demo"}

# ============================================================================
# Run Server
# ============================================================================

if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8080))

    print("=" * 60)
    print("🚀 Pinterest Growth Platform - Demo Server")
    print("=" * 60)
    print(f"📍 Server: http://0.0.0.0:{port}")
    print(f"📚 API Docs: http://0.0.0.0:{port}/docs")
    print(f"🧪 Test UI: http://0.0.0.0:{port}/")
    print("=" * 60)

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )
