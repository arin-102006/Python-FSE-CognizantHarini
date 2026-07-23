<template>
  <Header />
  <RouterView />
</template>

<script setup>
import Header from './components/Header.vue'
import { RouterView } from 'vue-router'
</script>