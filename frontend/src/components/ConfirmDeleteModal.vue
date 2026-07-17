<template>
  <div v-if="isOpen" class="modal-overlay" @click.self="closeModal">
    <div class="modal-content confirm-content">
      <div class="modal-header">
        <h2>Confirmas Eliminación</h2>
        <button class="close-btn" @click="closeModal">✖</button>
      </div>
      
      <div class="modal-body">
        <p>¿Estás seguro de que deseas eliminar el producto <strong>{{ productName }}</strong>?</p>
        <p class="text-danger">Esta acción no se puede deshacer.</p>
      </div>

      <div class="modal-actions">
        <button class="btn btn-secondary" @click="closeModal" :disabled="loading">Cancelar</button>
        <button class="btn btn-danger" @click="confirmDelete" :disabled="loading">
          {{ loading ? 'Eliminando...' : 'Sí, Eliminar' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  isOpen: Boolean,
  productName: String,
  loading: Boolean
})

const emit = defineEmits(['close', 'confirm'])

const closeModal = () => {
  emit('close')
}

const confirmDelete = () => {
  emit('confirm')
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

.confirm-content {
  background: white;
  padding: 30px;
  border-radius: 8px;
  width: 100%;
  max-width: 450px; /* Más pequeño que el formulario */
  box-shadow: 0 4px 20px rgba(0,0,0,0.15);
  text-align: center;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.modal-header h2 { 
  margin: 0; 
  color: #e74c3c; 
  font-size: 1.5rem;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #7f8c8d;
}

.modal-body {
  margin-bottom: 25px;
  font-size: 1.1rem;
  color: #34495e;
}

.text-danger {
  color: #e74c3c;
  font-size: 0.9rem;
  margin-top: 10px;
}

.modal-actions {
  display: flex;
  justify-content: center;
  gap: 15px;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 600;
}

.btn-secondary { background-color: #95a5a6; color: white; }
.btn-danger { background-color: #e74c3c; color: white; }
.btn-danger:hover { background-color: #c0392b; }
.btn:disabled { opacity: 0.7; cursor: not-allowed; }
</style>