import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:5000',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
})

api.interceptors.request.use(config => {
  const token = localStorage.getItem('token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

api.interceptors.response.use(
  res => res,
  err => {
    if (err.response?.status === 401) {
      console.warn('Token expired or not authorized')
    }
    return Promise.reject(err)
  }
)

export default api
