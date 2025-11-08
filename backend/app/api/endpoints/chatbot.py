"""
Chatbot CEO Endpoints
"""
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional, Dict
from pydantic import BaseModel
from app.services.ai.chatbot_ceo import chatbot_ceo

router = APIRouter()

class ChatMessage(BaseModel):
    role: str  # "user" or "assistant"
    content: str

class ChatRequest(BaseModel):
    message: str
    conversation_history: Optional[List[ChatMessage]] = None
    user_context: Optional[Dict] = None

class AnalyzePerformanceRequest(BaseModel):
    analytics_data: Dict

class CreateStrategyRequest(BaseModel):
    niche: str
    current_followers: int
    target_followers: int
    timeline_months: int

class ReviewContentRequest(BaseModel):
    pin_title: str
    pin_description: str
    niche: str

class DailyTasksRequest(BaseModel):
    user_context: Dict

@router.post("/chat")
async def chat(request: ChatRequest):
    """Chat with CEO bot"""
    try:
        # Convert conversation history to dict format
        history = None
        if request.conversation_history:
            history = [
                {"role": msg.role, "content": msg.content}
                for msg in request.conversation_history
            ]

        response = await chatbot_ceo.chat(
            user_message=request.message,
            conversation_history=history,
            user_context=request.user_context
        )

        return {
            "response": response,
            "timestamp": "2024-01-01T00:00:00Z"  # Add actual timestamp
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyze-performance")
async def analyze_performance(request: AnalyzePerformanceRequest):
    """Analyze Pinterest performance and get insights"""
    try:
        analysis = await chatbot_ceo.analyze_performance(
            analytics_data=request.analytics_data
        )
        return analysis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/create-strategy")
async def create_growth_strategy(request: CreateStrategyRequest):
    """Create a comprehensive growth strategy"""
    try:
        strategy = await chatbot_ceo.create_growth_strategy(
            niche=request.niche,
            current_followers=request.current_followers,
            target_followers=request.target_followers,
            timeline_months=request.timeline_months
        )
        return strategy
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/review-content")
async def review_content(request: ReviewContentRequest):
    """Review and score pin content"""
    try:
        review = await chatbot_ceo.review_content(
            pin_title=request.pin_title,
            pin_description=request.pin_description,
            niche=request.niche
        )
        return review
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/daily-tasks")
async def get_daily_tasks(request: DailyTasksRequest):
    """Get suggested daily tasks"""
    try:
        tasks = await chatbot_ceo.suggest_daily_tasks(
            user_context=request.user_context
        )
        return {"tasks": tasks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ask")
async def ask_question(
    question: str,
    context: Optional[Dict] = None
):
    """Ask a Pinterest-related question"""
    try:
        answer = await chatbot_ceo.answer_question(
            question=question,
            context=context
        )
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
