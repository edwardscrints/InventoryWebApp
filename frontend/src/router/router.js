// Configuración del Rutas, incluyendo vista principal
// Created By: Edward Acosta

import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path: '/',
        name: 'home',
        redirect: '/productos'
    },
    {
        path: '/productos',
        name: 'productos',
        //Solo se descarga si se invoca la ruta
        component: () => import('../views/ProductsView.vue')
    }
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
})

export default router