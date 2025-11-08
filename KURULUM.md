# Pinterest Growth Platform - Kurulum Rehberi

## Hızlı Başlangıç

### 1. Gereksinimler
- Docker Desktop kurulu olmalı
- Git kurulu olmalı
- En az 4GB RAM
- 10GB boş disk alanı

### 2. Adım Adım Kurulum

#### A. Projeyi İndirin
```bash
git clone https://github.com/yourusername/pinterest-growth-platform.git
cd pinterest-growth-platform
```

#### B. API Anahtarlarını Alın

1. **OpenAI API Key** (Zorunlu):
   - https://platform.openai.com/api-keys adresine gidin
   - Hesap oluşturun ve API key alın
   - Ücretli bir hesap gerekebilir

2. **Pinterest Developer** (Zorunlu):
   - https://developers.pinterest.com/ adresine gidin
   - Uygulama oluşturun
   - App ID ve App Secret alın

3. **Cloudinary** (Opsiyonel - görsel yükleme için):
   - https://cloudinary.com/ hesap oluşturun
   - Dashboard'dan API credentials alın

#### C. Environment Ayarları

1. Backend environment:
```bash
cp backend/.env.example backend/.env
```

2. `backend/.env` dosyasını düzenleyin:
```env
# Zorunlu
OPENAI_API_KEY=sk-your-openai-key-here
PINTEREST_APP_ID=your-pinterest-app-id
PINTEREST_APP_SECRET=your-pinterest-app-secret
SECRET_KEY=generate-a-random-secret-key-here

# Database (Docker kullanıyorsanız varsayılanları değiştirmeyin)
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/pinterest_growth
REDIS_URL=redis://redis:6379/0
CELERY_BROKER_URL=redis://redis:6379/1
CELERY_RESULT_BACKEND=redis://redis:6379/2

# Opsiyonel
ANTHROPIC_API_KEY=your-anthropic-key (Claude için)
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

3. Frontend environment:
```bash
cp frontend/.env.local.example frontend/.env.local
```

#### D. Docker ile Başlatın

```bash
# Tüm servisleri başlat
docker-compose up -d

# Logları izle
docker-compose logs -f

# Servislerin durumunu kontrol et
docker-compose ps
```

#### E. Database Migration

```bash
# Migration dosyalarını oluştur (ilk kurulumda)
docker-compose exec backend alembic revision --autogenerate -m "Initial migration"

# Migration'ları çalıştır
docker-compose exec backend alembic upgrade head
```

#### F. Uygulamaya Erişin

- **Frontend (Web UI)**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379

### 3. İlk Kullanım

1. http://localhost:3000 adresine gidin
2. Hesap oluşturun
3. Pinterest hesabınızı bağlayın
4. AI özelliklerini test edin!

## Sorun Giderme

### Port Çakışması
Eğer portlar kullanımdaysa, `docker-compose.yml` dosyasında port numaralarını değiştirin:
```yaml
ports:
  - "3001:3000"  # Frontend için
  - "8001:8000"  # Backend için
```

### Database Bağlantı Hatası
```bash
# PostgreSQL container'ını yeniden başlat
docker-compose restart postgres

# Logları kontrol et
docker-compose logs postgres
```

### Celery Worker Çalışmıyor
```bash
# Worker'ı yeniden başlat
docker-compose restart celery_worker

# Logları kontrol et
docker-compose logs celery_worker
```

### Frontend Build Hatası
```bash
# Node modules'i temizle
docker-compose exec frontend rm -rf node_modules
docker-compose exec frontend npm install

# Container'ı yeniden başlat
docker-compose restart frontend
```

## Manuel Kurulum (Docker Olmadan)

### Backend

```bash
cd backend

# Python 3.11+ gerekli
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

# PostgreSQL ve Redis'i manuel olarak kurun ve başlatın
# .env dosyasını düzenleyin

# Migration
alembic upgrade head

# Server
uvicorn app.main:app --reload --port 8000
```

Ayrı terminallerде:
```bash
# Celery Worker
celery -A app.celery_app worker --loglevel=info

# Celery Beat
celery -A app.celery_app beat --loglevel=info
```

### Frontend

```bash
cd frontend

# Node.js 18+ gerekli
npm install

# .env.local dosyasını düzenleyin

# Development server
npm run dev
```

## Production Deployment

### Docker Production Build

```bash
# Production build
docker-compose -f docker-compose.prod.yml up -d

# SSL sertifikası için nginx ekleyin
# Güvenlik için environment variables'ı güvenli tutun
```

### Environment Variables Production
```env
DEBUG=False
SECRET_KEY=very-strong-random-key-min-32-chars
ALLOWED_ORIGINS=https://yourdomain.com
```

## Yedekleme

### Database Yedekleme
```bash
docker-compose exec postgres pg_dump -U postgres pinterest_growth > backup.sql
```

### Database Geri Yükleme
```bash
docker-compose exec -T postgres psql -U postgres pinterest_growth < backup.sql
```

## Güncelleme

```bash
# Kodu güncelle
git pull

# Container'ları yeniden build et
docker-compose down
docker-compose up -d --build

# Migration'ları çalıştır
docker-compose exec backend alembic upgrade head
```

## Destek

Sorun yaşıyorsanız:
1. Logları kontrol edin: `docker-compose logs`
2. GitHub Issues: https://github.com/yourusername/pinterest-growth-platform/issues
3. Email: support@example.com
