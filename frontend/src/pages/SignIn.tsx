import { useState } from "react";
import Button from "../components/Button";
import Card from "../components/Card";
import Input from "../components/Input";
import signUp from "../utils/Requests";
import "../index.css";

export default () => {
    const [name, setName] = useState('')
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('')

    const handleSignUp = async () => {
         

        const response = await signUp({name,email,password});

        console.log(response)
    }


  return (
    <>
      <Card>
        <Input label="Nome" value={name} onChange={(e: React.ChangeEvent<HTMLInputElement>) => setName(e.target.value)}></Input>
        <Input label="Email" value={email} onChange={(e: React.ChangeEvent<HTMLInputElement>) => setEmail(e.target.value)}></Input>
        <Input label="Senha" value={password} onChange={(e: React.ChangeEvent<HTMLInputElement>) => setPassword(e.target.value)}></Input>
        <Button label="Cadastrar" onClick={handleSignUp}></Button>
      </Card>
    </>
  );
};
