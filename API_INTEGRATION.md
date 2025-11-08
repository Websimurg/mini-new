# API Entegrasyon Rehberi

## ✅ Entegre Edilmiş API'lar

### 1. Pinterest API ✅
**Status:** Aktif ve Yapılandırılmış

- **Client ID:** 1535671
- **Access Token:** Yapılandırıldı ✅
- **Endpoint:** https://api.pinterest.com/v5/

**Kullanım:**
```python
from app.services.pinterest.pinterest_service import get_default_pinterest_service

# Default token ile servis oluştur
pinterest = get_default_pinterest_service()

# Veya özel token ile
pinterest = PinterestService(access_token="custom_token")

# Kullanıcı profilini al
profile = await pinterest.get_user_profile()

# Board'ları al
boards = await pinterest.get_boards()

# Pin oluştur
pin = await pinterest.create_pin(
    board_id="board_id",
    title="Pin Title",
    description="Pin Description",
    image_url="https://example.com/image.jpg"
)
```

### 2. OpenAI API (GPT-4) ✅
**Status:** Aktif ve Yapılandırılmış

**Özellikler:**
- Pin açıklaması oluşturma
- Başlık önerileri
- Hashtag üretimi
- Trend analizi
- İçerik optimizasyonu

**Kullanım:**
```python
from app.services.ai.content_generator import ai_content_generator

# Pin açıklaması oluştur
description = await ai_content_generator.generate_pin_description(
    topic="Sağlıklı Kahvaltı",
    keywords=["kahvaltı", "sağlıklı", "tarifler"],
    tone="engaging",
    length="medium"
)

# Hashtag oluştur
hashtags = await ai_content_generator.generate_hashtags(
    topic="Fitness",
    keywords=["workout", "health"],
    count=15
)
```

### 3. Fal.ai (AI Image Generation) ✅
**Status:** Aktif ve Yapılandırılmış

**Özellikler:**
- Pinterest-optimized görsel üretimi (1024x1536)
- 7 farklı stil seçeneği
- Hızlı ve ekonomik
- Birden fazla varyasyon üretimi

**Stiller:**
- modern
- vintage
- colorful
- elegant
- playful
- minimalist
- bold

**Kullanım:**
```python
from app.services.ai.fal_image_generator import fal_image_generator

# Basit görsel üret
image_bytes = await fal_image_generator.generate_pin_image(
    prompt="A beautiful sunset over mountains"
)

# Stil ile üret
image_bytes = await fal_image_generator.generate_with_style(
    prompt="Modern kitchen design",
    style="modern"
)

# Çoklu varyasyon
images = await fal_image_generator.generate_multiple_variations(
    prompt="Yoga poses for beginners",
    count=4
)
```

### 4. Supabase (Database) ✅
**Status:** Aktif ve Yapılandırılmış

**URL:** https://uukxrfhvkgdpecpwmlxr.supabase.co

**Backend Kullanım:**
```python
from app.db.supabase_client import get_supabase

supabase = get_supabase()

# Veri çek
response = supabase.table('pins').select('*').execute()
```

**Frontend Kullanım:**
```typescript
import { supabase, supabaseHelpers } from '@/lib/supabase'

// Kullanıcı girişi
const user = await supabaseHelpers.signIn(email, password)

// Pinterest hesaplarını al
const accounts = await supabaseHelpers.getPinterestAccounts(userId)

// Pin oluştur
const pin = await supabaseHelpers.createPin({
  title: "Pin Title",
  description: "Description",
  user_id: userId
})
```

## 🔌 API Endpoint'leri

### AI Content Generation

#### 1. Generate Description
```http
POST /api/v1/ai/generate/description
Content-Type: application/json

{
  "topic": "Healthy Breakfast",
  "keywords": ["breakfast", "healthy", "recipes"],
  "tone": "engaging",
  "length": "medium"
}
```

#### 2. Generate Titles
```http
POST /api/v1/ai/generate/titles
Content-Type: application/json

{
  "topic": "Fitness Tips",
  "keywords": ["fitness", "workout"],
  "count": 5
}
```

#### 3. Generate Hashtags
```http
POST /api/v1/ai/generate/hashtags
Content-Type: application/json

{
  "topic": "Travel Photography",
  "keywords": ["travel", "photography"],
  "count": 15
}
```

#### 4. Generate Image (Fal.ai)
```http
POST /api/v1/ai/generate/image
Content-Type: application/json

{
  "prompt": "Modern minimalist home office setup",
  "use_fal": true,
  "style": "modern",
  "add_text": "Home Office Ideas",
  "text_position": "center"
}
```

