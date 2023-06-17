import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Main from 'C:/Users/User/Desktop/S2S/KDT-SoundToShow/S2S/frontend/src/pages/main/main.js';

function App() {
    return (
      <Router>
        <Routes>
          <Route path="/" element={<Main />} />
          {/* More routes */}
        </Routes>
      </Router>
    );
  }
  

export default App;
