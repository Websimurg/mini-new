#!/bin/bash

echo "=========================================="
echo "🚀 Pinterest Growth Platform Başlatılıyor"
echo "=========================================="
echo ""

# Check if .env exists
if [ ! -f "backend/.env" ]; then
    echo "⚠️  backend/.env dosyası bulunamadı!"
    echo "📝 Örnek .env dosyası oluşturuluyor..."
    cp backend/.env.example backend/.env 2>/dev/null || echo "❌ .env.example bulunamadı"
    echo "✅ Lütfen backend/.env dosyasında OpenAI API anahtarınızı yapılandırın"
    echo ""
fi

# Check OpenAI API key
if grep -q "sk-proj-demo-key" backend/.env; then
    echo "⚠️  UYARI: OpenAI API anahtarı yapılandırılmamış!"
    echo "📝 Lütfen backend/.env dosyasında OPENAI_API_KEY değerini güncelleyin"
    echo ""
fi

echo "📦 Python bağımlılıkları kontrol ediliyor..."
pip3 install -q fastapi uvicorn python-dotenv openai requests pydantic 2>/dev/null

echo "✅ Backend hazır!"
echo ""
echo "🌐 Demo Server başlatılıyor..."
echo "   📍 URL: http://localhost:8080"
echo "   📚 API Docs: http://localhost:8080/docs"
echo "   🧪 Test UI: http://localhost:8080/"
echo ""
echo "💡 Frontend için (başka bir terminalde):"
echo "   cd frontend-simple && npm install && npm run dev"
echo "   Frontend: http://localhost:5173"
echo ""
echo "=========================================="
echo ""

# Start the demo server
python3 demo_server.py
