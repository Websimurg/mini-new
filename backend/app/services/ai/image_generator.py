"""
AI Image Generator Service
Generates Pinterest-optimized images using AI
"""
from typing import Optional, Dict
import openai
from app.core.config import settings
import httpx
import base64
from io import BytesIO
from PIL import Image

class AIImageGenerator:
    def __init__(self):
        self.openai_client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

    async def generate_pin_image_dalle(
        self,
        prompt: str,
        size: str = "1024x1792"  # Pinterest vertical format
    ) -> bytes:
        """Generate pin image using DALL-E 3"""

        response = self.openai_client.images.generate(
            model="dall-e-3",
            prompt=f"{prompt}\n\nStyle: Pinterest pin, vertical format, professional, eye-catching, vibrant colors",
            size=size,
            quality="hd",
            n=1,
        )

        image_url = response.data[0].url

        # Download image
        async with httpx.AsyncClient() as client:
            img_response = await client.get(image_url)
            return img_response.content

    async def generate_pin_image_stable_diffusion(
        self,
        prompt: str
    ) -> bytes:
        """Generate pin image using Stable Diffusion (via Replicate)"""

        if not settings.REPLICATE_API_TOKEN:
            raise ValueError("REPLICATE_API_TOKEN not configured")

        # This is a placeholder - you'd integrate with Replicate API
        # For now, we'll use DALL-E as fallback
        return await self.generate_pin_image_dalle(prompt)

    async def resize_for_pinterest(
        self,
        image_bytes: bytes,
        width: int = 1000,
        height: int = 1500
    ) -> bytes:
        """Resize image to Pinterest optimal dimensions (2:3 ratio)"""

        image = Image.open(BytesIO(image_bytes))

        # Calculate aspect ratio
        aspect = width / height
        img_aspect = image.width / image.height

        if img_aspect > aspect:
            # Image is wider, crop width
            new_height = image.height
            new_width = int(new_height * aspect)
            left = (image.width - new_width) // 2
            image = image.crop((left, 0, left + new_width, new_height))
        else:
            # Image is taller, crop height
            new_width = image.width
            new_height = int(new_width / aspect)
            top = (image.height - new_height) // 2
            image = image.crop((0, top, new_width, top + new_height))

        # Resize to target dimensions
        image = image.resize((width, height), Image.Resampling.LANCZOS)

        # Convert to bytes
        output = BytesIO()
        image.save(output, format='PNG', optimize=True, quality=95)
        return output.getvalue()

    async def add_text_overlay(
        self,
        image_bytes: bytes,
        text: str,
        position: str = "center"
    ) -> bytes:
        """Add text overlay to image (for pin titles)"""

        from PIL import ImageDraw, ImageFont

        image = Image.open(BytesIO(image_bytes))
        draw = ImageDraw.Draw(image)

        # Try to use a nice font, fallback to default
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
        except:
            font = ImageFont.load_default()

        # Calculate text position
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        if position == "center":
            x = (image.width - text_width) // 2
            y = (image.height - text_height) // 2
        elif position == "top":
            x = (image.width - text_width) // 2
            y = 50
        else:  # bottom
            x = (image.width - text_width) // 2
            y = image.height - text_height - 50

        # Draw text with outline for better visibility
        outline_color = "black"
        text_color = "white"

        # Draw outline
        for adj_x in range(-2, 3):
            for adj_y in range(-2, 3):
                draw.text((x + adj_x, y + adj_y), text, font=font, fill=outline_color)

        # Draw text
        draw.text((x, y), text, font=font, fill=text_color)

        # Convert to bytes
        output = BytesIO()
        image.save(output, format='PNG', optimize=True, quality=95)
        return output.getvalue()

ai_image_generator = AIImageGenerator()
