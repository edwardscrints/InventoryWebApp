// Instancia de Axios para las peticiones a la API
// Created By. Ing Edward Acosta

import axios from 'axios';

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
    headers: {
        'Content-Type': 'application/json',
    },
});


api.interceptors.response.use(
    (response) => response,
    (error) => {
        console.error('Error en la API:', error.response?.data || error.message);
        // Notificaciones globales
        return Promise.reject(error);
    }
);

export default api;