"""
Fal.ai Image Generator Service
Alternative to DALL-E for image generation
"""
from typing import Optional
import httpx
from app.core.config import settings
import asyncio

class FalImageGenerator:
    """Generate images using Fal.ai API"""

    def __init__(self):
        self.api_key = settings.FAL_API_KEY
        self.base_url = "https://fal.run/fal-ai"

    async def generate_pin_image(
        self,
        prompt: str,
        model: str = "flux/dev",
        width: int = 1024,
        height: int = 1536,  # Pinterest vertical format (2:3 ratio)
        num_inference_steps: int = 28,
        guidance_scale: float = 3.5
    ) -> bytes:
        """
        Generate Pinterest-optimized image using Fal.ai

        Args:
            prompt: Image generation prompt
            model: Fal.ai model to use (flux/dev, flux-pro, etc.)
            width: Image width
            height: Image height
            num_inference_steps: Number of denoising steps
            guidance_scale: How closely to follow the prompt
        """
        if not self.api_key:
            raise ValueError("FAL_API_KEY not configured")

        # Enhance prompt for Pinterest
        enhanced_prompt = f"{prompt}, Pinterest pin style, vertical format, professional, eye-catching, vibrant colors, high quality"

        endpoint = f"{self.base_url}/{model}"

        payload = {
            "prompt": enhanced_prompt,
            "image_size": {
                "width": width,
                "height": height
            },
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale,
            "num_images": 1,
            "enable_safety_checker": True,
            "output_format": "png"
        }

        headers = {
            "Authorization": f"Key {self.api_key}",
            "Content-Type": "application/json"
        }

        async with httpx.AsyncClient(timeout=120.0) as client:
            # Submit generation request
            response = await client.post(
                endpoint,
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            result = response.json()

            # Get image URL from result
            if "images" in result and len(result["images"]) > 0:
                image_url = result["images"][0]["url"]
            elif "image" in result:
                image_url = result["image"]["url"]
            else:
                raise ValueError("No image URL in response")

            # Download the generated image
            img_response = await client.get(image_url)
            img_response.raise_for_status()

            return img_response.content

    async def generate_multiple_variations(
        self,
        prompt: str,
        count: int = 4
    ) -> list[bytes]:
        """Generate multiple image variations"""
        tasks = [
            self.generate_pin_image(prompt)
            for _ in range(count)
        ]

        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Filter out errors
        images = [r for r in results if isinstance(r, bytes)]

        return images

    async def generate_with_style(
        self,
        prompt: str,
        style: str = "modern"
    ) -> bytes:
        """Generate image with specific style"""

        style_prompts = {
            "modern": "modern, clean, minimalist, professional",
            "vintage": "vintage, retro, nostalgic, aged",
            "colorful": "vibrant, colorful, bright, energetic",
            "elegant": "elegant, sophisticated, classy, luxury",
            "playful": "playful, fun, whimsical, creative",
            "minimalist": "minimalist, simple, clean lines, negative space",
            "bold": "bold, strong, dramatic, high contrast"
        }

        style_addition = style_prompts.get(style, "professional")
        full_prompt = f"{prompt}, {style_addition}"

        return await self.generate_pin_image(full_prompt)

    async def upscale_image(
        self,
        image_url: str,
        scale: int = 2
    ) -> bytes:
        """Upscale an existing image"""

        endpoint = f"{self.base_url}/clarity-upscaler"

        payload = {
            "image_url": image_url,
            "scale": scale
        }

        headers = {
            "Authorization": f"Key {self.api_key}",
            "Content-Type": "application/json"
        }

        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                endpoint,
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            result = response.json()

            upscaled_url = result.get("image", {}).get("url")
            if not upscaled_url:
                raise ValueError("No upscaled image URL in response")

            img_response = await client.get(upscaled_url)
            img_response.raise_for_status()

            return img_response.content

fal_image_generator = FalImageGenerator()
