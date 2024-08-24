import { useState } from "react";
import Input from "./components/Input";
import {createUser} from "../utils/Requests";
import "../index.css";
import { useNavigate } from "react-router";

export default () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const handleCreateUser = async () => {
    const response = await createUser({ name, email, password });

    if (response.detail) {
      setMessage(response.detail)
      return;
    }

    navigate("/login");
    
  };

  return (
    <>
      <div className="card">
        <h2 className="title-text">Crie sua conta</h2>
        {message && <strong className="danger-text">{message}</strong>}
        {}
        <Input
          label="Nome"
          value={name}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setName(e.target.value)
          }
        ></Input>
        <Input
          label="Email"
          value={email}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setEmail(e.target.value)
          }
        ></Input>
        <Input
          label="Senha"
          password
          value={password}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setPassword(e.target.value)
          }
        ></Input>
        <button className="btn-primary" onClick={handleCreateUser}>
          Cadastrar-se
        </button>
      </div>
    </>
  );
};
