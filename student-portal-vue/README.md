# Hands-On 10 - API Integration & Advanced State Management

## Framework Used
Vue 3 + Pinia

## Features Implemented

- Centralized Axios API Client
- Request Interceptor
- Response Interceptor
- API Service Layer
- Pinia Advanced Store
- Async fetchAndEnroll() Action
- Store Reset using $reset()
- Global Error Handler

## State Management Comparison

### React + Redux Toolkit
- Uses actions, reducers and async thunks.
- Good for large applications.
- More boilerplate than Pinia.

### Angular + NgRx
- Uses Actions, Reducers, Effects and Selectors.
- Very structured.
- Steeper learning curve.

### Vue + Pinia
- Very simple syntax.
- Less boilerplate.
- Excellent integration with Vue Composition API.
- Supports async actions and reactive state easily.

## NgRx Data Flow

Component
→ Action
→ Effect
→ API
→ Reducer
→ Store
→ Selector
→ Component