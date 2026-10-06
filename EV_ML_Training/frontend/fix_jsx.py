import os

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's completely recreate the return statement from scratch.
# We will find the start of the return statement and the end.
start_idx = content.find('  return (')
if start_idx == -1:
    print('Could not find return statement')
    exit(1)

# I have the exact components I need. Let me just hardcode the entire return statement.
new_return = """  return (
    <div className="app-container">
      {/* Sidebar */}
      <div className="sidebar">
        <div className="sidebar-logo">
          <ZapIcon className="logo-icon" size={28} />
          <div className="logo-text">
            <h2>EV Battery AI</h2>
            <p>Battery Health Prediction</p>
          </div>
        </div>
        
        <div className="sidebar-nav">
          <div className={`nav-item ${activeTab === 'Dashboard' ? 'active' : ''}`} onClick={() => setActiveTab('Dashboard')}><LayoutDashboard size={18} /> Dashboard</div>
          <div className={`nav-item ${activeTab === 'Battery Analysis' ? 'active' : ''}`} onClick={() => setActiveTab('Battery Analysis')}><Battery size={18} /> Battery Analysis</div>
          <div className={`nav-item ${activeTab === 'Prediction History' ? 'active' : ''}`} onClick={() => setActiveTab('Prediction History')}><History size={18} /> Prediction History</div>
          <div className={`nav-item ${activeTab === 'Visualizations' ? 'active' : ''}`} onClick={() => setActiveTab('Visualizations')}><ActivityIcon size={18} /> Visualizations</div>
          <div className={`nav-item ${activeTab === 'About Project' ? 'active' : ''}`} onClick={() => setActiveTab('About Project')}><Info size={18} /> About Project</div>
          <div className={`nav-item ${activeTab === 'Settings' ? 'active' : ''}`} onClick={() => setActiveTab('Settings')}><Settings size={18} /> Settings</div>
        </div>

        <div className="sidebar-bottom-img">
          <img src={carSidebar} alt="EV Car" />
          <div className="sidebar-bottom-text">
            <h3>Clean Energy Smarter Future</h3>
            <p>AI-Driven Battery Intelligence for a Sustainable Tomorrow</p>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="main-content">
        {/* Header */}
        <div className="top-header">
          <div className="api-status glass-panel">
            <div className={`status-dot ${apiStatus}`}></div>
            <div className="api-text">
              <h4>{apiStatus === 'connected' ? 'API Connected' : apiStatus === 'error' ? 'API Offline' : 'Connecting...'}</h4>
              <p>FastAPI • 127.0.0.1:8000</p>
            </div>
          </div>
          <div className="user-profile glass-panel" style={{ padding: '8px 16px', borderRadius: '30px' }}>
            <Sun size={18} color="var(--text-muted)" />
            <div className="avatar">EV</div>
            <div className="api-text">
              <h4>EV Analytics</h4>
              <p>AI Powered</p>
            </div>
          </div>
        </div>

        <div className="dashboard-container">
          {activeTab === 'Dashboard' && (
            <>
              {/* Main Banner */}
              <div className="main-banner">
                <div className="banner-overlay"></div>
                <div className="banner-content">
                  <div className="banner-icon"><Battery size={24} /></div>
                  <div className="banner-text">
                    <h1>EV Battery Intelligence Dashboard</h1>
                    <p>Predict battery failure risk and remaining useful life using machine learning</p>
                  </div>
                  <div className="banner-right glass-panel">
                    <CheckCircle2 size={18} />
                    <span>Powering a Sustainable Future</span>
                  </div>
                </div>
              </div>

              {/* Top Stats Cards */}
              <div className="top-cards-grid">
                <div className="stat-card glass-panel">
                  <div className="stat-icon health"><Battery size={24} /></div>
                  <div className="stat-info">
                    <h3>Battery Health (SOH)</h3>
                    <div className="value">{results.soh.toFixed(1)}%</div>
                    <p>State of Health</p>
                  </div>
                </div>
                <div className="stat-card glass-panel">
                  <div className="stat-icon risk"><ShieldAlert size={24} /></div>
                  <div className="stat-info">
                    <h3>Failure Probability</h3>
                    <div className="value">{(results.failure_probability * 100).toFixed(4)}%</div>
                    <p>{results.failure_probability < 0.05 ? 'Very Low Risk' : 'High Risk'}</p>
                  </div>
                </div>
                <div className="stat-card glass-panel">
                  <div className="stat-icon life"><ActivityIcon size={24} /></div>
                  <div className="stat-info">
                    <h3>Remaining Life</h3>
                    <div className="value">{results.predicted_remaining_life_cycles.toLocaleString(undefined, {maximumFractionDigits: 2})}</div>
                    <p>Predicted Cycles</p>
                  </div>
                </div>
                <div className="stat-card glass-panel">
                  <div className="stat-icon status"><BrainCircuit size={24} /></div>
                  <div className="stat-info">
                    <h3>Battery Status</h3>
                    <div className="value" style={{ color: results.failure_prediction === 0 ? 'var(--success)' : 'var(--danger)' }}>
                      {results.failure_prediction === 0 ? 'Healthy' : 'Failure Risk'}
                    </div>
                    <p>AI Prediction Result</p>
                  </div>
                </div>
              </div>
            </>
          )}

          {activeTab === 'Battery Analysis' && (
            <div className="main-grid" style={{ display: 'flex', gap: '24px' }}>
              <div className="input-section glass-panel" style={{ flex: '1' }}>
                <div className="section-header">
                  <div style={{ background: 'var(--primary)', padding: '6px', borderRadius: '8px' }}><Cpu size={16} color="white" /></div>
                  <div>
                    <h2>Battery Parameters Input</h2>
                    <p>Enter battery and vehicle parameters for prediction</p>
                  </div>
                </div>

                <div style={{ overflowY: 'auto', flex: 1, paddingRight: '4px' }}>
                  {GROUPS.map((group, idx) => (
                    <div key={idx} className="accordion-item">
                      <div 
                        className="accordion-header"
                        onClick={() => setActiveGroup(activeGroup === group.title ? '' : group.title)}
                      >
                        <div className="accordion-title">
                          {group.icon} {group.title}
                        </div>
                        {activeGroup === group.title ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
                      </div>
                      {activeGroup === group.title && (
                        <div className="accordion-content">
                          {group.fields.map(field => (
                            <div key={field.key} className="input-group">
                              <label>{field.label}</label>
                              <input 
                                type={field.type} 
                                value={formData[field.key]} 
                                onChange={(e) => handleInputChange(e, field.key)}
                              />
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
                  ))}
                </div>

                <button 
                  className="analyze-btn" 
                  onClick={handleAnalyze}
                  disabled={isAnalyzing}
                >
                  <BrainCircuit size={20} />
                  {isAnalyzing ? 'Analyzing...' : 'Analyze Battery'}
                </button>
              </div>
            </div>
          )}

          {(activeTab === 'Dashboard' || activeTab === 'Battery Analysis' || activeTab === 'Visualizations') && (
            <div className={activeTab === 'Battery Analysis' ? "results-section glass-panel" : "results-section"} style={activeTab === 'Battery Analysis' ? { flex: '1', padding: '20px' } : { marginTop: activeTab === 'Dashboard' ? '24px' : '0' }}>
              {activeTab !== 'Battery Analysis' && (
                <div className="glass-panel" style={{ padding: '20px' }}>
                  <div className="section-header" style={{ justifyContent: 'space-between' }}>
                    <div style={{ display: 'flex', gap: '12px', alignItems: 'center' }}>
                      <div style={{ background: 'var(--primary)', padding: '6px', borderRadius: '8px' }}><Activity size={16} color="white" /></div>
                      <div>
                        <h2>Prediction Results</h2>
                        <p>AI analysis based on trained machine learning models</p>
                      </div>
                    </div>
                    <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                      Oct 6, 2026 7:28 PM
                    </div>
                  </div>

                  <div className="charts-row">
                    {/* Failure Risk Chart */}
                    <div className="chart-card glass-panel" style={{ background: 'rgba(15,23,42,0.4)' }}>
                      <h3>Failure Risk Distribution</h3>
                      <div className="chart-container">
                        <ResponsiveContainer width="100%" height="100%">
                          <PieChart>
                            <Pie data={failureRiskData} innerRadius={60} outerRadius={80} paddingAngle={2} dataKey="value" stroke="none">
                              <Cell fill={COLORS[0]} />
                              <Cell fill={COLORS[3]} />
                            </Pie>
                            <Tooltip contentStyle={{ background: 'var(--bg-dark)', border: '1px solid var(--border)' }} />
                          </PieChart>
                        </ResponsiveContainer>
                        <div style={{ position: 'absolute', textAlign: 'center' }}>
                          <div style={{ fontSize: '20px', fontWeight: 'bold' }}>{failureRiskData[0].value.toFixed(2)}%</div>
                          <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Healthy</div>
                        </div>
                      </div>
                      <div className="chart-legend">
                        <div className="legend-item">
                          <div className="legend-label"><div className="legend-dot" style={{ background: COLORS[0] }}></div> Healthy</div>
                          <div>{failureRiskData[0].value.toFixed(4)}%</div>
                        </div>
                        <div className="legend-item">
                          <div className="legend-label"><div className="legend-dot" style={{ background: COLORS[3] }}></div> Failure Risk</div>
                          <div>{failureRiskData[1].value.toFixed(4)}%</div>
                        </div>
                      </div>
                    </div>

                    {/* SOH Chart */}
                    <div className="chart-card glass-panel" style={{ background: 'rgba(15,23,42,0.4)' }}>
                      <h3>Battery Health Status</h3>
                      <div className="chart-container">
                        <ResponsiveContainer width="100%" height="100%">
                          <PieChart>
                            <Pie data={sohData} innerRadius={60} outerRadius={80} paddingAngle={2} dataKey="value" stroke="none">
                              <Cell fill={COLORS[1]} />
                              <Cell fill={COLORS[5]} />
                            </Pie>
                            <Tooltip contentStyle={{ background: 'var(--bg-dark)', border: '1px solid var(--border)' }} />
                          </PieChart>
                        </ResponsiveContainer>
                        <div style={{ position: 'absolute', textAlign: 'center' }}>
                          <div style={{ fontSize: '20px', fontWeight: 'bold' }}>{results.soh.toFixed(1)}%</div>
                          <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>SOH</div>
                        </div>
                      </div>
                      <div className="chart-legend">
                        <div className="legend-item">
                          <div className="legend-label"><div className="legend-dot" style={{ background: COLORS[1] }}></div> Current SOH</div>
                          <div>{results.soh.toFixed(1)}%</div>
                        </div>
                        <div className="legend-item">
                          <div className="legend-label"><div className="legend-dot" style={{ background: COLORS[5] }}></div> Degradation</div>
                          <div>{(100 - results.soh).toFixed(1)}%</div>
                        </div>
                        <div className="legend-item" style={{ marginTop: '4px' }}>
                          <div className="legend-label"><div className="legend-dot" style={{ background: COLORS[0] }}></div> Health Status</div>
                          <div style={{ color: 'var(--success)' }}>{results.soh > 80 ? 'Good' : 'Poor'}</div>
                        </div>
                      </div>
                    </div>

                    {/* RUL Chart */}
                    <div className="chart-card glass-panel" style={{ background: 'rgba(15,23,42,0.4)' }}>
                      <h3>Remaining Useful Life</h3>
                      <div className="chart-container">
                        <ResponsiveContainer width="100%" height="100%">
                          <PieChart>
                            <Pie data={rulData} innerRadius={60} outerRadius={80} paddingAngle={2} dataKey="value" stroke="none">
                              <Cell fill={COLORS[2]} />
                              <Cell fill={COLORS[5]} />
                            </Pie>
                            <Tooltip contentStyle={{ background: 'var(--bg-dark)', border: '1px solid var(--border)' }} />
                          </PieChart>
                        </ResponsiveContainer>
                        <div style={{ position: 'absolute', textAlign: 'center' }}>
                          <div style={{ fontSize: '18px', fontWeight: 'bold' }}>{results.predicted_remaining_life_cycles.toLocaleString(undefined, {maximumFractionDigits: 0})}</div>
                          <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Cycles</div>
                        </div>
                      </div>
                      <div className="chart-legend">
                        <div className="legend-item">
                          <div className="legend-label"><div className="legend-dot" style={{ background: COLORS[2] }}></div> Predicted RUL</div>
                          <div>{results.predicted_remaining_life_cycles.toLocaleString(undefined, {maximumFractionDigits: 2})}</div>
                        </div>
                        <div className="legend-item">
                          <div className="legend-label"><div className="legend-dot" style={{ background: COLORS[5] }}></div> Typical Range</div>
                          <div>0 - 15,000</div>
                        </div>
                        <div className="legend-item" style={{ marginTop: '4px' }}>
                          <div className="legend-label"><div className="legend-dot" style={{ background: COLORS[0] }}></div> Status</div>
                          <div style={{ color: 'var(--success)' }}>Excellent</div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              )}

              {activeTab !== 'Visualizations' && (
                <div className="bottom-info-row" style={{ marginTop: '24px' }}>
                  {/* Key Battery Params */}
                  <div className="key-params-card glass-panel">
                    <div className="section-header" style={{ marginBottom: 0 }}>
                      <Activity size={16} color="var(--primary)" />
                      <h2 style={{ fontSize: '16px' }}>Key Battery Parameters</h2>
                    </div>
                    <div className="params-grid">
                      <div className="param-box">
                        <ZapIcon className="icon" size={20} color="var(--primary)" />
                        <div className="label">Voltage</div>
                        <div className="val">{results.voltage.toFixed(2)} V</div>
                      </div>
                      <div className="param-box">
                        <Thermometer className="icon" size={20} color="var(--danger)" />
                        <div className="label">Temperature</div>
                        <div className="val">{results.temp.toFixed(1)} °C</div>
                      </div>
                      <div className="param-box">
                        <Battery className="icon" size={20} color="var(--success)" />
                        <div className="label">State of Charge</div>
                        <div className="val">{results.soc.toFixed(0)}%</div>
                      </div>
                      <div className="param-box">
                        <ActivityIcon className="icon" size={20} color="var(--accent)" />
                        <div className="label">State of Health</div>
                        <div className="val">{results.soh.toFixed(1)}%</div>
                      </div>
                    </div>
                  </div>

                  {/* AI Assessment */}
                  <div className="ai-assessment-card glass-panel">
                    <div className="section-header" style={{ marginBottom: 0 }}>
                      <BrainCircuit size={16} color="var(--warning)" />
                      <h2 style={{ fontSize: '16px' }}>AI Assessment</h2>
                    </div>
                    
                    {results.failure_prediction === 0 ? (
                      <div className="assessment-content">
                        <div className="assessment-icon"><CheckCircle2 size={24} /></div>
                        <div className="assessment-text">
                          <h4>Battery Healthy</h4>
                          <p>The battery currently shows a healthy condition with very low predicted failure probability. Continue regular maintenance and monitor thermal and electrical parameters.</p>
                        </div>
                      </div>
                    ) : (
                      <div className="assessment-content risk">
                        <div className="assessment-icon"><AlertTriangle size={24} /></div>
                        <div className="assessment-text">
                          <h4>Failure Risk Detected</h4>
                          <p>The AI model has detected anomalies indicating a potential failure risk. Please schedule maintenance immediately and limit fast charging to prevent further degradation.</p>
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              )}
            </div>
          )}

          {(activeTab === 'Prediction History' || activeTab === 'Dashboard') && (
            <div className="history-section glass-panel">
              <div className="section-header">
                <History size={18} color="var(--primary)" />
                <div>
                  <h2>Recent Prediction History</h2>
                  <p>Your recent battery analysis results (stored in session)</p>
                </div>
              </div>
              
              <div className="table-container">
                <table>
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>Date & Time</th>
                      <th>Battery Status</th>
                      <th>Failure Probability</th>
                      <th>Remaining Life (Cycles)</th>
                      <th>SOH</th>
                      <th>Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    {history.map((row, idx) => (
                      <tr key={row.id}>
                        <td>{idx + 1}</td>
                        <td>{row.date}</td>
                        <td><span className={getStatusBadgeClass(row.status)}>{row.status}</span></td>
                        <td>{formatProb(row.probability)}</td>
                        <td>{row.rul.toLocaleString(undefined, {maximumFractionDigits: 2})}</td>
                        <td>{row.soh.toFixed(1)}%</td>
                        <td>
                          <button className="action-btn"><Eye size={14} /></button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {activeTab === 'About Project' && (
            <div className="glass-panel" style={{ padding: '32px' }}>
              <h2>About EV Battery AI</h2>
              <p style={{ marginTop: '16px', color: 'var(--text-muted)', lineHeight: '1.6' }}>
                This project leverages machine learning to monitor electric vehicle battery health and predict potential failures before they occur. 
                Using advanced telemetry data like cell voltage, temperature, state of charge, and historical cycle data, 
                our AI models provide real-time State of Health (SOH) estimates and remaining useful life (RUL) predictions.
              </p>
              <h3 style={{ marginTop: '24px', color: 'var(--text-main)' }}>Key Features</h3>
              <ul style={{ marginTop: '12px', marginLeft: '24px', color: 'var(--text-muted)', lineHeight: '1.6' }}>
                <li>Real-time failure probability assessment</li>
                <li>State of Health (SOH) monitoring and degradation tracking</li>
                <li>Remaining Useful Life (RUL) calculation in cycles</li>
                <li>Comprehensive visual dashboard for battery telemetry</li>
              </ul>
            </div>
          )}

          {activeTab === 'Settings' && (
            <div className="glass-panel" style={{ padding: '32px' }}>
              <h2>Settings</h2>
              <div style={{ marginTop: '24px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
                <div className="input-group">
                  <label>API Endpoint</label>
                  <input type="text" defaultValue="http://127.0.0.1:8000" />
                </div>
                <div className="input-group">
                  <label>Data Refresh Interval (seconds)</label>
                  <input type="number" defaultValue="30" />
                </div>
                <button className="analyze-btn" style={{ width: 'fit-content', padding: '10px 24px', marginTop: '16px' }}>
                  Save Settings
                </button>
              </div>
            </div>
          )}

        </div>
      </div>
    </div>
  );
}
"""

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content[:start_idx] + new_return)
