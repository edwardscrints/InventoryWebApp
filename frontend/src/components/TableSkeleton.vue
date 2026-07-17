<template>
  <div class="skeleton-container">
    <table class="data-table">
      <thead>
        <tr>
          <!-- 7 columnas -->
          <th v-for="i in 7" :key="i">
            <div class="skeleton skeleton-header"></div>
          </th>
        </tr>
      </thead>
      <tbody>
        <!--7 filas -->
        <tr v-for="row in 7" :key="row">
          <td v-for="col in 7" :key="col">
            <div class="skeleton skeleton-text"></div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.data-table {
  width: 100%;
  border-collapse: collapse;
}

.data-table th, .data-table td {
  padding: 15px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.skeleton {
  background: #e0e0e0;
  border-radius: 4px;
  animation: pulse 1.5s infinite ease-in-out;
}

.skeleton-header {
  height: 20px;
  width: 60%;
}

.skeleton-text {
  height: 18px;
  width: 85%;
}

/* Animación */
@keyframes pulse {
  0% {
    background-color: #e2e8f0;
  }
  50% {
    background-color: #f1f5f9;
  }
  100% {
    background-color: #e2e8f0;
  }
}
</style>