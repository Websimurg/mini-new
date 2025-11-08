# 🚀 Replit'e 2 Dakikada Deploy Etme

Bu rehber ile Pinterest Growth Platform'u Replit'e deploy edip hemen kullanmaya başlayabilirsiniz!

## 📋 Ön Hazırlık

Sadece bir şey gerekli:
- **OpenAI API Key**: https://platform.openai.com/api-keys

## 🎯 Adım 1: Replit'e Aktar

### Yöntem 1: GitHub'dan Import (Önerilen)

1. [Replit.com](https://replit.com) hesabınıza giriş yapın
2. Sağ üstte **"+ Create Repl"** butonuna tıklayın
3. **"Import from GitHub"** sekmesini seçin
4. GitHub URL'nizi yapıştırın:
   ```
   https://github.com/Websimurg/mini-new
   ```
5. Branch'i seçin: `claude/youtube-video-clone-system-011CUv9bhiFe4VXXHD6Bbccq`
6. **"Import from GitHub"** butonuna tıklayın

### Yöntem 2: Zip Yükleme

1. Bu repo'yu zip olarak indirin
2. Replit'te "Upload Zip" seçeneğini kullanın

## 🔑 Adım 2: Secrets Ekleyin

Replit'te sol taraftaki **Tools** menüsünden **"Secrets"** sekmesini açın.

### Zorunlu Secret:

```
Key: OPENAI_API_KEY
Value: sk-proj-abc123...  (OpenAI API anahtarınız)
```

### Opsiyonel Secrets (İleri düzey):

```
PINTEREST_ACCESS_TOKEN=your_pinterest_token_here
FAL_KEY=your_fal_api_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
```

**💡 İpucu:** Sadece `OPENAI_API_KEY` ile başlayabilirsiniz!

## ▶️ Adım 3: Run!

Sağ üstteki yeşil **"Run"** butonuna basın!

İlk çalıştırmada:
- Bağımlılıklar otomatik yüklenecek (30-60 saniye)
- Server başlayacak
- Tarayıcınızda otomatik açılacak

## 🌐 Erişim

### Server başladıktan sonra:

- **Ana Sayfa/Test UI:** Replit'in verdiği URL (örn: `https://pinterest-growth.username.repl.co`)
- **API Docs:** `https://your-url.repl.co/docs`
- **Health Check:** `https://your-url.repl.co/health`

## 🎨 Test Edin!

### Ana sayfada yapabilecekleriniz:

1. **🎨 AI İçerik Üretimi**
   - Pin açıklaması oluştur
   - Başlık önerileri al
   - Hashtag üret
   - Trend analizi yap

2. **💬 CEO Chatbot**
   - Pinterest stratejisi sor
   - Büyüme planı oluştur
   - Öneriler al

3. **📊 Pinterest Entegrasyonu**
   - Profil bilgilerini gör (demo data)
   - Board'ları listele (demo data)
   - Pinterest API key ekleyince gerçek veriler

## 🔧 Sorun Giderme

### ❌ "ModuleNotFoundError" hatası
**Çözüm:** Repl'i yeniden başlatın (Stop → Run)

### ❌ "OpenAI API key hatası"
**Çözüm:**
- Secrets'ta `OPENAI_API_KEY` olduğundan emin olun
- API key'in geçerli ve kredisi olduğunu kontrol edin
- Repl'i yeniden başlatın

### ❌ "Cannot connect" hatası
**Çözüm:**
- Replit'in verdiği URL'yi kullanın
- Server'ın çalıştığından emin olun (Console'da log kontrolü)

## 📱 İleri Düzey Özellikler

### Always On (7/24 Çalışsın)

1. Repl sayfanızda **"Deployments"** sekmesine gidin
2. **"Reserved VM"** seçeneğini aktif edin
3. Repl'iniz artık 7/24 çalışır!

**Not:** Bu ücretli bir özelliktir (Replit Hacker Plan gerekir)

### Custom Domain Bağlama

1. **"Deployments"** → **"Custom Domain"**
2. Kendi domain'inizi ekleyin
3. DNS ayarlarını yapın

