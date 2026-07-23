import apiClient from './apiClient'

export function getAllCourses() {
  return apiClient.get('/posts')
}

export function getCourseById(id) {
  return apiClient.get(`/posts/${id}`)
}

export function enrollStudent(studentId, courseId) {
  return Promise.resolve({
    success: true,
    studentId,
    courseId,
    message: 'Enrollment Successful'
  })
}