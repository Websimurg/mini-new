# ⚡ Hızlı Başlangıç

## 1️⃣ Ön Gereksinimler

```bash
# Python 3.11+ ve Node.js 18+ yüklü olmalı
python3 --version
node --version
npm --version
```

## 2️⃣ Backend'i Başlat (5 dakika)

```bash
# 1. Backend klasörüne git
cd backend

# 2. Virtual environment oluştur
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Dependencies yükle
pip install -r requirements.txt

# 4. Environment dosyasını kontrol et
cat .env  # API anahtarlarının olduğundan emin ol

# 5. Serveri başlat
uvicorn app.main:app --reload --port 8000
```

**Backend çalışıyor!**
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

## 3️⃣ Frontend'i Başlat (3 dakika)

Yeni bir terminal aç:

```bash
# 1. Frontend klasörüne git
cd frontend

# 2. Dependencies yükle
npm install

# 3. Environment dosyasını kontrol et
cat .env.local  # API keys kontrol

# 4. Development server başlat
npm run dev
```

**Frontend çalışıyor!**
- App: http://localhost:3000

## 4️⃣ Hızlı Test (1 dakika)

### API Endpoint Test:

```bash
# OpenAI - Hashtag Üret
curl -X POST http://localhost:8000/api/v1/ai/generate/hashtags \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Healthy Breakfast",
    "keywords": ["breakfast", "healthy"],
    "count": 10
  }'

# Pinterest - Profil Al
curl http://localhost:8000/api/v1/pinterest/profile

# Chatbot CEO - Chat
curl -X POST http://localhost:8000/api/v1/chatbot/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Merhaba, Pinterest stratejisi hakkında bilgi verir misin?"
  }'
```

### Web UI Test:

1. http://localhost:3000 adresine git
2. Dashboard'u incele
3. "AI İçerik" sekmesine tıkla
4. Bir konu ve keywords gir
5. "Açıklama Oluştur" butonuna tıkla

## 5️⃣ Alternatif: Docker ile Başlat

Eğer Docker yüklüyse (en kolay yöntem):

```bash
# Tüm servisleri başlat
docker-compose up -d

# Database migration
docker-compose exec backend alembic upgrade head

# Logları izle
docker-compose logs -f

# Durdur
docker-compose down
```

## 🎯 Test Sayfaları

### Backend API (Swagger UI)
http://localhost:8000/docs

Buradan **tüm endpoint'leri interaktif test edebilirsiniz!**

#### Test Edilebilecek Özellikler:

**AI Content Generation:**
- `POST /api/v1/ai/generate/description` - Pin açıklaması üret
- `POST /api/v1/ai/generate/titles` - Başlık önerileri
- `POST /api/v1/ai/generate/hashtags` - Hashtag üret
- `POST /api/v1/ai/generate/image` - AI görsel üret (Fal.ai)
- `POST /api/v1/ai/optimize` - İçerik optimize et
- `GET /api/v1/ai/trends/{niche}` - Trend analizi

**Chatbot CEO:**
- `POST /api/v1/chatbot/chat` - CEO ile sohbet
- `POST /api/v1/chatbot/analyze-performance` - Performans analizi
- `POST /api/v1/chatbot/create-strategy` - Büyüme stratejisi
- `POST /api/v1/chatbot/review-content` - İçerik değerlendirmesi
- `POST /api/v1/chatbot/daily-tasks` - Günlük görevler

**Pinterest API:**
- `GET /api/v1/pinterest/boards` - Board'ları listele
- `POST /api/v1/pinterest/boards` - Yeni board oluştur
- `GET /api/v1/pinterest/profile` - Profil bilgisi

### Frontend UI
http://localhost:3000

#### Sayfalar:
- **Ana Sayfa** - Landing page
- **Dashboard** - http://localhost:3000/dashboard
  - Genel Bakış
  - AI İçerik Üretici
  - İçerik Planlayıcı
  - CEO Chatbot
  - Analitik

## 🐛 Sorun Giderme

### Port Kullanımda Hatası
```bash
# 8000 portunu kullanan servisi bul
lsof -i :8000
# Veya farklı port kullan
uvicorn app.main:app --reload --port 8001
```

### ModuleNotFoundError
```bash
# Pip cache temizle ve yeniden yükle
pip cache purge
pip install -r requirements.txt --force-reinstall
```

### API Key Hatası
```bash
# Environment dosyasını kontrol et
cat backend/.env

# Eksik varsa API_INTEGRATION.md dosyasına bak
cat API_INTEGRATION.md
```

### CORS Hatası
```bash
# backend/.env dosyasında ALLOWED_ORIGINS kontrol et
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
```

## 📊 Örnek Request'ler

### AI Görsel Üret (Fal.ai)
```json
POST /api/v1/ai/generate/image

{
  "prompt": "Healthy breakfast bowl with fruits and granola, food photography",
  "use_fal": true,
  "style": "colorful",
  "add_text": "Healthy Start",
  "text_position": "center"
}
```

### Chatbot ile Strateji Al
```json
POST /api/v1/chatbot/create-strategy

{
  "niche": "Home Decor",
  "current_followers": 500,
  "target_followers": 10000,
  "timeline_months": 6
}
```

### Pin Açıklaması Üret
```json
POST /api/v1/ai/generate/description

{
  "topic": "Quick Dinner Recipes",
  "keywords": ["dinner", "quick", "easy", "recipes"],
  "tone": "engaging",
  "length": "medium"
}
```

## ✨ İlk Kullanım Akışı

1. **Backend başlat** → http://localhost:8000/docs
2. **Test endpoint** → Swagger UI'da "Try it out"
3. **Frontend başlat** → http://localhost:3000
4. **Dashboard'a git** → Sol menüden gezin
5. **AI İçerik üret** → Konu gir ve test et
6. **CEO Chatbot** → Soru sor ve öneriler al

## 🚀 Production Deploy

### Backend (Railway/Render)
```bash
# Railway
railway login
railway init
railway up

# Render
# render.yaml dosyası hazır
```

### Frontend (Vercel)
```bash
# Vercel
vercel login
vercel

# Netlify
netlify deploy
```

## 📝 Notlar

- **Tüm API anahtarları .env dosyasında yapılandırılmış**
- **PostgreSQL ve Redis Docker ile otomatik başlar**
- **Celery worker otomatik pin scheduling için çalışır**
- **Hot reload aktif - kod değişikliklerini otomatik algılar**

---

**🎉 Hazırsınız! Servisleri başlatın ve test edin!**

Sorularınız için: API_INTEGRATION.md dosyasına bakın.