### Share Link

Projenizi paylaşmak için:
1. Sağ üstte **"Share"** butonuna tıklayın
2. Link'i kopyalayıp paylaşın

## 🎯 Örnek Kullanım

### Pin Açıklaması Oluştur

1. Ana sayfada **"AI İçerik"** sekmesine gidin
2. **Konu:** "Sağlıklı smoothie tarifleri"
3. **Anahtar Kelimeler:** "smoothie, sağlıklı, detoks"
4. **"Açıklama Oluştur"** butonuna tıklayın
5. Sonucu kopyalayıp Pinterest'te kullanın!

### CEO Chatbot ile Strateji

1. **"CEO Chatbot"** sekmesine gidin
2. Soru sorun: "5000 takipçiye ulaşmak için ne yapmalıyım?"
3. AI asistan size detaylı strateji verecek!

## 📊 API Endpoint Örnekleri

### cURL ile Test:

```bash
# Pin açıklaması oluştur
curl -X POST https://your-url.repl.co/api/v1/ai/generate/description \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Vegan brownie tarifi",
    "keywords": ["vegan", "brownie", "çikolatalı"],
    "tone": "friendly",
    "length": "medium"
  }'

# Hashtag üret
curl -X POST https://your-url.repl.co/api/v1/ai/generate/hashtags \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Home decor",
    "keywords": ["interior", "modern"],
    "count": 15
  }'

# CEO chatbot
curl -X POST https://your-url.repl.co/api/v1/chatbot/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Pinterest için 5 öneri ver"
  }'
```

## 🌟 Kullanılabilir Özellikler

✅ **Tam Çalışan:**
- AI içerik üretimi (OpenAI GPT-4)
- Pin açıklaması, başlık, hashtag
- CEO Chatbot
- Trend analizi
- Büyüme stratejisi

⚠️ **Demo Mod:**
- Pinterest profil/board bilgileri (demo data)
- Pinterest API key ekleyince gerçek veri

❌ **Şu An Yok:**
- Database (gelişmiş versiyonda var)
- Otomatik pin paylaşımı (manuel kullanım için)
- Kullanıcı kaydı (tek kullanıcı demo)

## 💰 Maliyet

**Replit:**
- Ücretsiz tier: Sınırlı kullanım (sleep mode)
- Hacker Plan ($7/ay): Her zaman açık, daha hızlı

**OpenAI:**
- GPT-4: ~$0.01 per request (usage-based)
- İlk $5 bedava krediniz var

## 🚀 Production için

Demo yeterli gelmezse:

### Full Stack Deploy:
```bash
# Frontend: Vercel
# Backend: Railway/Render
# Database: Supabase

# Lokal test:
docker-compose up -d
```

## 📚 Ek Kaynaklar

- **BASLATMA_KILAVUZU.md** - Lokal kurulum
- **QUICK_START.md** - Detaylı rehber
- **API_INTEGRATION.md** - API kullanımı
- **README.md** - Genel bakış

## ❓ Sık Sorulan Sorular

### Ücretsiz mi?
Evet! Replit free tier + OpenAI free credit ile başlayabilirsiniz.

### Veritabanı gerekli mi?
Hayır! Demo server veritabanı kullanmaz, direkt API çağrıları yapar.

### Pinterest hesabı bağlamak zorunlu mu?
Hayır! Demo verilerle test edebilirsiniz. İsterseniz sonra Pinterest API ekleyin.

### Mobil cihazdan kullanabilir miyim?
Evet! Replit URL'i mobil tarayıcılardan da çalışır.

---

## ✅ Hazırsınız!

Şimdi:
1. ✅ Replit'e import ettiniz
2. ✅ OpenAI API key eklediniz
3. ✅ Run butonuna bastınız
4. 🎉 **Pinterest Growth Platform çalışıyor!**

**İyi kullanımlar! 🚀**

---

**💡 Bonus:** Projeyi beğendiniz mi? GitHub'da ⭐ vermeyi unutmayın!
