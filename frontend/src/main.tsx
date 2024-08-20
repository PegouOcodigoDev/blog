import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import SignIn from './pages/SignIn'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <SignIn></SignIn>
  </StrictMode>,
)
