
import Header from './Components/Header';
import Footer from './Components/Footer';
import React, { useState } from 'react';
import Signup from './Components/Signup';
import Login from './Components/Login';
import './Styles/App.css'; 

function App() {
  const [isSignup, setIsSignup] = useState(true);

  return (
    <div className="container">
      <Header />
      <div className="button-container">
      <button onClick={() => setIsSignup(true)}>Signup</button>
      <button onClick={() => setIsSignup(false)}>Login</button>
      </div>
      {isSignup ? <Signup /> : <Login />}
      <Footer />
    </div>
  );
}

export default App;
