import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import Hello from './components/Hello.vue'
import NotFound from './components/404.vue'

// @ts-ignore
const componentName: string = django_component_name

const components = {
    hello: Hello
}
// @ts-ignore
const app = createApp(components[componentName] ?? NotFound)

app.use(createPinia())

app.mount('#app')
