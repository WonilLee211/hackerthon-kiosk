import React from "react";
import { Route, Routes, Link } from "react-router-dom";
import Main from './Main/Main';
import Admin from './admin/admin';


function App() {
  return (
    <Routes>
          <Route path="/" exact element={<Main/>} />
          <Route exact path="/admin" element={<Admin />} />
    </Routes>
  );
}

export default App;
