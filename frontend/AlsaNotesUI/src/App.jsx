import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import InteractivePage from './components/signin';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<InteractivePage />} />
      </Routes>
    </Router>
  );
}

export default App;
