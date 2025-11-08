# 🚀 Replit'te Çalıştırma Rehberi

## Hızlı Başlangıç (2 Dakika)

### 1. Replit'te Projeyi Aç

1. [Replit.com](https://replit.com) hesabınıza giriş yapın
2. "Create Repl" butonuna tıklayın
3. "Import from GitHub" seçeneğini seçin
4. GitHub repo URL'nizi yapıştırın: `https://github.com/Websimurg/mini-new`
5. "Import from GitHub" butonuna tıklayın

### 2. Secrets (API Keys) Ekleyin

Replit'te sol tarafta "Secrets" (🔒) sekmesine tıklayın ve şu anahtarları ekleyin:

**Not:** API anahtarları `backend/.env` dosyasında mevcut. Oradan kopyalayın.

```bash
# backend/.env dosyasından kopyalayın:

OPENAI_API_KEY=your_openai_api_key_here
PINTEREST_ACCESS_TOKEN=your_pinterest_access_token_here
FAL_API_KEY=your_fal_api_key_here
SUPABASE_URL=your_supabase_url_here
SUPABASE_ANON_KEY=your_supabase_anon_key_here
```

**API Anahtarlarını Nereden Alacağınız:**
- `backend/.env` dosyasını açın
- Her bir değeri kopyalayın
- Replit Secrets'a yapıştırın

### 3. Run Butonuna Bas!

Sağ üstteki yeşil "▶ Run" butonuna tıklayın. İşte bu kadar!

## 🎯 Erişim Linkleri

Repl başladıktan sonra:

- **Ana Sayfa (Test UI)**: Replit'in verdiği URL (örn: `https://your-repl.your-username.repl.co`)
- **API Docs**: `https://your-repl.your-username.repl.co/docs`
- **Health Check**: `https://your-repl.your-username.repl.co/health`

## 🧪 Neler Test Edebilirsiniz?

### Ana Sayfadan (Web UI):
1. **AI İçerik Üretimi**
   - Hashtag oluştur
   - Pin açıklaması yaz
   - Başlık önerileri al

2. **CEO Chatbot**
   - Pinterest stratejisi sor
   - Büyüme planı al

3. **Pinterest API**
   - Profil bilgisi
   - Board'ları gör

### API Docs'tan (/docs):
Tüm endpoint'leri interaktif test edin!

## 📝 Örnek İstekler

### Hashtag Üret
```bash
curl -X POST https://your-repl.repl.co/api/v1/ai/generate/hashtags \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Healthy Breakfast",
    "keywords": ["breakfast", "healthy"],
    "count": 10
  }'
```

### Chatbot ile Konuş
```bash
curl -X POST https://your-repl.repl.co/api/v1/chatbot/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Pinterest için 5 öneri ver"
  }'
```

## 🔧 Sorun Giderme

### "Can't find module" hatası
Repl'i yeniden başlatın (Stop → Run)

### API key hatası
Secrets'ı doğru eklediğinizden emin olun

### Port hatası
Otomatik port atanır, değiştirmeye gerek yok

## 🌟 Özellikler

✅ **Çalışan Özellikler:**
- OpenAI GPT-4 entegrasyonu
- Pin açıklaması/hashtag/başlık üretimi
- CEO Chatbot
- Pinterest profil bilgisi
- Trend analizi
- Büyüme stratejisi

✅ **Demo Modu:**
- Pinterest API gerçek veya demo data
- Database yok, direkt API test
- Hızlı ve basit

## 💡 Sonraki Adımlar

1. **Share Repl**: Replit'te "Share" butonuna tıklayarak link alın
2. **Always On**: Replit'in "Always On" özelliği ile 7/24 çalışır
3. **Custom Domain**: Kendi domain'inizi bağlayın

## 🚀 Production'a Geçiş

Demo yeterli gelmezse:

1. **Full Stack Deploy:**
   - Frontend: Vercel
   - Backend: Railway/Render
   - Database: Supabase (already configured!)

2. **Docker Deploy:**
   ```bash
   docker-compose up -d
   ```

## 📚 Dokümantasyon

- **QUICK_START.md** - Lokal kurulum
- **API_INTEGRATION.md** - API kullanım rehberi
- **README.md** - Genel bakış

---

**🎉 Hazırsınız! Replit'te test edin!**
