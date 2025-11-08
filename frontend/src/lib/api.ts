import axios from 'axios'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export const api = axios.create({
  baseURL: `${API_URL}/api/v1`,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor for auth token
api.interceptors.request.use((config) => {
  if (typeof window !== 'undefined') {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
  }
  return config
})

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized
      if (typeof window !== 'undefined') {
        localStorage.removeItem('token')
        window.location.href = '/login'
      }
    }
    return Promise.reject(error)
  }
)

// API Services
export const aiService = {
  generateDescription: (data: any) => api.post('/ai/generate/description', data),
  generateTitles: (data: any) => api.post('/ai/generate/titles', data),
  generateHashtags: (data: any) => api.post('/ai/generate/hashtags', data),
  generateImage: (data: any) => api.post('/ai/generate/image', data),
  optimizeContent: (data: any) => api.post('/ai/optimize', data),
  getContentIdeas: (data: any) => api.post('/ai/ideas', data),
  getTrends: (niche: string) => api.get(`/ai/trends/${niche}`),
}

export const chatbotService = {
  chat: (data: any) => api.post('/chatbot/chat', data),
  analyzePerformance: (data: any) => api.post('/chatbot/analyze-performance', data),
  createStrategy: (data: any) => api.post('/chatbot/create-strategy', data),
  reviewContent: (data: any) => api.post('/chatbot/review-content', data),
  getDailyTasks: (data: any) => api.post('/chatbot/daily-tasks', data),
  ask: (question: string, context?: any) =>
    api.post('/chatbot/ask', null, { params: { question, context } }),
}

export const pinterestService = {
  getBoards: () => api.get('/pinterest/boards'),
  createBoard: (data: any) => api.post('/pinterest/boards', data),
  getProfile: () => api.get('/pinterest/profile'),
}

export const pinsService = {
  getPins: () => api.get('/pins'),
  createPin: (data: any) => api.post('/pins', data),
  deletePin: (id: number) => api.delete(`/pins/${id}`),
}

export const schedulerService = {
  getScheduledPins: () => api.get('/scheduler/scheduled'),
  schedulePin: (data: any) => api.post('/scheduler/schedule', data),
}

export const analyticsService = {
  getOverview: () => api.get('/analytics/overview'),
  getPinAnalytics: (pinId: string) => api.get(`/analytics/pin/${pinId}`),
}
