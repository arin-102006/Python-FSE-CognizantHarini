import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { getCourseById, enrollStudent } from '../api/courseApi'

export const useEnrollmentStore = defineStore('enrollment', () => {

  const enrolledCourses = ref([])
  const loading = ref(false)
  const error = ref(null)

  const totalCredits = computed(() =>
    enrolledCourses.value.reduce((sum, course) => sum + (course.credits || 0), 0)
  )

  function enroll(course) {
    const exists = enrolledCourses.value.find(
      c => c.id === course.id
    )

    if (!exists) {
      enrolledCourses.value.push(course)
    }
  }

  function unenroll(courseId) {
    enrolledCourses.value = enrolledCourses.value.filter(
      course => course.id !== courseId
    )
  }

  async function fetchAndEnroll(courseId) {
    loading.value = true
    error.value = null

    try {
      const course = await getCourseById(courseId)

      await enrollStudent(1, courseId)

      enroll({
        id: course.id,
        name: course.title,
        credits: 3
      })
    } catch (err) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }

  function $reset() {
    enrolledCourses.value = []
    loading.value = false
    error.value = null
  }

  return {
    enrolledCourses,
    totalCredits,
    loading,
    error,
    enroll,
    unenroll,
    fetchAndEnroll,
    $reset
  }

})