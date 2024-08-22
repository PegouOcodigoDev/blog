import { useState } from "react";
import Input from "./components/Input";
import signUp from "../utils/Requests";
import "../index.css";
import { useNavigate } from "react-router";

export default () => {
    const [name, setName] = useState('')
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('')
    const [message, setMessage] = useState('')
    const navigate = useNavigate()

    const handleSignUp = async () => {
        const response = await signUp({name,email,password});

        if (!response.detail){
          navigate('/login');
        }
        else{
          setMessage(response.detail)
        }
    }


  return (
    <>
      <div className="card">
        <h2 className="text-emerald-500 font-serif font-bold text-xl">Crie sua conta</h2>
        {message && <p className="text-red-400 font-serif text-sm text-center">{message}</p>}
        {}
        <Input label="Nome" value={name} onChange={(e: React.ChangeEvent<HTMLInputElement>) => setName(e.target.value)}></Input>
        <Input label="Email" value={email} onChange={(e: React.ChangeEvent<HTMLInputElement>) => setEmail(e.target.value)}></Input>
        <Input label="Senha" password value={password} onChange={(e: React.ChangeEvent<HTMLInputElement>) => setPassword(e.target.value)}></Input>
        <button className="btn-primary" onClick={handleSignUp}>Cadastrar-se</button>
      </div>
    </>
  );
};
