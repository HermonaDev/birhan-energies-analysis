import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, ReferenceLine } from 'recharts';

const App = () => {
  const [data, setData] = useState([]);
  const [filteredData, setFilteredData] = useState([]);
  const [analysis, setAnalysis] = useState({});
  const [events, setEvents] = useState([]);
  const [highlightDate, setHighlightDate] = useState(null);
  const [startDate, setStartDate] = useState('2005-01-01');

  useEffect(() => {
    const URL = "http://127.0.0.1:5000/api";
    axios.get(`${URL}/prices`).then(res => {
      setData(res.data);
      setFilteredData(res.data.filter(d => d.Date >= startDate));
    });
    axios.get(`${URL}/analysis`).then(res => setAnalysis(res.data));
    axios.get(`${URL}/events`).then(res => setEvents(res.data));
  }, [startDate]);

  return (
    <div style={styles.layout}>
      {/* SIDEBAR with Click-to-Highlight */}
      <aside style={styles.sidebar}>
        <h2 style={styles.sidebarTitle}>EVENT DRILL-DOWN</h2>
        <p style={styles.sidebarHint}>Click an event to highlight on chart</p>
        <div style={styles.list}>
          {events.map((e, i) => (
            <div key={i} style={styles.card} onClick={() => setHighlightDate(e.Date)}>
              <small style={{color: '#3b82f6'}}>{e.Date}</small>
              <div style={{fontSize: '13px'}}>{e.Event}</div>
            </div>
          ))}
        </div>
      </aside>

      <main style={styles.main}>
        <header style={styles.header}>
          <h1>Birhan Energies Intelligence</h1>
          {/* USER CONTROL: Date Filter */}
          <div style={styles.control}>
            <label>Start Date: </label>
            <input type="date" value={startDate} onChange={(e) => setStartDate(e.target.value)} />
          </div>
        </header>

        <section style={styles.chartBox}>
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={filteredData}>
              <CartesianGrid strokeDasharray="3 3" vertical={false} />
              <XAxis dataKey="Date" hide={true} />
              <YAxis domain={['auto', 'auto']} />
              <Tooltip />
              <Line type="monotone" dataKey="Price" stroke="#2563eb" dot={false} isAnimationActive={false} />
              {/* Event Highlighting */}
              {highlightDate && <ReferenceLine x={highlightDate} stroke="orange" label="SELECTED EVENT" strokeWidth={2}/>}
              <ReferenceLine x={analysis.date} stroke="red" label="BAYESIAN BREAK" strokeDasharray="5 5" />
            </LineChart>
          </ResponsiveContainer>
        </section>
      </main>
    </div>
  );
};

const styles = {
  layout: { display: 'flex', height: '100vh', fontFamily: 'Inter, sans-serif' },
  sidebar: { width: '300px', backgroundColor: '#0f172a', color: 'white', padding: '20px', overflowY: 'auto' },
  sidebarTitle: { color: '#3b82f6', borderBottom: '1px solid #1e293b', paddingBottom: '10px' },
  sidebarHint: { fontSize: '11px', color: '#64748b' },
  card: { padding: '10px', backgroundColor: '#1e293b', borderRadius: '6px', marginBottom: '10px', cursor: 'pointer' },
  main: { flex: 1, padding: '30px', backgroundColor: '#f8fafc' },
  header: { display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' },
  chartBox: { height: '500px', backgroundColor: 'white', padding: '20px', borderRadius: '12px', boxShadow: '0 4px 6px rgba(0,0,0,0.05)' },
  control: { backgroundColor: 'white', padding: '10px', borderRadius: '8px', border: '1px solid #e2e8f0' }
};

export default App;
