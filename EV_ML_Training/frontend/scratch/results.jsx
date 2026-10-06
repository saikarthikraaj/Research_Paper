            {/* Right Results Panel */}
            <div className="results-section">
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

              <div className="bottom-info-row">
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

            </div>
