// Inyeccion de Pinia y preparacion de vue
// Created By. Ing Edward Acosta
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

// Importaremos el router en el siguiente paso
// import router from './router' 

const app = createApp(App)
const pinia = createPinia()

// Inyectamos las dependencias
app.use(pinia)
// app.use(router) // Lo descomentaremos en breve

app.mount('#app')