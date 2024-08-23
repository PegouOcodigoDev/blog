import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import SignUp from "./pages/SignUp";
import { Provider } from "react-redux";
import { store } from "./redux/store";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from "./pages/Login";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Provider store={store}>
    <BrowserRouter>
        <Routes>
          <Route path="/">
          <Route path="/signup" element={<SignUp></SignUp>}/>
          <Route path="/login" element={<Login></Login>}/>
          </Route>
        </Routes>
    </BrowserRouter>
    </Provider>
  </StrictMode>
);
