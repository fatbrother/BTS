import api from './axios'

export const register = address =>
  api.post('/register', { address })

export const login = async address => {
  const res = await api.post('/login', { address })
  const token = res.data.access_token
  localStorage.setItem('token', token)
  return token
}
