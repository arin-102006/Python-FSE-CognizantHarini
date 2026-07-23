import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

// Global Error Handler
app.config.errorHandler = (err, instance, info) => {
  console.error('Global Error:', err)
  console.error('Component:', instance)
  console.error('Info:', info)

  alert('Something went wrong. Please try again.')
}

app.mount('#app')