// Inyeccion de Pinia y preparacion de vue, inclusion de router
// Created By. Ing Edward Acosta
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router/router.js'

const app = createApp(App)
const pinia = createPinia()

// Dependencias
app.use(pinia)
app.use(router)

app.mount('#app')