<template>
  <div class="card">
    <h3>{{ name }}</h3>
    <p><b>Code:</b> {{ code }}</p>
    <p><b>Credits:</b> {{ credits }}</p>
    <p><b>Grade:</b> {{ grade }}</p>
  </div>
</template>

<script setup>
defineProps({
  name: String,
  code: String,
  credits: Number,
  grade: String
})
</script>

<style scoped>
.card {
  border: 1px solid #ccc;
  padding: 15px;
  margin: 10px;
  border-radius: 8px;
}
</style>