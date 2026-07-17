<template>
  <MainLayout>
    <div class="products-header">
      <h1>Gestión de Productos</h1>
      <button class="btn btn-primary" @click="openCreateModal">
        + Nuevo Producto
      </button>
    </div>

    <!-- Dashboard Cards -->
    <div class="dashboard-cards">
      <div class="card">
        <div class="card-icon">📦</div>
        <div class="card-info">
          <h3>Total Productos</h3>
          <p>{{ totalProducts }}</p>
        </div>
      </div>
      <div class="card">
        <div class="card-icon">⚠️</div>
        <div class="card-info">
          <h3>Bajo Stock</h3>
          <p>{{ lowStockCount }}</p>
        </div>
      </div>
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
      <TableSkeleton v-if="productStore.loading" />
      
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
              <span 
                :class="['badge', product.estado === 'Activo' ? 'badge-active' : 'badge-inactive']"
                @click="toggleStatus(product)"
                title="Clic para cambiar estado"
              >
                {{ product.estado }}
              </span>
            </td>
            <td class="actions">
             <button class="btn-icon text-blue" @click="openEditModal(product)" title="Editar">EDITAR</button>
             <button class="btn-icon text-red" @click="openDeleteModal(product)" title="Eliminar">ELIMINAR</button>
             <button class="btn-icon text-gray" @click="openHistoryModal(product)" title="Historial">HISTORIAL</button>
            </td>
          </tr>
          <tr v-if="productStore.products.length === 0 && !productStore.loading">
            <td colspan="7" class="empty-state">
              <div class="empty-state-content">
                <span class="empty-icon">🔍</span>
                <p>No se encontraron productos con tu búsqueda.</p>
                <button class="btn-secondary" v-if="searchQuery" @click="searchQuery = ''; handleSearch()">Limpiar Búsqueda</button>
              </div>
            </td>
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
<ConfirmDeleteModal 
  :isOpen="isDeleteModalOpen"
  :productName="productToDelete?.nombre || ''"
  :loading="productStore.loading"
  @close="closeDeleteModal"
  @confirm="executeDelete"
/>
<HistoryModal
  :isOpen="isHistoryModalOpen"
  :productName="productNameForHistory"
  :history="historyData"
  :loading="productStore.loading"
  @close="closeHistoryModal"
/>
  </MainLayout>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useProductStore } from '../stores/productStore'
import MainLayout from '../components/MainLayout.vue'
import ProductModal from '../components/ProductModal.vue'
import ConfirmDeleteModal from '../components/ConfirmDeleteModal.vue'
import HistoryModal from '../components/HistoryModal.vue'
import { useToast } from '../composables/useToast'
import TableSkeleton from '../components/TableSkeleton.vue'

// Store
const productStore = useProductStore()

// Datos
const searchQuery = ref('')

// Computed properties for Dashboard Cards
const totalProducts = computed(() => productStore.products.length)
const lowStockCount = computed(() => {
  return productStore.products.filter(p => p.stock < 10).length
})

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

//ToastContainer
const { toasts, showToast, removeToast } = useToast()

// Estado para modal de Eliminación
const isDeleteModalOpen = ref(false)
const productToDelete = ref(null)

// Funciones de eliminación
const openDeleteModal = (product) => {
  productToDelete.value = product
  isDeleteModalOpen.value = true
}

const closeDeleteModal = () => {
  isDeleteModalOpen.value = false
  productToDelete.value = null
}

const toggleStatus = async (product) => {
  try {
    await productStore.toggleStatus(product.id)
    showToast(`Estado actualizado con éxito`, 'success')
  } catch (error) {
    showToast("Error al cambiar estado: " + productStore.error, 'error')
  }
}

// Estado para el modal de Historial
const isHistoryModalOpen = ref(false)
const historyData = ref([])
const productNameForHistory = ref('')

const handleSaveProduct = async (productData) => {
  try {
    if (selectedProduct.value) {
      // Actualizar
      await productStore.updateProduct(selectedProduct.value.id, productData)
      showToast('Producto actualizado exitosamente', 'success')
    } else {
      // Crear
      await productStore.createProduct(productData)
      showToast('Producto creado exitosamente', 'success')
    }
    closeModal()
  } catch (error) {
    showToast('Error al guardar: ' + productStore.error, 'error')
  }
}

const executeDelete = async () => {
  if (!productToDelete.value) return
  try {
    await productStore.deleteProduct(productToDelete.value.id)
    showToast('Producto eliminado exitosamente', 'success')
    closeDeleteModal()
  } catch (error) {
    showToast("Error al eliminar: " + productStore.error, 'error')
  }
}

const openHistoryModal = async (product) => {
  productNameForHistory.value = product.nombre
  isHistoryModalOpen.value = true
  
  // Llamamos a la tienda para traer los datos reales
  historyData.value = await productStore.fetchProductHistory(product.id)
}

const closeHistoryModal = () => {
  isHistoryModalOpen.value = false
  historyData.value = []
}
</script>

<style scoped>
.products-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.dashboard-cards {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

.card {
  flex: 1;
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  display: flex;
  align-items: center;
  gap: 15px;
}

.card-icon {
  font-size: 2.5em;
}

.card-info h3 {
  margin: 0;
  font-size: 1em;
  color: #7f8c8d;
}

.card-info p {
  margin: 5px 0 0;
  font-size: 1.5em;
  font-weight: bold;
  color: #2c3e50;
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
  cursor: pointer;
  user-select: none;
  transition: opacity 0.2s;
}

.badge:hover {
  opacity: 0.8;
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

.empty-state {
  text-align: center;
  padding: 40px !important;
}

.empty-state-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  color: #7f8c8d;
}

.empty-icon {
  font-size: 3em;
}

.btn-secondary {
  background-color: #ecf0f1;
  color: #2c3e50;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 10px;
  font-weight: bold;
}

.btn-secondary:hover {
  background-color: #bdc3c7;
}
</style>