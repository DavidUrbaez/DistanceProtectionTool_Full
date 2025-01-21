import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [message, setMessage] = useState('')

  useEffect(() => {
    // In production, this will be your Vercel URL
    const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000'

    fetch(`${apiUrl}/api/hello`)
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(error => console.error('Error:', error))
  }, [])


  return (
    <div className="App">
      <h1>Frontend + Backend Integration Test</h1>
      <p>Message from backend: {message || 'Loading...'}</p>
    </div>
  )
}
export default App 