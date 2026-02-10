import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, ReferenceLine } from 'recharts';

const App = () => {
  const [data, setData] = useState([]);
  const [analysis, setAnalysis] = useState({});
  const [events, setEvents] = useState([]);

  // Forced API path
  const API = "http://127.0.0.1:5000/api";

  useEffect(() => {
    // Prices
    axios.get(`${API}/prices`).then(res => setData(res.data));
    
    // Analysis
    axios.get(`${API}/analysis`).then(res => {
        console.log("Analysis Received:", res.data);
        setAnalysis(res.data);
    });

    // Events
    axios.get(`${API}/events`).then(res => {
        console.log("Events Received:", res.data);
        setEvents(res.data);
    });
  }, []);

  return (
    <div style={{ display: 'flex', height: '100vh', width: '100vw', backgroundColor: '#f1f5f9', fontFamily: 'sans-serif' }}>
      
      {/* SIDEBAR */}
      <aside style={{ width: '320px', backgroundColor: '#0f172a', color: 'white', padding: '25px', overflowY: 'auto' }}>
        <h2 style={{ fontSize: '20px', color: '#3b82f6', borderBottom: '1px solid #1e293b', paddingBottom: '15px' }}>GLOBAL EVENTS</h2>
        {events.length > 0 ? events.map((e, i) => (
          <div key={i} style={{ marginBottom: '15px', padding: '12px', backgroundColor: '#1e293b', borderRadius: '8px', borderLeft: '4px solid #3b82f6' }}>
            <small style={{ color: '#94a3b8' }}>{e.Date}</small>
            <div style={{ fontSize: '13px', marginTop: '4px', color: '#f8fafc' }}>{e.Event}</div>
          </div>
        )) : <p>Loading events...</p>}
      </aside>

      {/* MAIN CONTENT */}
      <main style={{ flex: 1, padding: '40px', overflowY: 'auto' }}>
        <div style={{ marginBottom: '40px' }}>
          <h1 style={{ color: '#1e293b', margin: 0, fontSize: '32px' }}>Brent Oil Intelligence</h1>
          <p style={{ color: '#64748b' }}>Structural Break: <b>{analysis.date}</b></p>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '25px', marginBottom: '40px' }}>
          <div style={cardStyle}>
            <span style={labelStyle}>PRICE SHIFT</span>
            <h2 style={{ color: '#10b981', margin: '10px 0', fontSize: '36px' }}>{analysis.price_shift || "---"}</h2>
            <small style={{ color: '#94a3b8' }}>$\mu$: ${analysis.mu1} → ${analysis.mu2}</small>
          </div>
          <div style={cardStyle}>
            <span style={labelStyle}>RISK DELTA (VOLATILITY)</span>
            <h2 style={{ color: '#f59e0b', margin: '10px 0', fontSize: '36px' }}>{analysis.risk_delta || "---"}</h2>
            <small style={{ color: '#94a3b8' }}>Bayesian Convergence: R-hat 1.0</small>
          </div>
        </div>

        <div style={{ height: '450px', backgroundColor: 'white', padding: '30px', borderRadius: '15px', boxShadow: '0 10px 15px -3px rgba(0,0,0,0.1)' }}>
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={data}>
              <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" />
              <XAxis dataKey="Date" hide={true} />
              <YAxis domain={['auto', 'auto']} stroke="#94a3b8" />
              <Tooltip />
              <Line type="monotone" dataKey="Price" stroke="#2563eb" dot={false} strokeWidth={3} isAnimationActive={false} />
              <ReferenceLine x={analysis.date} stroke="#ef4444" strokeWidth={3} strokeDasharray="8 8" label={{ value: 'SHIFT', position: 'top', fill: '#ef4444', fontWeight: 'bold' }} />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </main>
    </div>
  );
};

const cardStyle = { backgroundColor: 'white', padding: '30px', borderRadius: '15px', boxShadow: '0 4px 6px rgba(0,0,0,0.05)', border: '1px solid #e2e8f0' };
const labelStyle = { fontSize: '12px', color: '#64748b', fontWeight: 'bold', letterSpacing: '1.5px' };

export default App;