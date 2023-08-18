import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

// @ts-ignore
const componentName: string = django_component_name

const components = {
    app: App
}
// @ts-ignore
const app = createApp(components[componentName])

app.use(createPinia())

app.mount('#app')
