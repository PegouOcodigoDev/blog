import { useState } from "react"
import Input from "./components/Input"
import { Link } from "react-router-dom"

export default () => {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [message, setMessage] = useState('')

    return (
        <>
            <div className="card">
                <h2 className="title-text">Entar</h2>
                {message && <strong className="danger-text">{message}</strong>}
                <Input
                label="Email"
                value={email}
                onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                    setEmail(e.target.value)
                }
                ></Input>
                <Input
                label="Password"
                value={password}
                onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                    setPassword(e.target.value)
                }
                ></Input>
                <Link to={'/'}>Esqueceu sua senha?</Link>
                <button className="btn-primary">Logar</button>
            </div>
        </>
    )
}