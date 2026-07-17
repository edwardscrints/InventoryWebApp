<template>
  <div id="app">
    <router-view></router-view>
    <ToastContainer />
  </div>
</template>

<script setup>
import ToastContainer from './components/ToastContainer.vue'
</script>

<style>
/* Limpieza visual */
body {
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  background-color: #f4f6f8;
}
</style>