import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'https://jsonplaceholder.typicode.com',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// Request Interceptor
apiClient.interceptors.request.use(
  (config) => {
    config.headers.Authorization = 'Bearer mock-token-12345'
    return config
  },
  (error) => Promise.reject(error)
)

// Response Interceptor
apiClient.interceptors.response.use(
  (response) => response.data,
  (error) => {
    throw {
      message: error.response?.data?.message || error.message,
      statusCode: error.response?.status || 500
    }
  }
)

export default apiClient