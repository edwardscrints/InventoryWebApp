<template>
  <MainLayout>
    <div class="products-header">
      <h1>Gestión de Productos</h1>
      <button class="btn btn-primary" @click="openCreateModal">
        + Nuevo Producto
      </button>
    </div>

    <!-- Barra de Búsqueda -->
    <div class="search-bar">
      <input 
        type="text" 
        v-model="searchQuery" 
        @input="handleSearch"
        placeholder="Buscar por nombre o SKU..." 
        class="form-control"
      />
    </div>

    <!-- Tabla de Productos -->
    <div class="table-container">
      <div v-if="productStore.loading" class="loading">Cargando datos...</div>
      
      <table v-else class="data-table">
        <thead>
          <tr>
            <th>SKU</th>
            <th>Nombre</th>
            <th>Categoría</th>
            <th>Precio</th>
            <th>Stock</th>
            <th>Estado</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in productStore.products" :key="product.id">
            <td>{{ product.sku }}</td>
            <td>{{ product.nombre }}</td>
            <td>{{ product.categoria }}</td>
            <td>${{ product.precio }}</td>
            <td>{{ product.stock }}</td>
            <td>
              <span :class="['badge', product.estado === 'Activo' ? 'badge-active' : 'badge-inactive']">
                {{ product.estado }}
              </span>
            </td>
            <td class="actions">
             <button class="btn-icon text-blue" @click="openEditModal(product)" title="Editar">EDITAR</button>
  <button class="btn-icon text-red" title="Eliminar">ELIMINAR</button>
  <button class="btn-icon text-gray" title="Historial">HISTORIAL</button>
            </td>
          </tr>
          <tr v-if="productStore.products.length === 0">
            <td colspan="7" class="text-center">No se encontraron productos.</td>
          </tr>
        </tbody>
      </table>
    </div>
<ProductModal 
  :isOpen="isModalOpen" 
  :product="selectedProduct"
  :loading="productStore.loading"
  @close="closeModal"
  @save="handleSaveProduct"
/>
  </MainLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useProductStore } from '../stores/productStore'
import MainLayout from '../components/MainLayout.vue'
import ProductModal from '../components/ProductModal.vue'

const productStore = useProductStore()
const searchQuery = ref('')

// Estado para controlar el modal
const isModalOpen = ref(false)
const selectedProduct = ref(null)


onMounted(() => {
  productStore.fetchProducts()
})


const handleSearch = () => {
  productStore.fetchProducts(searchQuery.value)
}

const openCreateModal = () => {
  console.log("Se esta abriendo el modal de creación")
  selectedProduct.value = null 
  isModalOpen.value = true
}

const openEditModal = (product) => {
  selectedProduct.value = product
  isModalOpen.value = true
}

const closeModal = () => {
  isModalOpen.value = false
  selectedProduct.value = null
}

const handleSaveProduct = async (productData) => {
  try {
    if (selectedProduct.value) {
      // Actualizar
      await productStore.updateProduct(selectedProduct.value.id, productData)
    } else {
      // Crear
      await productStore.createProduct(productData)
    }
    closeModal()
  } catch (error) {
    alert("Hubo un error al guardar: " + productStore.error)
  }
}
</script>

<style scoped>
.products-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.search-bar {
  margin-bottom: 20px;
}

.form-control {
  width: 100%;
  max-width: 400px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.table-container {
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  overflow: hidden;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
}

.data-table th, .data-table td {
  padding: 15px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.data-table th {
  background-color: #f8f9fa;
  font-weight: 600;
  color: #333;
}

.badge {
  padding: 5px 10px;
  border-radius: 20px;
  font-size: 0.85em;
  font-weight: bold;
}

.badge-active {
  background-color: #d4edda;
  color: #155724;
}

.badge-inactive {
  background-color: #f8d7da;
  color: #721c24;
}

.actions {
  display: flex;
  gap: 10px;
}

.btn-icon {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.2em;
}

.btn-primary {
  background-color: #3498db;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #2980b9;
}

.text-center {
  text-align: center;
  padding: 20px;
  color: #777;
}
</style>