// WaterTankApp.jsx
import React, { useState, useEffect } from "react";
import { motion } from "framer-motion";

export default function WaterTankApp() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [sensorId, setSensorId] = useState("");
  const [sensorValue, setSensorValue] = useState(50); // Simulated data
  const [sensorInput, setSensorInput] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = () => {
    if (username && password) setIsLoggedIn(true);
  };

  const handleSensorSubmit = () => {
    if (sensorInput) {
      setSensorId(sensorInput);
      // Simulate data fetch
      fetchSensorValue();
    }
  };

  const fetchSensorValue = () => {
    // Replace this with real API call later
    setSensorValue(Math.floor(Math.random() * 100));
  };

  useEffect(() => {
    if (sensorId) {
      const interval = setInterval(fetchSensorValue, 5000); // Refresh every 5s
      return () => clearInterval(interval);
    }
  }, [sensorId]);

  const tankHeight = 300;
  const fillHeight = (sensorValue / 100) * tankHeight;

  return (
    <div style={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'linear-gradient(to bottom right, #bfdbfe, #c7d2fe)', padding: '1rem' }}>
      {!isLoggedIn ? (
        <div style={{ width: '100%', maxWidth: '400px', padding: '1.5rem', backgroundColor: '#fff', borderRadius: '1rem', boxShadow: '0 10px 25px rgba(0,0,0,0.1)' }}>
          <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', textAlign: 'center' }}>Login</h2>
          <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} style={inputStyle} />
          <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} style={inputStyle} />
          <button onClick={handleLogin} style={buttonStyle}>Sign In</button>
        </div>
      ) : !sensorId ? (
        <div style={{ width: '100%', maxWidth: '400px', padding: '1.5rem', backgroundColor: '#fff', borderRadius: '1rem', boxShadow: '0 10px 25px rgba(0,0,0,0.1)' }}>
          <h2 style={{ fontSize: '1.5rem', fontWeight: 'bold', textAlign: 'center' }}>Enter Sensor ID</h2>
          <input type="text" placeholder="Sensor ID" value={sensorInput} onChange={(e) => setSensorInput(e.target.value)} style={inputStyle} />
          <button onClick={handleSensorSubmit} style={buttonStyle}>Connect</button>
        </div>
      ) : (
        <div style={{ width: '100%', maxWidth: '600px', padding: '1.5rem', backgroundColor: '#fff', borderRadius: '1rem', boxShadow: '0 10px 25px rgba(0,0,0,0.1)' }}>
          <h2 style={{ fontSize: '1.25rem', fontWeight: 'bold', marginBottom: '1rem', textAlign: 'center' }}>Water Tank Live Visualization</h2>
          <div style={{ position: 'relative', width: '8rem', height: '300px', border: '4px solid #2563eb', borderBottomLeftRadius: '9999px', borderBottomRightRadius: '9999px', backgroundColor: '#dbeafe', overflow: 'hidden', margin: '0 auto' }}>
            <motion.div
              style={{ position: 'absolute', bottom: 0, left: 0, width: '100%', backgroundColor: '#3b82f6' }}
              initial={{ height: 0 }}
              animate={{ height: fillHeight }}
              transition={{ duration: 1 }}
            />
            <div style={{ position: 'absolute', bottom: '0.5rem', width: '100%', textAlign: 'center', color: 'white', fontWeight: 'bold', fontSize: '1.125rem' }}>
              {sensorValue}%
            </div>
          </div>
          <p style={{ marginTop: '1rem', fontSize: '0.875rem', color: '#6b7280', textAlign: 'center' }}>Sensor ID: {sensorId}</p>
        </div>
      )}
    </div>
  );
}

const inputStyle = {
  width: '100%',
  padding: '0.75rem',
  marginTop: '1rem',
  borderRadius: '0.5rem',
  border: '1px solid #d1d5db',
  outline: 'none'
};

const buttonStyle = {
  width: '100%',
  padding: '0.75rem',
  marginTop: '1rem',
  borderRadius: '0.5rem',
  backgroundColor: '#2563eb',
  color: '#fff',
  border: 'none',
  fontWeight: 'bold'
};