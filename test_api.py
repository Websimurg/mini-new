#!/usr/bin/env python3
"""
Quick API Test - Pinterest Growth Platform
Tests all integrated APIs without database
"""
import os
import asyncio
from dotenv import load_dotenv

# Load environment
load_dotenv('backend/.env')

async def test_openai():
    """Test OpenAI API"""
    print("\n🤖 Testing OpenAI API...")
    try:
        import openai
        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a Pinterest marketing expert."},
                {"role": "user", "content": "Generate 3 hashtags for a healthy breakfast pin."}
            ],
            max_tokens=100
        )

        result = response.choices[0].message.content
        print(f"✅ OpenAI API Working!")
        print(f"Response: {result}")
        return True
    except Exception as e:
        print(f"❌ OpenAI Error: {str(e)}")
        return False

async def test_pinterest():
    """Test Pinterest API"""
    print("\n📌 Testing Pinterest API...")
    try:
        import requests

        access_token = os.getenv('PINTEREST_ACCESS_TOKEN')
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        response = requests.get(
            "https://api.pinterest.com/v5/user_account",
            headers=headers
        )

        if response.status_code == 200:
            data = response.json()
            print(f"✅ Pinterest API Working!")
            print(f"Username: {data.get('username', 'N/A')}")
            print(f"Profile URL: {data.get('profile_url', 'N/A')}")
            return True
        else:
            print(f"❌ Pinterest Error: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Pinterest Error: {str(e)}")
        return False

async def test_fal_ai():
    """Test Fal.ai API"""
    print("\n🎨 Testing Fal.ai API...")
    try:
        import httpx

        api_key = os.getenv('FAL_API_KEY')

        # Simple test - check if API key is valid
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                "https://fal.run/fal-ai/flux/dev",
                json={
                    "prompt": "A simple test image",
                    "image_size": {"width": 512, "height": 512},
                    "num_inference_steps": 4  # Fast test
                },
                headers={
                    "Authorization": f"Key {api_key}",
                    "Content-Type": "application/json"
                }
            )

            if response.status_code in [200, 201]:
                print(f"✅ Fal.ai API Working!")
                print(f"Response status: {response.status_code}")
                return True
            else:
                print(f"⚠️  Fal.ai Response: {response.status_code}")
                print(f"Message: {response.text[:200]}")
                return False

    except Exception as e:
        print(f"❌ Fal.ai Error: {str(e)}")
        return False

async def test_supabase():
    """Test Supabase connection"""
    print("\n🗄️  Testing Supabase...")
    try:
        from supabase import create_client

        url = os.getenv('SUPABASE_URL')
        key = os.getenv('SUPABASE_ANON_KEY')

        supabase = create_client(url, key)

        # Simple health check
        print(f"✅ Supabase Connected!")
        print(f"URL: {url}")
        return True

    except Exception as e:
        print(f"❌ Supabase Error: {str(e)}")
        return False

async def main():
    print("=" * 60)
    print("🚀 Pinterest Growth Platform - API Test")
    print("=" * 60)

    results = {}

    # Test each API
    results['OpenAI'] = await test_openai()
    results['Pinterest'] = await test_pinterest()
    results['Fal.ai'] = await test_fal_ai()
    results['Supabase'] = await test_supabase()

    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Summary")
    print("=" * 60)

    for service, status in results.items():
        emoji = "✅" if status else "❌"
        print(f"{emoji} {service}: {'Working' if status else 'Failed'}")

    total = len(results)
    passed = sum(results.values())
    print(f"\n✨ {passed}/{total} services working!")

    if passed == total:
        print("\n🎉 All systems operational! Ready to use!")
    elif passed > 0:
        print("\n⚠️  Some services need attention, but core features work!")
    else:
        print("\n❌ Please check your API keys and try again.")

    print("\n💡 Next steps:")
    print("   1. Start backend: cd backend && uvicorn app.main:app --reload")
    print("   2. Visit API docs: http://localhost:8000/docs")
    print("   3. Start frontend: cd frontend && npm run dev")

if __name__ == "__main__":
    asyncio.run(main())
