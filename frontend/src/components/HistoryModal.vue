<template>
<Transition name="fade">
  <div v-if="isOpen" class="modal-overlay" @click.self="closeModal">
    <div class="modal-content history-content">
      <div class="modal-header">
        <h2> Historial de Cambios</h2>
        <button class="close-btn" @click="closeModal">✖</button>
      </div>
      
      <div class="modal-body">
        <p class="subtitle">Producto: <strong>{{ productName }}</strong></p>
        
        <div v-if="loading" class="text-center loading-text">
          Cargando historial...
        </div>
        
        <div v-else-if="history.length === 0" class="text-center empty-text">
          No hay registros en el historial para este producto.
        </div>

        <!-- Línea de tiempo -->
        <div v-else class="timeline">
          <div v-for="item in history" :key="item.id" class="timeline-item">
            <div class="timeline-marker" :class="getMarkerClass(item.action)"></div>
            <div class="timeline-content">
              <div class="timeline-header">
                <span class="action-badge" :class="getMarkerClass(item.action)">
                  {{ item.action }}
                </span>
                <span class="date">{{ formatDate(item.created_at) }}</span>
              </div>
              <p class="description">{{ item.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </Transition>
</template>

<script setup>
defineProps({
  isOpen: Boolean,
  productName: String,
  history: {
    type: Array,
    default: () => []
  },
  loading: Boolean
})

const emit = defineEmits(['close'])

const closeModal = () => {
  emit('close')
}

// Se formato la fecha para que sea legible
const formatDate = (dateString) => {
  const options = { 
    year: 'numeric', month: 'short', day: 'numeric', 
    hour: '2-digit', minute: '2-digit', second: '2-digit' 
  }
  return new Date(dateString).toLocaleDateString('es-CO', options)
}

// Colores por acción
const getMarkerClass = (action) => {
  switch (action) {
    case 'CREATE': return 'marker-create'
    case 'UPDATE': return 'marker-update'
    case 'DELETE': return 'marker-delete'
    case 'STATUS_CHANGE': return 'marker-status'
    default: return 'marker-default'
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.history-content {
  background: white;
  padding: 30px;
  border-radius: 8px;
  width: 100%;
  max-width: 600px;
  max-height: 80vh; /* Para que no se salga de la pantalla */
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #eee;
  padding-bottom: 15px;
}

.modal-header h2 { margin: 0; color: #2c3e50; }
.close-btn { background: none; border: none; font-size: 1.5rem; cursor: pointer; color: #7f8c8d; }

.modal-body {
  margin-top: 15px;
  overflow-y: auto; /* Scroll interno si hay muchos eventos */
  padding-right: 10px;
}

.subtitle { color: #34495e; font-size: 1.1rem; margin-bottom: 20px; }
.text-center { text-align: center; padding: 20px; color: #7f8c8d; }

/* Estilos */
.timeline {
  position: relative;
  border-left: 2px solid #ecf0f1;
  margin-left: 10px;
  padding-left: 20px;
}

.timeline-item {
  position: relative;
  margin-bottom: 25px;
}

.timeline-marker {
  position: absolute;
  left: -27px; /* Centrar sobre el borde */
  top: 0;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 2px solid white;
}

.timeline-content {
  background: #f8f9fa;
  padding: 15px;
  border-radius: 6px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.timeline-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
  font-size: 0.85rem;
}

.date { color: #95a5a6; }
.description { margin: 0; color: #2c3e50; font-size: 0.95rem; }

/* Animación del Modal */
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

/* Colores dinámicos */
.action-badge { padding: 3px 8px; border-radius: 12px; font-weight: bold; font-size: 0.75rem; color: white;}
.marker-create { background-color: #2ecc71; }
.marker-update { background-color: #3498db; }
.marker-delete { background-color: #e74c3c; }
.marker-status { background-color: #f1c40f; color: #333;}
.marker-default { background-color: #95a5a6; }

</style>