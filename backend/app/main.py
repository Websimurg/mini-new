from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from app.core.config import settings
from app.api.endpoints import (
    auth,
    pinterest,
    pins,
    boards,
    content_plans,
    scheduler,
    ai_content,
    analytics,
    chatbot
)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Pinterest Growth Platform - All-in-one Pinterest automation and growth tool",
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=1000)

# Routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(pinterest.router, prefix="/api/v1/pinterest", tags=["Pinterest"])
app.include_router(pins.router, prefix="/api/v1/pins", tags=["Pins"])
app.include_router(boards.router, prefix="/api/v1/boards", tags=["Boards"])
app.include_router(content_plans.router, prefix="/api/v1/content-plans", tags=["Content Planning"])
app.include_router(scheduler.router, prefix="/api/v1/scheduler", tags=["Scheduler"])
app.include_router(ai_content.router, prefix="/api/v1/ai", tags=["AI Content Generation"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["Analytics"])
app.include_router(chatbot.router, prefix="/api/v1/chatbot", tags=["Chatbot CEO"])

@app.get("/")
async def root():
    return {
        "message": "Pinterest Growth Platform API",
        "version": settings.APP_VERSION,
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
