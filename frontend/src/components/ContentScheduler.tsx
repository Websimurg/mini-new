'use client'

import { useState } from 'react'
import { Calendar, Clock, Plus } from 'lucide-react'

export default function ContentScheduler() {
  return (
    <div>
      <div className="mb-6 flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold mb-2">İçerik Planlama</h1>
          <p className="text-gray-600">
            Pinlerinizi planlayın ve zamanla
          </p>
        </div>
        <button className="flex items-center gap-2 px-6 py-3 bg-pinterest-red text-white rounded-lg hover:bg-pinterest-red-hover transition">
          <Plus size={20} />
          Yeni Plan
        </button>
      </div>

      <div className="grid md:grid-cols-2 gap-6">
        {/* Calendar View */}
        <div className="bg-white rounded-xl shadow-sm p-6">
          <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
            <Calendar size={24} />
            Takvim
          </h2>
          <div className="text-center py-12 text-gray-500">
            Takvim görünümü yakında...
          </div>
        </div>

        {/* Scheduled Pins */}
        <div className="bg-white rounded-xl shadow-sm p-6">
          <h2 className="text-xl font-bold mb-4 flex items-center gap-2">
            <Clock size={24} />
            Zamanlanmış Pinler
          </h2>
          <div className="space-y-4">
            <ScheduledPinItem
              title="Sağlıklı Kahvaltı Tarifleri"
              date="15 Ocak 2024, 14:00"
              status="pending"
            />
            <ScheduledPinItem
              title="Ev Dekorasyonu Fikirleri"
              date="16 Ocak 2024, 09:00"
              status="pending"
            />
            <ScheduledPinItem
              title="DIY Projeler"
              date="17 Ocak 2024, 16:00"
              status="pending"
            />
          </div>
        </div>
      </div>
    </div>
  )
}

function ScheduledPinItem({
  title,
  date,
  status,
}: {
  title: string
  date: string
  status: 'pending' | 'published' | 'failed'
}) {
  const statusColors = {
    pending: 'bg-yellow-100 text-yellow-800',
    published: 'bg-green-100 text-green-800',
    failed: 'bg-red-100 text-red-800',
  }

  const statusLabels = {
    pending: 'Bekliyor',
    published: 'Yayınlandı',
    failed: 'Başarısız',
  }

  return (
    <div className="p-4 border border-gray-200 rounded-lg hover:border-pinterest-red transition">
      <div className="flex justify-between items-start mb-2">
        <h3 className="font-semibold">{title}</h3>
        <span
          className={`px-2 py-1 rounded-full text-xs font-medium ${statusColors[status]}`}
        >
          {statusLabels[status]}
        </span>
      </div>
      <p className="text-sm text-gray-600">{date}</p>
    </div>
  )
}
