// API Base URL
const API_URL = 'http://localhost:8080/api/v1'

// Tab Switching
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        // Remove active class from all tabs
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'))
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'))

        // Add active class to clicked tab
        btn.classList.add('active')
        const tabId = btn.getAttribute('data-tab')
        document.getElementById(tabId).classList.add('active')
    })
})

// Utility Functions
function showLoading(elementId) {
    const el = document.getElementById(elementId)
    el.innerHTML = '<div class="loading">⏳ Yükleniyor...</div>'
    el.style.display = 'block'
}

function showError(elementId, message) {
    const el = document.getElementById(elementId)
    el.innerHTML = `<div class="error">❌ Hata: ${message}</div>`
    el.style.display = 'block'
}

function showSuccess(elementId, content) {
    const el = document.getElementById(elementId)
    el.innerHTML = `<div class="success">${content}</div>`
    el.style.display = 'block'
}

// API Status Check
async function checkAPIStatus() {
    try {
        const response = await fetch('http://localhost:8080/health')
        const statusEl = document.getElementById('api-status')
        if (response.ok) {
            statusEl.style.color = '#10b981'
            statusEl.title = 'API çalışıyor'
        } else {
            statusEl.style.color = '#ef4444'
            statusEl.title = 'API bağlantı hatası'
        }
    } catch (error) {
        const statusEl = document.getElementById('api-status')
        statusEl.style.color = '#ef4444'
        statusEl.title = 'API bağlantı hatası: ' + error.message
    }
}

// Check API status on load and every 30 seconds
checkAPIStatus()
setInterval(checkAPIStatus, 30000)

// ============================================================================
// AI Content Generation Functions
// ============================================================================

window.generateDescription = async function() {
    const topic = document.getElementById('desc-topic').value
    const keywords = document.getElementById('desc-keywords').value.split(',').map(k => k.trim())
    const tone = document.getElementById('desc-tone').value

    if (!topic || keywords.length === 0) {
        showError('desc-result', 'Lütfen konu ve anahtar kelimeleri girin')
        return
    }

    showLoading('desc-result')

    try {
        const response = await fetch(`${API_URL}/ai/generate/description`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic, keywords, tone, length: 'medium' })
        })

        if (!response.ok) {
            const error = await response.json()
            throw new Error(error.detail || 'API hatası')
        }

        const data = await response.json()
        showSuccess('desc-result', `
            <h4>✅ Pin Açıklaması:</h4>
            <div class="generated-content">${data.description}</div>
            <button class="btn-secondary" onclick="navigator.clipboard.writeText(\`${data.description.replace(/`/g, '\\`')}\`)">
                📋 Kopyala
            </button>
        `)
    } catch (error) {
        showError('desc-result', error.message)
    }
}

window.generateTitles = async function() {
    const topic = document.getElementById('title-topic').value
    const keywords = document.getElementById('title-keywords').value.split(',').map(k => k.trim())
    const count = parseInt(document.getElementById('title-count').value)

    if (!topic || keywords.length === 0) {
        showError('title-result', 'Lütfen konu ve anahtar kelimeleri girin')
        return
    }

    showLoading('title-result')

    try {
        const response = await fetch(`${API_URL}/ai/generate/titles`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic, keywords, count })
        })

        if (!response.ok) {
            const error = await response.json()
            throw new Error(error.detail || 'API hatası')
        }

        const data = await response.json()
        const titlesHTML = data.titles.map((title, i) =>
            `<div class="title-item">
                <strong>${i + 1}.</strong> ${title}
                <button class="btn-copy" onclick="navigator.clipboard.writeText('${title}')">📋</button>
            </div>`
        ).join('')

        showSuccess('title-result', `
            <h4>✅ Başlık Önerileri:</h4>
            <div class="titles-list">${titlesHTML}</div>
        `)
    } catch (error) {
        showError('title-result', error.message)
    }
}

window.generateHashtags = async function() {
    const topic = document.getElementById('hashtag-topic').value
    const keywords = document.getElementById('hashtag-keywords').value.split(',').map(k => k.trim())
    const count = parseInt(document.getElementById('hashtag-count').value)

    if (!topic || keywords.length === 0) {
        showError('hashtag-result', 'Lütfen konu ve anahtar kelimeleri girin')
        return
    }

    showLoading('hashtag-result')

    try {
        const response = await fetch(`${API_URL}/ai/generate/hashtags`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic, keywords, count })
        })

        if (!response.ok) {
            const error = await response.json()
            throw new Error(error.detail || 'API hatası')
        }

        const data = await response.json()
        const hashtagsText = data.hashtags.join(' ')

        showSuccess('hashtag-result', `
            <h4>✅ Hashtagler:</h4>
            <div class="hashtags">${hashtagsText}</div>
            <button class="btn-secondary" onclick="navigator.clipboard.writeText('${hashtagsText}')">
                📋 Tümünü Kopyala
            </button>
        `)
    } catch (error) {
        showError('hashtag-result', error.message)
    }
}

