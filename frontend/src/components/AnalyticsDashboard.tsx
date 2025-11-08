'use client'

import { BarChart, TrendingUp, Eye, Heart, MousePointer } from 'lucide-react'

export default function AnalyticsDashboard() {
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-3xl font-bold mb-2">Analitik</h1>
        <p className="text-gray-600">
          Pinterest performansınızı takip edin
        </p>
      </div>

      {/* Stats Grid */}
      <div className="grid md:grid-cols-4 gap-6 mb-8">
        <MetricCard
          icon={<Eye className="text-blue-600" size={24} />}
          label="Görüntülenme"
          value="125,430"
          change="+28%"
          positive
        />
        <MetricCard
          icon={<Heart className="text-red-600" size={24} />}
          label="Kaydetme"
          value="8,543"
          change="+15%"
          positive
        />
        <MetricCard
          icon={<MousePointer className="text-green-600" size={24} />}
          label="Tıklama"
          value="2,145"
          change="+32%"
          positive
        />
        <MetricCard
          icon={<TrendingUp className="text-purple-600" size={24} />}
          label="Etkileşim Oranı"
          value="6.8%"
          change="+2.1%"
          positive
        />
      </div>

      {/* Charts */}
      <div className="grid md:grid-cols-2 gap-6">
        <div className="bg-white rounded-xl shadow-sm p-6">
          <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
            <BarChart size={24} />
            Performans Trendi
          </h2>
          <div className="h-64 flex items-center justify-center text-gray-500">
            Grafik gösterimi yakında...
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-sm p-6">
          <h2 className="text-xl font-bold mb-4">En İyi Performans Gösteren Pinler</h2>
          <div className="space-y-3">
            <TopPinItem
              title="Sağlıklı Kahvaltı Tarifleri"
              impressions={12543}
              saves={842}
            />
            <TopPinItem
              title="Ev Dekorasyonu Fikirleri"
              impressions={10234}
              saves={723}
            />
            <TopPinItem
              title="DIY Projeler"
              impressions={8965}
              saves={654}
            />
          </div>
        </div>
      </div>
    </div>
  )
}

function MetricCard({
  icon,
  label,
  value,
  change,
  positive,
}: {
  icon: React.ReactNode
  label: string
  value: string
  change: string
  positive: boolean
}) {
  return (
    <div className="bg-white rounded-xl shadow-sm p-6">
      <div className="flex items-center gap-3 mb-4">{icon}</div>
      <p className="text-gray-600 text-sm mb-1">{label}</p>
      <p className="text-2xl font-bold mb-2">{value}</p>
      <p className={positive ? 'text-green-600 text-sm' : 'text-red-600 text-sm'}>
        {change} son 30 gün
      </p>
    </div>
  )
}

function TopPinItem({
  title,
  impressions,
  saves,
}: {
  title: string
  impressions: number
  saves: number
}) {
  return (
    <div className="p-3 border border-gray-200 rounded-lg">
      <h3 className="font-semibold mb-2">{title}</h3>
      <div className="flex gap-4 text-sm text-gray-600">
        <span>{impressions.toLocaleString()} görüntülenme</span>
        <span>{saves.toLocaleString()} kaydetme</span>
      </div>
    </div>
  )
}
