"""
AI Content Generator Service
Handles all AI-powered content generation (ContentGoblin features)
"""
from typing import Optional, Dict, List
import openai
from anthropic import Anthropic
from app.core.config import settings
import json

class AIContentGenerator:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        if settings.ANTHROPIC_API_KEY:
            self.anthropic_client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        else:
            self.anthropic_client = None

    async def generate_pin_description(
        self,
        topic: str,
        keywords: List[str],
        tone: str = "engaging",
        length: str = "medium"
    ) -> str:
        """Generate SEO-optimized pin description"""

        keywords_str = ", ".join(keywords)

        prompt = f"""Write a Pinterest pin description for the topic: "{topic}"

Requirements:
- Tone: {tone}
- Length: {length} (100-200 words)
- Include these keywords naturally: {keywords_str}
- Make it SEO-optimized and engaging
- Include a call-to-action
- Add relevant hashtags at the end

Write only the description, nothing else."""

        response = self.openai_client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a Pinterest marketing expert. You create engaging, SEO-optimized pin descriptions."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )

        return response.choices[0].message.content.strip()

    async def generate_pin_title(
        self,
        topic: str,
        keywords: List[str],
        count: int = 5
    ) -> List[str]:
        """Generate multiple pin title options"""

        keywords_str = ", ".join(keywords)

        prompt = f"""Generate {count} catchy Pinterest pin titles for: "{topic}"

Requirements:
- Include keywords: {keywords_str}
- Keep titles under 100 characters
- Make them click-worthy and SEO-friendly
- Use power words and numbers when appropriate

Return only the titles, one per line."""

        response = self.openai_client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a Pinterest title expert. Create attention-grabbing, SEO-optimized titles."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=200
        )

        titles = response.choices[0].message.content.strip().split('\n')
        return [title.strip('- ').strip() for title in titles if title.strip()]

    async def generate_hashtags(
        self,
        topic: str,
        keywords: List[str],
        count: int = 15
    ) -> List[str]:
        """Generate relevant hashtags"""

        keywords_str = ", ".join(keywords)

        prompt = f"""Generate {count} relevant Pinterest hashtags for: "{topic}"

Keywords: {keywords_str}

Requirements:
- Mix of popular and niche hashtags
- Relevant to the topic
- No spaces in hashtags
- Return only hashtags with # symbol, comma-separated"""

        response = self.openai_client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a Pinterest hashtag expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )

        hashtags_text = response.choices[0].message.content.strip()
        hashtags = [tag.strip() for tag in hashtags_text.replace('#', '').split(',')]
        return ['#' + tag for tag in hashtags if tag]

    async def analyze_trends(
        self,
        niche: str
    ) -> Dict:
        """Analyze current trends in a niche"""

        prompt = f"""Analyze current Pinterest trends for the niche: "{niche}"

Provide:
1. Top 5 trending topics
2. Popular content types (video, infographic, etc.)
3. Best posting times
4. Recommended keywords
5. Content ideas

Return as JSON format."""

        response = self.openai_client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a Pinterest trends analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500,
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)

    async def generate_content_ideas(
        self,
        niche: str,
        count: int = 10
    ) -> List[Dict]:
        """Generate content ideas for a niche"""

        prompt = f"""Generate {count} Pinterest content ideas for the niche: "{niche}"

For each idea provide:
- Title
- Description
- Target keywords
- Pin type (image, video, infographic)
- Difficulty (easy, medium, hard)

Return as JSON array."""

        response = self.openai_client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a Pinterest content strategist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=1000,
            response_format={"type": "json_object"}
        )

        result = json.loads(response.choices[0].message.content)
        return result.get("ideas", [])

    async def optimize_existing_content(
        self,
        title: str,
        description: str
    ) -> Dict:
        """Optimize existing pin content"""

        prompt = f"""Optimize this Pinterest pin content:

Title: {title}
Description: {description}

Provide:
1. Improved title (SEO-optimized)
2. Improved description (SEO-optimized)
3. Suggested keywords
4. Suggested hashtags
5. Improvement notes

Return as JSON format."""

        response = self.openai_client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a Pinterest SEO expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=600,
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)

    async def generate_image_prompt(
        self,
        topic: str,
        style: str = "modern"
    ) -> str:
        """Generate image generation prompt for DALL-E or Stable Diffusion"""

        prompt = f"""Create a detailed image generation prompt for a Pinterest pin about: "{topic}"

Style: {style}
Requirements:
- Vertical orientation (1000x1500px ideal)
- Eye-catching and vibrant
- Include text overlay space
- Professional quality

Write only the detailed image prompt."""

        response = self.openai_client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are an expert at creating prompts for AI image generation."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=200
        )

        return response.choices[0].message.content.strip()

ai_content_generator = AIContentGenerator()
