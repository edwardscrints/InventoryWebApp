<template>
  <div class="layout-container">
    <!-- Menú Lateral (Sidebar) -->
    <aside class="sidebar">
      <div class="logo">
        <h2>Assisprex</h2>
      </div>
      <nav>
        <router-link to="/productos" class="nav-link"> Productos</router-link>

      </nav>
    </aside>

    <!-- Vista Principal -->
    <div class="main-content">
      <!-- Barra de Navegación de Cabecera-->
      <header class="navbar">
        <div class="navbar-title">Panel de Administración</div>
        <div class="user-profile">Hola, Admin</div>
      </header>

      <!-- vistas -->
      <main class="page-content">
        <slot></slot>
      </main>
    </div>
  </div>
</template>

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
}

.logo {
  padding: 20px;
  text-align: center;
  border-bottom: 1px solid #34495e;
}

.nav-link {
  display: block;
  padding: 15px 20px;
  color: #ecf0f1;
  text-decoration: none;
  transition: background 0.3s;
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
}

.page-content {
  padding: 30px;
  flex: 1;
  overflow-y: auto;
}
</style>