**Response:**
```json
{
  "image": "data:image/png;base64,...",
  "message": "Image generated successfully",
  "generator": "fal.ai"
}
```

### Chatbot CEO

#### 1. Chat
```http
POST /api/v1/chatbot/chat
Content-Type: application/json

{
  "message": "Pinterest stratejim için öneriler verir misin?",
  "conversation_history": [
    {
      "role": "user",
      "content": "Merhaba"
    },
    {
      "role": "assistant",
      "content": "Merhaba! Nasıl yardımcı olabilirim?"
    }
  ],
  "user_context": {
    "niche": "Food & Recipes",
    "follower_count": 1500,
    "monthly_views": 45000
  }
}
```

#### 2. Analyze Performance
```http
POST /api/v1/chatbot/analyze-performance
Content-Type: application/json

{
  "analytics_data": {
    "impressions": 125000,
    "saves": 8500,
    "clicks": 2100,
    "engagement_rate": 6.8,
    "follower_growth": 250
  }
}
```

#### 3. Create Growth Strategy
```http
POST /api/v1/chatbot/create-strategy
Content-Type: application/json

{
  "niche": "Home Decor",
  "current_followers": 1000,
  "target_followers": 10000,
  "timeline_months": 6
}
```

## 📊 Rate Limits

### Pinterest API
- 200 requests/minute
- 10,000 requests/day

### OpenAI API
- gpt-4-turbo-preview: 10,000 TPM (tokens per minute)
- Depends on your tier

### Fal.ai
- Depends on your subscription
- Generally very generous limits

### Supabase
- Free tier: 500MB database, 2GB bandwidth
- Unlimited API requests

## 🔐 Güvenlik Notları

1. **API Anahtarları asla frontend'e expose etmeyin**
   - Backend'den proxy edin
   - Environment variables kullanın

2. **Rate limiting uygulayın**
   - Celery tasks ile throttle yapın
   - Redis ile cache kullanın

3. **Error handling**
   - Tüm API çağrılarında try-catch kullanın
   - User-friendly error mesajları gösterin

4. **Monitoring**
   - API kullanım metrikleri takip edin
   - Sentry ile error tracking yapın

## 🚀 Başlatma

1. Backend servisi başlat:
```bash
cd backend
uvicorn app.main:app --reload
```

2. API docs: http://localhost:8000/docs

3. Test endpoint:
```bash
curl -X POST http://localhost:8000/api/v1/ai/generate/hashtags \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Travel",
    "keywords": ["travel", "adventure"],
    "count": 10
  }'
```

## 📝 Örnek Workflow

### Tam Pin Oluşturma Süreci

```python
# 1. Konu ve keywords belirle
topic = "Healthy Breakfast Ideas"
keywords = ["breakfast", "healthy", "recipes", "nutrition"]

# 2. AI ile içerik üret
# Başlık
titles = await ai_content_generator.generate_pin_title(topic, keywords, count=5)
selected_title = titles[0]

# Açıklama
description = await ai_content_generator.generate_pin_description(
    topic, keywords, tone="engaging", length="medium"
)

# Hashtags
hashtags = await ai_content_generator.generate_hashtags(topic, keywords, count=15)

# 3. Görsel üret (Fal.ai)
image_prompt = f"{topic}, food photography, professional, appetizing"
image_bytes = await fal_image_generator.generate_with_style(
    prompt=image_prompt,
    style="colorful"
)

# Text overlay ekle
image_with_text = await ai_image_generator.add_text_overlay(
    image_bytes=image_bytes,
    text=selected_title,
    position="center"
)

# 4. Pinterest'e yükle
pinterest = get_default_pinterest_service()
pin = await pinterest.create_pin(
    board_id="your_board_id",
    title=selected_title,
    description=description + "\n\n" + " ".join(hashtags),
    image_url="uploaded_image_url",  # S3/Cloudinary'den URL
)

# 5. Database'e kaydet (Supabase)
supabase = get_supabase()
await supabase.table('pins').insert({
    'user_id': user_id,
    'pinterest_pin_id': pin['id'],
    'title': selected_title,
    'description': description,
    'hashtags': hashtags,
    'is_ai_generated': True
}).execute()
```

## 🎯 Sonraki Adımlar

- [ ] Pinterest OAuth flow ekle
- [ ] Cloudinary/S3 görsel upload entegrasyonu
- [ ] Webhook'lar ile real-time senkronizasyon
- [ ] A/B testing özelliği
- [ ] Bulk operations API

Tüm sistemler aktif ve kullanıma hazır! 🚀
