# 🚀 Pinterest Growth Platform - Hızlı Başlangıç Kılavuzu

Pinterest hesabınızı otomatik olarak büyütmek için AI destekli platform.

## ⚡ Hızlı Başlatma (Önerilen)

### 1. OpenAI API Key Edinme

1. https://platform.openai.com/ adresine gidin
2. Hesap oluşturun veya giriş yapın
3. API Keys bölümüne gidin
4. "Create new secret key" butonuna tıklayın
5. Oluşturulan anahtarı kopyalayın (sk-proj-... ile başlar)

### 2. API Key'i Yapılandırma

`backend/.env` dosyasını açın ve aşağıdaki satırı düzenleyin:

```bash
OPENAI_API_KEY=buraya-kendi-api-keyinizi-yapiştirin
```

Örnek:
```bash
OPENAI_API_KEY=sk-proj-abc123xyz456...
```

### 3. Demo Server'ı Başlatma

Terminal'de aşağıdaki komutu çalıştırın:

```bash
python3 demo_server.py
```

Server başarıyla başladığında şu mesajı göreceksiniz:
```
============================================================
🚀 Pinterest Growth Platform - Demo Server
============================================================
📍 Server: http://0.0.0.0:8080
📚 API Docs: http://0.0.0.0:8080/docs
🧪 Test UI: http://0.0.0.0:8080/
============================================================
```

### 4. Uygulamayı Kullanma

Tarayıcınızda şu adresleri açın:

- **Ana Sayfa/Test UI:** http://localhost:8080/
- **API Dökümantasyonu:** http://localhost:8080/docs
- **Alternatif Port:** http://localhost:8080 (veya 5173)

## 🎯 Özellikler

### AI İçerik Üretimi
- **Pin Açıklaması:** SEO optimizasyonlu pin açıklamaları oluştur
- **Başlık Önerileri:** Birden fazla başlık alternatifi al
- **Hashtag Üretimi:** Trend ve niche hashtagler oluştur
- **Trend Analizi:** Niche'iniz için trend içerik fikirleri

### CEO Chatbot
- Pinterest strateji danışmanlığı
- Büyüme planı oluşturma
- Soru-cevap ile destek

### Pinterest Entegrasyonu (Opsiyonel)
- Profil bilgileri
- Board yönetimi
- Pin paylaşımı

## 📝 Test Etme

### 1. API Dökümantasyonu ile Test

1. http://localhost:8080/docs adresine gidin
2. İstediğiniz endpoint'i seçin (örn: `/api/v1/ai/generate/description`)
3. "Try it out" butonuna tıklayın
4. Parametreleri doldurun:
   ```json
   {
     "topic": "Sağlıklı smoothie tarifleri",
     "keywords": ["smoothie", "sağlıklı", "detoks"],
     "tone": "engaging",
     "length": "medium"
   }
   ```
5. "Execute" butonuna tıklayın
6. Sonucu görüntüleyin

### 2. Test HTML Arayüzü ile Test

1. http://localhost:8080/ adresine gidin
2. Arayüzden özellikler test edilebilir

## 🔧 Sorun Giderme

### OpenAI API Hatası
**Hata:** `Authentication error` veya `Invalid API key`

**Çözüm:**
- `backend/.env` dosyasında API key'in doğru olduğundan emin olun
- API key'in aktif ve kredisi olduğunu kontrol edin

### Port Zaten Kullanımda
**Hata:** `Address already in use`

**Çözüm:**
- Farklı bir port kullanın:
  ```bash
  PORT=8081 python3 demo_server.py
  ```

### Python Modül Bulunamadı
**Hata:** `ModuleNotFoundError: No module named 'fastapi'`

**Çözüm:**
```bash
pip3 install fastapi uvicorn python-dotenv openai requests pydantic
```

## 📚 Kullanım Örnekleri

### Pin Açıklaması Oluşturma

**API İsteği:**
```bash
curl -X POST "http://localhost:8080/api/v1/ai/generate/description" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Vegan brownie tarifi",
    "keywords": ["vegan", "brownie", "çikolatalı"],
    "tone": "friendly",
    "length": "medium"
  }'
```

### CEO Chatbot ile Sohbet

**API İsteği:**
```bash
curl -X POST "http://localhost:8080/api/v1/chatbot/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Pinterest hesabımı nasıl büyütebilirim?"
  }'
```

### Trend Analizi

**API İsteği:**
```bash
curl -X GET "http://localhost:8080/api/v1/ai/trends/home-decor"
```

## 🎨 Gelişmiş Özellikler

### Full Stack Versiyon (Next.js + PostgreSQL)

Daha gelişmiş özellikler için tam versiyon:

```bash
# Docker ile başlatma
docker-compose up -d

# Frontend
cd frontend
npm install
npm run dev

# Backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Erişim:**
- Frontend: http://localhost:3000
- Backend: http://localhost:8000

## 💡 İpuçları

1. **API Kullanımı:** OpenAI API'si ücretlidir. Kullanımı takip edin.
2. **Demo Mod:** Pinterest API anahtarları olmadan da çalışır (demo verilerle).
3. **Özelleştirme:** `demo_server.py` dosyasını ihtiyacınıza göre düzenleyebilirsiniz.
4. **Güvenlik:** Production'da mutlaka `SECRET_KEY` değiştirin.

## 📞 Yardım

- **Dokümantasyon:** README.md
- **API Entegrasyonu:** API_INTEGRATION.md
- **Hızlı Başlangıç:** QUICK_START.md

## 🎯 Sonraki Adımlar

1. ✅ Demo server'ı başlattınız
2. ⬜ OpenAI API key ekleyin
3. ⬜ İlk pin açıklamanızı oluşturun
4. ⬜ CEO chatbot ile strateji geliştirin
5. ⬜ Pinterest API entegrasyonu yapın

---

**Keyifli kullanımlar! 🚀**
