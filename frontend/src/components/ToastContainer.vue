<template>
  <div class="toast-container">
    <TransitionGroup name="toast">
      <div 
        v-for="toast in toasts" 
        :key="toast.id" 
        :class="['toast-message', `toast-${toast.type}`]"
      >
        {{ toast.message }}
      </div>
    </TransitionGroup>
  </div>
</template>

<script setup>
import { useToast } from '../composables/useToast'
const { toasts } = useToast()
</script>

<style scoped>
.toast-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  z-index: 9999;
}

.toast-message {
  padding: 12px 24px;
  border-radius: 6px;
  color: white;
  font-weight: 600;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  min-width: 250px;
  text-align: center;
}

.toast-success { background-color: #2ecc71; }
.toast-error { background-color: #e74c3c; }
.toast-warning { background-color: #f1c40f; color: #333; }

/* Animaciones para entrada y salida */
.toast-enter-active, .toast-leave-active {
  transition: all 0.4s ease;
}
.toast-enter-from {
  opacity: 0;
  transform: translateX(50px);
}
.toast-leave-to {
  opacity: 0;
  transform: translateX(50px);
}
</style>