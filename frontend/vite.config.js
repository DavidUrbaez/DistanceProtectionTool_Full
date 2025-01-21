import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: '/DistanceProtectionTool_Full/',  // Changed to match your repo name
})