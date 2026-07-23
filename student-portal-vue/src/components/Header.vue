<template>
  <nav>
    <h2>Student Portal</h2>

    <RouterLink to="/courses">Courses</RouterLink>
    <RouterLink to="/profile">Profile</RouterLink>

    <span class="count">
      Enrolled: {{ store.enrolledCourses.length }}
    </span>
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>

<style scoped>
nav {
  display: flex;
  gap: 20px;
  padding: 15px;
  background: #42b883;
  align-items: center;
}

h2 {
  color: white;
  margin-right: auto;
}

a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.count {
  color: white;
  margin-left: auto;
  font-weight: bold;
}
</style>