// ============================================================================
// Chatbot Functions
// ============================================================================

let conversationHistory = []

window.sendChatMessage = async function() {
    const input = document.getElementById('chat-input')
    const message = input.value.trim()

    if (!message) return

    // Add user message to chat
    const chatContainer = document.getElementById('chat-messages')
    chatContainer.innerHTML += `
        <div class="chat-message user">
            <strong>Siz:</strong> ${message}
        </div>
    `

    // Clear input
    input.value = ''

    // Show loading
    chatContainer.innerHTML += `
        <div class="chat-message bot loading-msg">
            <strong>CEO Bot:</strong> ⏳ Düşünüyor...
        </div>
    `
    chatContainer.scrollTop = chatContainer.scrollHeight

    try {
        const response = await fetch(`${API_URL}/chatbot/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                message,
                conversation_history: conversationHistory
            })
        })

        if (!response.ok) {
            throw new Error('API hatası')
        }

        const data = await response.json()

        // Remove loading message
        document.querySelector('.loading-msg')?.remove()

        // Add bot response
        chatContainer.innerHTML += `
            <div class="chat-message bot">
                <strong>CEO Bot:</strong> ${data.response}
            </div>
        `

        // Update conversation history
        conversationHistory.push(
            { role: 'user', content: message },
            { role: 'assistant', content: data.response }
        )

        chatContainer.scrollTop = chatContainer.scrollHeight
    } catch (error) {
        document.querySelector('.loading-msg')?.remove()
        chatContainer.innerHTML += `
            <div class="chat-message bot error">
                <strong>CEO Bot:</strong> ❌ Üzgünüm, bir hata oluştu: ${error.message}
            </div>
        `
    }
}

window.createStrategy = async function() {
    const niche = document.getElementById('strategy-niche').value
    const current = parseInt(document.getElementById('strategy-current').value)
    const target = parseInt(document.getElementById('strategy-target').value)
    const months = parseInt(document.getElementById('strategy-months').value)

    if (!niche) {
        showError('strategy-result', 'Lütfen niche alanını doldurun')
        return
    }

    showLoading('strategy-result')

    try {
        const response = await fetch(`${API_URL}/chatbot/create-strategy`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                niche,
                current_followers: current,
                target_followers: target,
                timeline_months: months
            })
        })

        if (!response.ok) {
            throw new Error('API hatası')
        }

        const data = await response.json()

        showSuccess('strategy-result', `
            <h4>✅ Büyüme Stratejisi:</h4>
            <div class="strategy-content">
                <pre>${JSON.stringify(data, null, 2)}</pre>
            </div>
        `)
    } catch (error) {
        showError('strategy-result', error.message)
    }
}

// ============================================================================
// Trends Functions
// ============================================================================

window.analyzeTrends = async function() {
    const niche = document.getElementById('trend-niche').value

    if (!niche) {
        showError('trend-result', 'Lütfen bir niche girin')
        return
    }

    showLoading('trend-result')

    try {
        const response = await fetch(`${API_URL}/ai/trends/${encodeURIComponent(niche)}`)

        if (!response.ok) {
            throw new Error('API hatası')
        }

        const data = await response.json()

        showSuccess('trend-result', `
            <h4>✅ Trend Analizi: ${niche}</h4>
            <div class="trend-content">
                <pre>${JSON.stringify(data, null, 2)}</pre>
            </div>
        `)
    } catch (error) {
        showError('trend-result', error.message)
    }
}

// ============================================================================
// Pinterest Profile Functions
// ============================================================================

window.getProfile = async function() {
    showLoading('profile-result')

    try {
        const response = await fetch(`${API_URL}/pinterest/profile`)

        if (!response.ok) {
            throw new Error('API hatası')
        }

        const data = await response.json()

        showSuccess('profile-result', `
            <h4>✅ Pinterest Profil:</h4>
            <div class="profile-content">
                <pre>${JSON.stringify(data, null, 2)}</pre>
            </div>
        `)
    } catch (error) {
        showError('profile-result', error.message)
    }
}

window.getBoards = async function() {
    showLoading('boards-result')

    try {
        const response = await fetch(`${API_URL}/pinterest/boards`)

        if (!response.ok) {
            throw new Error('API hatası')
        }

        const data = await response.json()

        showSuccess('boards-result', `
            <h4>✅ Pinterest Boards:</h4>
            <div class="boards-content">
                <pre>${JSON.stringify(data, null, 2)}</pre>
            </div>
        `)
    } catch (error) {
        showError('boards-result', error.message)
    }
}

console.log('🚀 Pinterest Growth Platform - Frontend yüklendi!')
console.log('API URL:', API_URL)
