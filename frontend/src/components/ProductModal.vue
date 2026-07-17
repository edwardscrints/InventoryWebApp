<template>
</Transition>
  <div v-if="isOpen" class="modal-overlay" @click.self="closeModal">
    <div class="modal-content">
      <div class="modal-header">
        <h2>{{ isEditing ? 'Editar Producto' : 'Nuevo Producto' }}</h2>
        <button class="close-btn" @click="closeModal">✖</button>
      </div>
      
      <!--Se uso .prevent para evitar que el formulario recargue la página -->
      <form @submit.prevent="handleSubmit">
        <div class="form-grid">
          <div class="form-group">
            <label>SKU *</label>
            <input type="text" v-model="formData.sku" required maxlength="50" class="form-control" :disabled="isEditing" placeholder="Ej: SKU-001" />
          </div>
          
          <div class="form-group">
            <label>Nombre *</label>
            <input type="text" v-model="formData.nombre" required maxlength="100" class="form-control" />
          </div>

          <div class="form-group">
            <label>Categoría *</label>
            <input type="text" v-model="formData.categoria" required maxlength="50" class="form-control" placeholder="Ej: Cuidado Facial" />
          </div>

          <div class="form-group">
            <label>Presentación *</label>
            <input type="text" v-model="formData.presentacion" required maxlength="20" class="form-control" placeholder="Ej: 200gr, 500ml" />
          </div>
          
          <div class="form-group">
            <label>Precio *</label>
            <!-- Validación HTML5: mínimo 0.01 exigido por el reto -->
            <input type="number" v-model="formData.precio" required min="0.01" step="0.01" class="form-control" />
          </div>
          
          <div class="form-group">
            <label>Stock *</label>
            <!-- Validación HTML5: mínimo 0 exigido por el reto -->
            <input type="number" v-model="formData.stock" required min="0" step="1" class="form-control" />
          </div>

          <div class="form-group">
            <label>Estado *</label>
            <select v-model="formData.estado" required class="form-control">
              <option value="Activo">Activo</option>
              <option value="Inactivo">Inactivo</option>
            </select>
          </div>
        </div>

        <div class="form-group full-width">
          <label>Descripción</label>
          <textarea v-model="formData.descripción" rows="3" class="form-control"></textarea>
        </div>
        
        <div class="modal-actions">
          <button type="button" class="btn btn-secondary" @click="closeModal">Cancelar</button>
          <button type="submit" class="btn btn-primary" :disabled="loading">
            {{ loading ? 'Guardando...' : 'Guardar Producto' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</Transition>
</template>

<script setup>
import { ref, watch, computed } from 'vue'

const props = defineProps({
  isOpen: Boolean,
  product: Object,
  loading: Boolean
})

const emit = defineEmits(['close', 'save'])

const defaultForm = {
  sku: '',
  nombre: '',
  categoria: '',
  presentacion: '',
  descripción: '',
  precio: '',
  stock: '',
  estado: 'Activo'
}

const formData = ref({ ...defaultForm })

const isEditing = computed(() => !!props.product)

// Reactividad: Si la propiedad product cambia se permite la edición
watch(
  () => props.product,
  (newVal) => {
    if (newVal) {
      formData.value = { ...newVal }
    } else {
      formData.value = { ...defaultForm }
    }
  },
  { immediate: true }
)

const closeModal = () => {
  emit('close')
}

const handleSubmit = () => {
  // Reglas de Negocio
  const payload = {
    ...formData.value,
    precio: parseFloat(formData.value.precio),
    stock: parseInt(formData.value.stock, 10)
  }
  emit('save', payload)
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 30px;
  border-radius: 8px;
  width: 100%;
  max-width: 700px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid #eee;
}

.modal-header h2 { margin: 0; color: #2c3e50; }

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #7f8c8d;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 15px;
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 15px;
}

.full-width {
  grid-column: span 2;
}

label {
  font-weight: 600;
  margin-bottom: 5px;
  color: #34495e;
  font-size: 0.9em;
}

.form-control {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1em;
}

.form-control:disabled {
  background-color: #f8f9fa;
  cursor: not-allowed;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid #eee;
}


.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

.fade-enter-active .modal-content,
.fade-leave-active .modal-content {
  transition: transform 0.3s ease;
}
.fade-enter-from .modal-content,
.fade-leave-to .modal-content {
  transform: scale(0.95);
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 600;
}

.btn-secondary { background-color: #95a5a6; color: white; }
.btn-primary { background-color: #3498db; color: white; }
.btn:disabled { opacity: 0.7; cursor: not-allowed; }
</style>