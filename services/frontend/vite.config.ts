import { fileURLToPath, URL } from 'node:url'
import path from 'path'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  base: '/static/',
  root: path.resolve('./src'),
  build: {
    manifest: true,
    emptyOutDir: true,
    assetsDir: '',
    sourcemap: true,
    target: 'es2015',
    outDir: path.resolve('./build'),
    rollupOptions: {
      input: {
        app: path.resolve('./src/main.ts'),
      },
    },
  },
  server: {
    host: "0.0.0.0",
    port: 3000,
    fs: {
      allow: ['../..'],  // Allow serving files from one level up to the project root
    },
    origin: 'http://localhost:3000',
  },
})
