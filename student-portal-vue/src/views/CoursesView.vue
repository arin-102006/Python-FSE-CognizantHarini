<template>
  <div>
    <h2>Courses</h2>

    <input
      type="text"
      placeholder="Search Course"
      v-model="searchTerm"
    />

    <div v-if="filteredCourses.length === 0">
      No courses found
    </div>

    <div
      v-for="course in filteredCourses"
      :key="course.id"
      class="course-item"
    >
      <CourseCard
        :name="course.name"
        :code="course.code"
        :credits="course.credits"
        :grade="course.grade"
      />

      <button @click="store.enroll(course)">
        Enroll
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import CourseCard from '../components/CourseCard.vue'
import { useEnrollmentStore } from '../stores/enrollment'

const searchTerm = ref('')
const courses = ref([])
const store = useEnrollmentStore()

onMounted(() => {
  courses.value = [
    { id: 1, name: 'Database Systems', code: 'CS301', credits: 4, grade: 'A' },
    { id: 2, name: 'Operating Systems', code: 'CS302', credits: 3, grade: 'A+' },
    { id: 3, name: 'Computer Networks', code: 'CS303', credits: 3, grade: 'B+' },
    { id: 4, name: 'Web Development', code: 'CS304', credits: 4, grade: 'A' },
    { id: 5, name: 'Artificial Intelligence', code: 'CS305', credits: 4, grade: 'A+' }
  ]
})

const filteredCourses = computed(() =>
  courses.value.filter(course =>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  )
)
</script>

<style scoped>
.course-item {
  margin-bottom: 20px;
}

button {
  margin-left: 10px;
  padding: 8px 15px;
}
</style>