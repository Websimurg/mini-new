'use client'

import { useState } from 'react'
import { Sparkles, Image as ImageIcon, Hash, Type } from 'lucide-react'
import { aiService } from '@/lib/api'
import toast from 'react-hot-toast'

export default function AIContentGenerator() {
  const [activeTab, setActiveTab] = useState<'description' | 'image' | 'hashtags' | 'titles'>('description')
  const [loading, setLoading] = useState(false)

  return (
    <div>
      <div className="mb-6">
        <h1 className="text-3xl font-bold mb-2">AI İçerik Üretimi</h1>
        <p className="text-gray-600">
          Pinterest için SEO optimizasyonlu içerik ve görseller oluştur
        </p>
      </div>

      {/* Tabs */}
      <div className="flex gap-2 mb-6">
        <TabButton
          icon={<Type size={20} />}
          label="Açıklama"
          active={activeTab === 'description'}
          onClick={() => setActiveTab('description')}
        />
        <TabButton
          icon={<Sparkles size={20} />}
          label="Başlık"
          active={activeTab === 'titles'}
          onClick={() => setActiveTab('titles')}
        />
        <TabButton
          icon={<Hash size={20} />}
          label="Hashtag"
          active={activeTab === 'hashtags'}
          onClick={() => setActiveTab('hashtags')}
        />
        <TabButton
          icon={<ImageIcon size={20} />}
          label="Görsel"
          active={activeTab === 'image'}
          onClick={() => setActiveTab('image')}
        />
      </div>

      {/* Content */}
      <div className="bg-white rounded-xl shadow-sm p-6">
        {activeTab === 'description' && <DescriptionGenerator />}
        {activeTab === 'titles' && <TitleGenerator />}
        {activeTab === 'hashtags' && <HashtagGenerator />}
        {activeTab === 'image' && <ImageGenerator />}
      </div>
    </div>
  )
}

function TabButton({
  icon,
  label,
  active,
  onClick,
}: {
  icon: React.ReactNode
  label: string
  active: boolean
  onClick: () => void
}) {
  return (
    <button
      onClick={onClick}
      className={`flex items-center gap-2 px-6 py-3 rounded-lg transition ${
        active
          ? 'bg-pinterest-red text-white'
          : 'bg-white text-gray-700 hover:bg-gray-100'
      }`}
    >
      {icon}
      <span className="font-medium">{label}</span>
    </button>
  )
}

function DescriptionGenerator() {
  const [topic, setTopic] = useState('')
  const [keywords, setKeywords] = useState('')
  const [result, setResult] = useState('')
  const [loading, setLoading] = useState(false)

  const generate = async () => {
    if (!topic || !keywords) {
      toast.error('Lütfen tüm alanları doldurun')
      return
    }

    setLoading(true)
    try {
      const response = await aiService.generateDescription({
        topic,
        keywords: keywords.split(',').map((k) => k.trim()),
        tone: 'engaging',
        length: 'medium',
      })
      setResult(response.data.description)
      toast.success('Açıklama oluşturuldu!')
    } catch (error) {
      toast.error('Bir hata oluştu')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <h2 className="text-xl font-bold mb-4">Pin Açıklaması Oluştur</h2>
      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium mb-2">Konu</label>
          <input
            type="text"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            placeholder="Örn: Sağlıklı kahvaltı tarifleri"
            className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-pinterest-red"
          />
        </div>
        <div>
          <label className="block text-sm font-medium mb-2">
            Anahtar Kelimeler (virgülle ayırın)
          </label>
          <input
            type="text"
            value={keywords}
            onChange={(e) => setKeywords(e.target.value)}
            placeholder="Örn: kahvaltı, sağlıklı, tarifler"
            className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-pinterest-red"
          />
        </div>
        <button
          onClick={generate}
          disabled={loading}
          className="px-6 py-3 bg-pinterest-red text-white rounded-lg hover:bg-pinterest-red-hover transition disabled:opacity-50"
        >
          {loading ? 'Oluşturuluyor...' : 'Açıklama Oluştur'}
        </button>
        {result && (
          <div className="mt-4 p-4 bg-gray-50 rounded-lg">
            <p className="text-sm font-medium mb-2">Oluşturulan Açıklama:</p>
            <p className="whitespace-pre-wrap">{result}</p>
          </div>
        )}
      </div>
    </div>
  )
}

function TitleGenerator() {
  return (
    <div>
      <h2 className="text-xl font-bold mb-4">Başlık Oluştur</h2>
      <p className="text-gray-600">Başlık oluşturma özelliği yakında...</p>
    </div>
  )
}

function HashtagGenerator() {
  return (
    <div>
      <h2 className="text-xl font-bold mb-4">Hashtag Oluştur</h2>
      <p className="text-gray-600">Hashtag oluşturma özelliği yakında...</p>
    </div>
  )
}

function ImageGenerator() {
  return (
    <div>
      <h2 className="text-xl font-bold mb-4">Görsel Oluştur</h2>
      <p className="text-gray-600">Görsel oluşturma özelliği yakında...</p>
    </div>
  )
}
