import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { Provider } from "react-redux";
import { store } from "./redux/store";
import StudentProvider from "./context/StudentContext";
import App from "./App";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <Provider store={store}>
      <StudentProvider>
        <BrowserRouter>
          <App />
        </BrowserRouter>
      </StudentProvider>
    </Provider>
  </React.StrictMode>
);