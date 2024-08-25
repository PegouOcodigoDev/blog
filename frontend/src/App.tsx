import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from "./pages/Login";
import SignUp from "./pages/SignUp";
import Home from "./pages/Home";
import NotFound from "./pages/404";
import "./App.css"

export default () => {
    return (
        <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home></Home>}/>
          <Route path="/signup" element={<SignUp></SignUp>}/>
          <Route path="/login" element={<Login></Login>}/>
          <Route path="*" element={<NotFound></NotFound>}/>
        </Routes>
    </BrowserRouter>
    )
}