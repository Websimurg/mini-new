"""
Chatbot CEO Service
AI-powered Pinterest growth advisor and strategy consultant
"""
from typing import List, Dict, Optional
import openai
from anthropic import Anthropic
from app.core.config import settings
import json
from datetime import datetime

class ChatbotCEO:
    """
    AI Chatbot CEO - Your Pinterest Growth Strategist
    Provides personalized advice, analytics interpretation, and growth strategies
    """

    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        if settings.ANTHROPIC_API_KEY:
            self.anthropic_client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        else:
            self.anthropic_client = None

        self.system_prompt = """You are the CEO of a Pinterest growth agency with 10+ years of experience.
You're an expert in:
- Pinterest algorithm and SEO
- Content strategy and planning
- Visual marketing and design
- Analytics and growth metrics
- Automation and scheduling strategies
- Niche targeting and audience building

Your role is to:
1. Analyze user's Pinterest performance
2. Provide actionable growth strategies
3. Interpret analytics and suggest improvements
4. Help with content planning and scheduling
5. Give personalized advice based on user's niche
6. Be encouraging but realistic
7. Provide specific, actionable recommendations

Always be professional, helpful, and data-driven in your responses.
"""

    async def chat(
        self,
        user_message: str,
        conversation_history: Optional[List[Dict]] = None,
        user_context: Optional[Dict] = None
    ) -> str:
        """Main chat interface"""

        # Build messages
        messages = [{"role": "system", "content": self.system_prompt}]

        # Add user context if provided
        if user_context:
            context_message = self._build_context_message(user_context)
            messages.append({"role": "system", "content": context_message})

        # Add conversation history
        if conversation_history:
            messages.extend(conversation_history)

        # Add current message
        messages.append({"role": "user", "content": user_message})

        # Get response
        response = self.openai_client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )

        return response.choices[0].message.content

    def _build_context_message(self, context: Dict) -> str:
        """Build context message from user data"""

        context_parts = ["Current user context:"]

        if "niche" in context:
            context_parts.append(f"- Niche: {context['niche']}")

        if "follower_count" in context:
            context_parts.append(f"- Followers: {context['follower_count']}")

        if "monthly_views" in context:
            context_parts.append(f"- Monthly views: {context['monthly_views']}")

        if "total_pins" in context:
            context_parts.append(f"- Total pins: {context['total_pins']}")

        if "avg_engagement" in context:
            context_parts.append(f"- Avg engagement rate: {context['avg_engagement']}%")

        if "goals" in context:
            context_parts.append(f"- Goals: {context['goals']}")

        return "\n".join(context_parts)

    async def analyze_performance(
        self,
        analytics_data: Dict
    ) -> Dict:
        """Analyze Pinterest performance and provide insights"""

        prompt = f"""Analyze this Pinterest account performance:

Metrics:
- Impressions: {analytics_data.get('impressions', 0)}
- Saves: {analytics_data.get('saves', 0)}
- Clicks: {analytics_data.get('clicks', 0)}
- Engagement Rate: {analytics_data.get('engagement_rate', 0)}%
- Follower Growth: {analytics_data.get('follower_growth', 0)}
- Top Performing Pins: {analytics_data.get('top_pins', [])}

Provide:
1. Performance summary (good/average/needs improvement)
2. Key strengths
3. Areas for improvement
4. Specific action items (at least 5)
5. Growth predictions if recommendations are followed

Return as JSON format."""

        response = self.openai_client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800,
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)

    async def create_growth_strategy(
        self,
        niche: str,
        current_followers: int,
        target_followers: int,
        timeline_months: int
    ) -> Dict:
        """Create a comprehensive growth strategy"""

        prompt = f"""Create a detailed Pinterest growth strategy:

Current Situation:
- Niche: {niche}
- Current Followers: {current_followers}
- Target Followers: {target_followers}
- Timeline: {timeline_months} months

Create a comprehensive growth plan including:
1. Monthly milestones
2. Content strategy (types, frequency, themes)
3. Posting schedule (best times, frequency)
4. SEO strategy (keywords, hashtags)
5. Engagement tactics
6. Automation recommendations
7. Success metrics to track
8. Potential challenges and solutions

Return as detailed JSON format."""

        response = self.openai_client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1500,
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)

    async def review_content(
        self,
        pin_title: str,
        pin_description: str,
        niche: str
    ) -> Dict:
        """Review and score pin content"""

        prompt = f"""Review this Pinterest pin content for the {niche} niche:

Title: {pin_title}
Description: {pin_description}

Provide:
1. Overall score (1-10)
2. Title score (1-10) with feedback
3. Description score (1-10) with feedback
4. SEO score (1-10) with feedback
5. Specific improvements for each element
6. Predicted performance (low/medium/high)

Return as JSON format."""

        response = self.openai_client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=600,
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)

    async def suggest_daily_tasks(
        self,
        user_context: Dict
    ) -> List[str]:
        """Suggest daily tasks based on user's situation"""

        prompt = f"""Based on this Pinterest account status, suggest 5-7 specific tasks for today:

Context: {json.dumps(user_context)}

Tasks should be:
- Specific and actionable
- Prioritized by impact
- Realistic to complete in one day
- Focused on growth

Return as JSON array of task strings."""

        response = self.openai_client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=400,
            response_format={"type": "json_object"}
        )

        result = json.loads(response.choices[0].message.content)
        return result.get("tasks", [])

    async def answer_question(
        self,
        question: str,
        context: Optional[Dict] = None
    ) -> str:
        """Answer Pinterest-related questions"""

        context_str = ""
        if context:
            context_str = f"\n\nUser context: {json.dumps(context)}"

        prompt = f"{question}{context_str}"

        return await self.chat(
            user_message=prompt,
            conversation_history=None,
            user_context=context
        )

chatbot_ceo = ChatbotCEO()
