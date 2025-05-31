import api from './axios'

export const reserveTicket = signedTx =>
  api.post('/reserveEvent', { signedTx })

export const checkResult = contractAddress =>
  api.get(`/checkResult?contractAddress=${contractAddress}`)