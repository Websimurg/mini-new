'use client'

import { useState } from 'react'
import {
  LayoutDashboard,
  Image,
  Calendar,
  TrendingUp,
  MessageSquare,
  Settings,
  LogOut
} from 'lucide-react'
import ChatbotCEO from '@/components/ChatbotCEO'
import AIContentGenerator from '@/components/AIContentGenerator'
import ContentScheduler from '@/components/ContentScheduler'
import AnalyticsDashboard from '@/components/AnalyticsDashboard'

type Tab = 'overview' | 'ai-content' | 'scheduler' | 'analytics' | 'chatbot'

export default function Dashboard() {
  const [activeTab, setActiveTab] = useState<Tab>('overview')

  return (
    <div className="flex h-screen bg-gray-50">
      {/* Sidebar */}
      <aside className="w-64 bg-white border-r border-gray-200">
        <div className="p-6">
          <h1 className="text-xl font-bold text-pinterest-red">
            Pinterest Growth
          </h1>
        </div>

        <nav className="px-4 space-y-2">
          <NavItem
            icon={<LayoutDashboard size={20} />}
            label="Genel Bakış"
            active={activeTab === 'overview'}
            onClick={() => setActiveTab('overview')}
          />
          <NavItem
            icon={<Image size={20} />}
            label="AI İçerik"
            active={activeTab === 'ai-content'}
            onClick={() => setActiveTab('ai-content')}
          />
          <NavItem
            icon={<Calendar size={20} />}
            label="Planlama"
            active={activeTab === 'scheduler'}
            onClick={() => setActiveTab('scheduler')}
          />
          <NavItem
            icon={<TrendingUp size={20} />}
            label="Analitik"
            active={activeTab === 'analytics'}
            onClick={() => setActiveTab('analytics')}
          />
          <NavItem
            icon={<MessageSquare size={20} />}
            label="CEO Asistan"
            active={activeTab === 'chatbot'}
            onClick={() => setActiveTab('chatbot')}
          />
        </nav>

        <div className="absolute bottom-0 w-64 p-4 border-t">
          <NavItem
            icon={<Settings size={20} />}
            label="Ayarlar"
            onClick={() => {}}
          />
          <NavItem
            icon={<LogOut size={20} />}
            label="Çıkış"
            onClick={() => {}}
          />
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto">
        <div className="p-8">
          {activeTab === 'overview' && <OverviewTab />}
          {activeTab === 'ai-content' && <AIContentGenerator />}
          {activeTab === 'scheduler' && <ContentScheduler />}
          {activeTab === 'analytics' && <AnalyticsDashboard />}
          {activeTab === 'chatbot' && <ChatbotCEO />}
        </div>
      </main>
    </div>
  )
}

function NavItem({
  icon,
  label,
  active = false,
  onClick,
}: {
  icon: React.ReactNode
  label: string
  active?: boolean
  onClick: () => void
}) {
  return (
    <button
      onClick={onClick}
      className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg transition ${
        active
          ? 'bg-pinterest-red text-white'
          : 'text-gray-700 hover:bg-gray-100'
      }`}
    >
      {icon}
      <span className="font-medium">{label}</span>
    </button>
  )
}

function OverviewTab() {
  return (
    <div>
      <h1 className="text-3xl font-bold mb-8">Genel Bakış</h1>

      <div className="grid md:grid-cols-3 gap-6 mb-8">
        <StatCard
          title="Toplam Pin"
          value="245"
          change="+12%"
          positive
        />
        <StatCard
          title="Aylık Görüntüleme"
          value="125K"
          change="+28%"
          positive
        />
        <StatCard
          title="Takipçi"
          value="8.5K"
          change="+15%"
          positive
        />
      </div>

      <div className="bg-white rounded-xl p-6 shadow-sm">
        <h2 className="text-xl font-bold mb-4">Hoş Geldiniz!</h2>
        <p className="text-gray-600 mb-4">
          Pinterest Growth Platform'a hoş geldiniz. Sol menüden istediğiniz özelliğe ulaşabilirsiniz:
        </p>
        <ul className="space-y-2 text-gray-600">
          <li>• <strong>AI İçerik:</strong> Otomatik pin görseli ve içerik oluştur</li>
          <li>• <strong>Planlama:</strong> İçeriklerini planla ve zamanla</li>
          <li>• <strong>Analitik:</strong> Performansını takip et</li>
          <li>• <strong>CEO Asistan:</strong> AI ile strateji geliştir</li>
        </ul>
      </div>
    </div>
  )
}

function StatCard({
  title,
  value,
  change,
  positive = true,
}: {
  title: string
  value: string
  change: string
  positive?: boolean
}) {
  return (
    <div className="bg-white rounded-xl p-6 shadow-sm">
      <p className="text-gray-600 text-sm mb-2">{title}</p>
      <p className="text-3xl font-bold mb-2">{value}</p>
      <p className={positive ? 'text-green-600' : 'text-red-600'}>
        {change} son 30 gün
      </p>
    </div>
  )
}
