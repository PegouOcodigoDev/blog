import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import SignUp from "./pages/SignUp";
import { Provider } from "react-redux";
import { store } from "./redux/store";
import { BrowserRouter, Route, Routes } from "react-router-dom";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <BrowserRouter>
        <Routes>
          <Route path="/">
          <Route path="/signup" element={<Provider store={store}><SignUp></SignUp></Provider>}/>
          <Route path="/login" element={<h1>Login</h1>}/>
          </Route>
        </Routes>
    </BrowserRouter>
  </StrictMode>
);
