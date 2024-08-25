import { useState } from "react"
import Input from "./components/Input"
import { Link, useNavigate } from "react-router-dom"
import { login } from "../utils/requests"
import { useDispatch } from "react-redux"
import { setUser } from "../redux/reducers/userReducer"

export default () => {
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [message, setMessage] = useState('')
    const navigate = useNavigate()
    const dispatch = useDispatch()

    const handleLogin = async () => {
        const response = await login({email, password});
        if(response.detail){
            setMessage(response.detail);
            return;
        }

        if (response.data){
            const { refresh, access, ...user } = response.data;

            localStorage.setItem('access_token', access);
            localStorage.setItem('refresh_token', refresh)

            dispatch(setUser(user));

            navigate('/')
        }
    }

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
                password
                label="Password"
                value={password}
                onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
                    setPassword(e.target.value)
                }
                ></Input>
                <Link to={'/'}>Esqueceu sua senha?</Link>
                <button className="btn-primary" onClick={handleLogin}>Logar</button>
            </div>
        </>
    )
}