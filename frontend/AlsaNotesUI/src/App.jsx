import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import InteractivePage from './components/InteractivePage';
import HomePage from './components/HomePage'; // Assuming you have a homepage component

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/interactive" element={<InteractivePage />} />
      </Routes>
    </Router>
  );
}

export default App;
