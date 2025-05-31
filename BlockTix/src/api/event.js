import api from './axios'

export const getAllEvents = () => api.get('/events')

export const getEventById = id => api.get(`/event/${id}`)

export const deployEvent = ({ signedTx, eventName, startTime, endTime, totalTickets }) =>
    api.post('/holdEvent', {
        signedTx,
        eventName,
        startTime,
        endTime,
        totalTickets
    })
