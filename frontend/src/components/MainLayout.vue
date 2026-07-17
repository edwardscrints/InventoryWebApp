<template>
  <div class="layout-container">
    <!-- Menú Lateral (Sidebar) -->
    <aside :class="['sidebar', { collapsed: isCollapsed }]">
      <div class="logo" @click="toggleSidebar" title="Contraer/Expandir menú">
        <h2 v-if="!isCollapsed">Assisprex</h2>
        <h2 v-else>A</h2>
      </div>
      <nav>
        <router-link to="/productos" class="nav-link"> 
          <span class="icon">📦</span>
          <span v-if="!isCollapsed" class="text">Productos</span>
        </router-link>
      </nav>
    </aside>

    <!-- Vista Principal -->
    <div class="main-content">
      <!-- Barra de Navegación de Cabecera-->
      <header class="navbar">
        <div class="navbar-title-container">
          <div class="navbar-title">Panel de Administración</div>
        </div>
        <div class="user-profile-container">
          <div class="user-profile" @click="toggleProfileMenu">Hola, Admin ▼</div>
          
          <div v-if="isProfileMenuOpen" class="profile-menu">
            <div class="profile-header">Usuario: Admin</div>
            <button class="profile-btn" @click="handleAction">Editar usuario</button>
            <button class="profile-btn text-red" @click="handleAction">Cerrar Sesión</button>
          </div>
        </div>
      </header>

      <!-- vistas -->
      <main class="page-content">
        <slot></slot>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useToast } from '../composables/useToast'

const isCollapsed = ref(false)
const isProfileMenuOpen = ref(false)

const { showToast } = useToast()

const toggleSidebar = () => {
  isCollapsed.value = !isCollapsed.value
}

const toggleProfileMenu = () => {
  isProfileMenuOpen.value = !isProfileMenuOpen.value
}

const handleAction = () => {
  showToast('No tienes permisos para ejecutar esta acción.', 'error')
  isProfileMenuOpen.value = false
}

onMounted(() => {
  setTimeout(() => {
    isCollapsed.value = true
  }, 3000)
})
</script>

<style scoped>
.layout-container {
  display: flex;
  height: 100vh;
}

.sidebar {
  width: 250px;
  background-color: #2c3e50;
  color: white;
  display: flex;
  flex-direction: column;
  transition: width 0.3s ease;
}

.sidebar.collapsed {
  width: 70px;
}

.logo {
  padding: 20px;
  text-align: center;
  border-bottom: 1px solid #34495e;
  white-space: nowrap;
  overflow: hidden;
  cursor: pointer;
  user-select: none;
  transition: background-color 0.2s;
}

.logo:hover {
  background-color: #34495e;
}

.nav-link {
  display: flex;
  align-items: center;
  padding: 15px 20px;
  color: #ecf0f1;
  text-decoration: none;
  transition: background 0.3s, padding 0.3s;
  white-space: nowrap;
  overflow: hidden;
}

.icon {
  margin-right: 10px;
  font-size: 1.2em;
}

.sidebar.collapsed .nav-link {
  padding: 15px;
  justify-content: center;
}

.sidebar.collapsed .icon {
  margin-right: 0;
}

.nav-link:hover, .nav-link.router-link-active {
  background-color: #34495e;
  border-left: 4px solid #3498db;
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  background-color: #f4f6f8;
}

.navbar {
  background-color: white;
  padding: 15px 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  overflow: hidden;
}

.navbar-title-container {
  flex: 1;
  overflow: hidden;
  margin-right: 20px;
}

.navbar-title {
  display: inline-block;
  white-space: nowrap;
  font-weight: 600;
  font-size: 1.1em;
  color: #2c3e50;
  animation: slide-right 10s linear infinite;
}

@keyframes slide-right {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}

.page-content {
  padding: 30px;
  flex: 1;
  overflow-y: auto;
}

.user-profile-container {
  position: relative;
}

.user-profile {
  cursor: pointer;
  user-select: none;
  font-weight: 500;
  padding: 8px 12px;
  border-radius: 4px;
  transition: background-color 0.2s;
}

.user-profile:hover {
  background-color: #f1f3f5;
}

.profile-menu {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: 5px;
  background: white;
  border: 1px solid #eee;
  border-radius: 8px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  width: 200px;
  z-index: 100;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.profile-header {
  padding: 15px;
  border-bottom: 1px solid #eee;
  font-weight: 600;
  color: #2c3e50;
  background-color: #f8f9fa;
}

.profile-btn {
  padding: 12px 15px;
  border: none;
  background: none;
  text-align: left;
  cursor: pointer;
  font-size: 0.95em;
  transition: background-color 0.2s;
  color: #34495e;
}

.profile-btn:hover {
  background-color: #f1f3f5;
}

.text-red {
  color: #e74c3c;
}
</style>