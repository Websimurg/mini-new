import Link from 'next/link'
import { ArrowRight, Zap, TrendingUp, Calendar, MessageSquare } from 'lucide-react'

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-pink-50 via-white to-red-50">
      {/* Header */}
      <header className="container mx-auto px-4 py-6">
        <nav className="flex justify-between items-center">
          <div className="text-2xl font-bold text-pinterest-red">
            Pinterest Growth Platform
          </div>
          <div className="space-x-4">
            <Link href="/login" className="text-gray-700 hover:text-pinterest-red">
              Giriş
            </Link>
            <Link
              href="/signup"
              className="bg-pinterest-red text-white px-6 py-2 rounded-full hover:bg-pinterest-red-hover transition"
            >
              Başla
            </Link>
          </div>
        </nav>
      </header>

      {/* Hero Section */}
      <section className="container mx-auto px-4 py-20 text-center">
        <h1 className="text-6xl font-bold text-gray-900 mb-6">
          Pinterest Hesabını
          <br />
          <span className="text-pinterest-red">Otomatik Büyüt</span>
        </h1>
        <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
          AI destekli içerik üretimi, otomatik planlama ve akıllı analitik ile Pinterest hesabını büyütmenin en kolay yolu.
        </p>
        <Link
          href="/dashboard"
          className="inline-flex items-center gap-2 bg-pinterest-red text-white px-8 py-4 rounded-full text-lg font-semibold hover:bg-pinterest-red-hover transition"
        >
          Hemen Başla
          <ArrowRight className="w-5 h-5" />
        </Link>
      </section>

      {/* Features */}
      <section className="container mx-auto px-4 py-20">
        <h2 className="text-4xl font-bold text-center mb-16">Özellikler</h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          <FeatureCard
            icon={<Zap className="w-12 h-12 text-pinterest-red" />}
            title="AI İçerik Üretimi"
            description="Otomatik pin görselleri, başlık ve açıklamalar oluştur. SEO optimizasyonlu içerikler."
          />
          <FeatureCard
            icon={<Calendar className="w-12 h-12 text-pinterest-red" />}
            title="Akıllı Planlama"
            description="Blog'larını otomatik pin'e dönüştür. RSS feed entegrasyonu ve zamanlama."
          />
          <FeatureCard
            icon={<TrendingUp className="w-12 h-12 text-pinterest-red" />}
            title="Otomasyon"
            description="Toplu pin yükleme, otomatik paylaşım, hashtag optimizasyonu."
          />
          <FeatureCard
            icon={<MessageSquare className="w-12 h-12 text-pinterest-red" />}
            title="CEO Chatbot"
            description="AI asistanın ile strateji geliştir, analitik yorumla, tavsiyeleri al."
          />
        </div>
      </section>

      {/* CTA */}
      <section className="container mx-auto px-4 py-20 text-center">
        <div className="bg-pinterest-red text-white rounded-3xl p-12">
          <h2 className="text-4xl font-bold mb-4">
            Hemen Pinterest Büyütmeye Başla
          </h2>
          <p className="text-xl mb-8 opacity-90">
            Ücretsiz dene, kredi kartı gerektirmez
          </p>
          <Link
            href="/signup"
            className="inline-block bg-white text-pinterest-red px-8 py-4 rounded-full text-lg font-semibold hover:bg-gray-100 transition"
          >
            Ücretsiz Başla
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer className="container mx-auto px-4 py-8 text-center text-gray-600 border-t">
        <p>&copy; 2024 Pinterest Growth Platform. Tüm hakları saklıdır.</p>
      </footer>
    </main>
  )
}

function FeatureCard({
  icon,
  title,
  description,
}: {
  icon: React.ReactNode
  title: string
  description: string
}) {
  return (
    <div className="bg-white p-8 rounded-2xl shadow-lg hover:shadow-xl transition">
      <div className="mb-4">{icon}</div>
      <h3 className="text-xl font-bold mb-3">{title}</h3>
      <p className="text-gray-600">{description}</p>
    </div>
  )
}
