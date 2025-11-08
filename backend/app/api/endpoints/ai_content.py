"""
AI Content Generation Endpoints
"""
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from app.services.ai.content_generator import ai_content_generator
from app.services.ai.image_generator import ai_image_generator
from app.services.ai.fal_image_generator import fal_image_generator

router = APIRouter()

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

class GenerateImageRequest(BaseModel):
    prompt: str
    add_text: Optional[str] = None
    text_position: str = "center"
    use_fal: bool = True  # Use Fal.ai by default
    style: Optional[str] = "modern"

class OptimizeContentRequest(BaseModel):
    title: str
    description: str

class ContentIdeasRequest(BaseModel):
    niche: str
    count: int = 10

@router.post("/generate/description")
async def generate_description(request: GenerateDescriptionRequest):
    """Generate SEO-optimized pin description"""
    try:
        description = await ai_content_generator.generate_pin_description(
            topic=request.topic,
            keywords=request.keywords,
            tone=request.tone,
            length=request.length
        )
        return {"description": description}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate/titles")
async def generate_titles(request: GenerateTitleRequest):
    """Generate multiple pin title options"""
    try:
        titles = await ai_content_generator.generate_pin_title(
            topic=request.topic,
            keywords=request.keywords,
            count=request.count
        )
        return {"titles": titles}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate/hashtags")
async def generate_hashtags(request: GenerateHashtagsRequest):
    """Generate relevant hashtags"""
    try:
        hashtags = await ai_content_generator.generate_hashtags(
            topic=request.topic,
            keywords=request.keywords,
            count=request.count
        )
        return {"hashtags": hashtags}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate/image")
async def generate_image(request: GenerateImageRequest):
    """Generate pin image using AI (Fal.ai or DALL-E)"""
    try:
        # Generate image using selected service
        if request.use_fal:
            # Use Fal.ai (faster and cheaper)
            if request.style:
                image_bytes = await fal_image_generator.generate_with_style(
                    prompt=request.prompt,
                    style=request.style
                )
            else:
                image_bytes = await fal_image_generator.generate_pin_image(
                    prompt=request.prompt
                )
        else:
            # Use DALL-E (OpenAI)
            image_bytes = await ai_image_generator.generate_pin_image_dalle(
                prompt=request.prompt
            )

        # Add text overlay if requested
        if request.add_text:
            image_bytes = await ai_image_generator.add_text_overlay(
                image_bytes=image_bytes,
                text=request.add_text,
                position=request.text_position
            )

        # In production, upload to S3/Cloudinary and return URL
        # For now, return base64
        import base64
        image_base64 = base64.b64encode(image_bytes).decode()

        return {
            "image": f"data:image/png;base64,{image_base64}",
            "message": "Image generated successfully",
            "generator": "fal.ai" if request.use_fal else "dall-e-3"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/optimize")
async def optimize_content(request: OptimizeContentRequest):
    """Optimize existing pin content"""
    try:
        optimized = await ai_content_generator.optimize_existing_content(
            title=request.title,
            description=request.description
        )
        return optimized
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ideas")
async def generate_content_ideas(request: ContentIdeasRequest):
    """Generate content ideas for a niche"""
    try:
        ideas = await ai_content_generator.generate_content_ideas(
            niche=request.niche,
            count=request.count
        )
        return {"ideas": ideas}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/trends/{niche}")
async def analyze_trends(niche: str):
    """Analyze current trends in a niche"""
    try:
        trends = await ai_content_generator.analyze_trends(niche=niche)
        return trends
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
