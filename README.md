# Pinterest Growth Platform

Pinterest hesabınızı otomatik olarak büyütmek için kapsamlı AI destekli platform. PinClicks, ContentGoblin ve BlogToPin gibi araçların tüm özelliklerini tek bir platformda birleştirir.

## ⚡ Hızlı Başlangıç

[![Run on Replit](https://replit.com/badge/github/Websimurg/mini-new)](https://replit.com/github/Websimurg/mini-new)

**2 Dakikada Başlat:**
- 🚀 [Replit'e Deploy Et](REPLIT_DEPLOY.md) - En kolay yol!
- 💻 [Lokal Kurulum](BASLATMA_KILAVUZU.md) - Bilgisayarınızda çalıştırın
- 📚 [API Kullanımı](API_INTEGRATION.md) - API ile entegrasyon

## 🚀 Özellikler

### 1. AI İçerik Üretimi (ContentGoblin Özellikleri)
- ✨ Otomatik pin görseli oluşturma (DALL-E 3)
- 📝 SEO optimizasyonlu pin açıklamaları
- 🎯 Başlık önerileri
- #️⃣ Hashtag optimizasyonu
- 📊 Trend analizi ve içerik fikirleri
- 🎨 Görsel optimizasyonu

### 2. İçerik Planlama (BlogToPin Özellikleri)
- 📅 İçerik takvimi ve zamanlama
- 🔄 Blog-to-Pin otomatik dönüştürme
- 📰 RSS feed entegrasyonu
- ⏰ Optimal zamanlama önerileri
- 📦 Toplu içerik planlama

### 3. Otomatik Pinleme (PinClicks Özellikleri)
- 🤖 Otomatik pin paylaşımı
- 📌 Toplu pin yükleme
- 🎲 Akıllı board yönetimi
- 🔁 Zamanlı yayınlama
- 🎯 Hedeflenmiş otomasyon

### 4. CEO Chatbot (AI Asistan)
- 💬 Pinterest strateji danışmanlığı
- 📈 Analitik yorumlama
- 💡 Kişiselleştirilmiş öneriler
- 📋 Günlük görev önerileri
- 🎓 Eğitim ve rehberlik

### 5. Analitik ve Raporlama
- 📊 Detaylı performans metrikleri
- 📈 Büyüme takibi
- 🎯 En iyi performans gösteren içerikler
- 📉 Etkileşim analizi
- 📅 Tarihsel veriler

## 🛠️ Teknoloji Stack

### Backend
- **Framework:** FastAPI (Python)
- **Database:** PostgreSQL
- **Cache:** Redis
- **Task Queue:** Celery
- **AI:** OpenAI GPT-4, DALL-E 3, Anthropic Claude

### Frontend
- **Framework:** Next.js 14 (TypeScript)
- **Styling:** Tailwind CSS
- **State Management:** Zustand
- **API Client:** Axios + React Query
- **UI Components:** Lucide Icons, React Hot Toast

### DevOps
- **Containerization:** Docker & Docker Compose
- **Database Migrations:** Alembic
- **API Documentation:** Swagger/OpenAPI

## 📦 Kurulum

### Gereksinimler
- Docker & Docker Compose
- Node.js 18+ (local development için)
- Python 3.11+ (local development için)

### Docker ile Kurulum (Önerilen)

1. Repository'yi klonlayın:
```bash
git clone https://github.com/yourusername/pinterest-growth-platform.git
cd pinterest-growth-platform
```

2. Environment dosyalarını oluşturun:
```bash
# Backend
cp backend/.env.example backend/.env
# API anahtarlarınızı backend/.env dosyasına ekleyin

# Frontend
cp frontend/.env.local.example frontend/.env.local
```

3. API anahtarlarını yapılandırın:
`backend/.env` dosyasını düzenleyin ve aşağıdaki anahtarları ekleyin:
- `OPENAI_API_KEY`: OpenAI API anahtarınız
- `PINTEREST_APP_ID`: Pinterest App ID
- `PINTEREST_APP_SECRET`: Pinterest App Secret
- Diğer gerekli API anahtarları

4. Docker Compose ile başlatın:
```bash
docker-compose up -d
```

5. Database migration'ları çalıştırın:
```bash
docker-compose exec backend alembic upgrade head
```

6. Uygulamaya erişin:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Manuel Kurulum

#### Backend

```bash
cd backend

# Virtual environment oluştur
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Dependencies yükle
pip install -r requirements.txt

# Environment variables
cp .env.example .env
# .env dosyasını düzenle

# Database migration
alembic upgrade head

# Server'ı başlat
uvicorn app.main:app --reload
```

#### Frontend

```bash
cd frontend

# Dependencies yükle
npm install

# Environment variables
cp .env.local.example .env.local

# Development server başlat
npm run dev
```

#### Celery Worker & Beat

```bash
cd backend

# Worker
celery -A app.celery_app worker --loglevel=info

# Beat (scheduler) - başka bir terminal'de
celery -A app.celery_app beat --loglevel=info
```

## 🔑 API Anahtarları

Platformun çalışması için aşağıdaki API anahtarlarına ihtiyacınız var:

1. **OpenAI API Key**: https://platform.openai.com/api-keys
2. **Pinterest Developer**: https://developers.pinterest.com/
3. **Cloudinary** (opsiyonel): https://cloudinary.com/
4. **Anthropic Claude** (opsiyonel): https://console.anthropic.com/

## 📚 Kullanım

### 1. Pinterest Hesabı Bağlama
Dashboard'a giriş yaptıktan sonra Pinterest hesabınızı bağlayın.

### 2. AI İçerik Oluşturma
- Sol menüden "AI İçerik" sekmesine gidin
- Konunuzu ve anahtar kelimelerinizi girin
- İçerik türünü seçin (açıklama, başlık, hashtag, görsel)
- "Oluştur" butonuna tıklayın

### 3. İçerik Planlama
- "Planlama" sekmesine gidin
- Yeni plan oluştur
- RSS feed veya manuel içerik ekle
- Zamanlama ayarlarını yapılandır

### 4. CEO Chatbot ile Danışmanlık
- "CEO Asistan" sekmesine gidin
- Sorularınızı sorun
- Strateji önerileri alın

## 🏗️ Proje Yapısı

```
pinterest-growth-platform/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── endpoints/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── services/
│   │   │   ├── ai/
│   │   │   ├── pinterest/
│   │   │   └── scheduler/
│   │   ├── celery_app.py
│   │   ├── main.py
│   │   └── tasks.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── lib/
│   │   └── services/
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🔄 Celery Task'lar

Platform otomatik olarak şu görevleri çalıştırır:

- **execute_scheduled_pins**: Her 5 dakikada zamanlanmış pinleri yayınlar
- **sync_pinterest_analytics**: Günlük analitik verileri senkronize eder
- **process_rss_feeds**: Saatlik RSS feed kontrolü
- **cleanup_old_data**: Haftalık eski veri temizliği

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📝 Lisans

Bu proje MIT lisansı altındadır.

## 🐛 Sorun Bildirimi

Bir sorun mu buldunuz? [Issue](https://github.com/yourusername/pinterest-growth-platform/issues) açın.

## 📧 İletişim

Sorularınız için: [email@example.com](mailto:email@example.com)

## 🎯 Yol Haritası

- [ ] Mobil uygulama
- [ ] Instagram entegrasyonu
- [ ] TikTok entegrasyonu
- [ ] A/B testing özellikleri
- [ ] Gelişmiş analitik raporları
- [ ] Team collaboration özellikleri
- [ ] White-label çözüm

---

**Not**: Bu platform eğitim ve meşru Pinterest büyütme amaçlı geliştirilmiştir. Pinterest'in kullanım koşullarına uygun şekilde kullanılmalıdır.
