import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import "./App.css";
import StudentProvider from "./context/StudentContext";

ReactDOM.createRoot(document.getElementById("root")).render(
  <StudentProvider>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StudentProvider>
);