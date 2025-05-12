import { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import Landing_page from "./Pages/Landing_Page/Landing_page";
import Homepage from "./Pages/Home_page/home_page";
import ProtectedRoutes from "./utils/ProtectedRoutes";
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Landing_page />} />

        <Route element={<ProtectedRoutes/>}>
        <Route path="/Home" element={<Homepage />} />
        
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
