<template>
  <div>
    <h2>Student Profile</h2>

    <h3>Enrolled Courses</h3>

    <ul>
      <li
        v-for="course in enrolledCourses"
        :key="course.id"
      >
        {{ course.name }} ({{ course.credits }} Credits)
      </li>
    </ul>

    <h3>Total Credits: {{ totalCredits }}</h3>
  </div>
</template>

<script setup>
import { useEnrollmentStore } from '../stores/enrollment'
import { storeToRefs } from 'pinia'

const store = useEnrollmentStore()

const {
  enrolledCourses,
  totalCredits
} = storeToRefs(store)
</script>