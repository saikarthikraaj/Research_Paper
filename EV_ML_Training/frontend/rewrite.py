import re

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

banner = re.search(r'(          {/\* Main Banner \*/}.*?          </div>)', content, re.DOTALL)
top_cards = re.search(r'(          {/\* Top Stats Cards \*/}.*?          </div>)', content, re.DOTALL)
input_panel = re.search(r'(            {/\* Left Inputs Panel \*/}.*?            </div>)', content, re.DOTALL)

# Right Results Panel - ends with 2 closing divs before the next section
results_panel_str = content[content.find('            {/* Right Results Panel */}'):content.find('          </div>\n\n          {/* History */}')]

history_panel = re.search(r'(          {/\* History \*/}.*?          </div>)', content, re.DOTALL)

import os
os.makedirs('scratch', exist_ok=True)
with open('scratch/banner.jsx', 'w', encoding='utf-8') as f: f.write(banner.group(1) if banner else 'none')
with open('scratch/top_cards.jsx', 'w', encoding='utf-8') as f: f.write(top_cards.group(1) if top_cards else 'none')
with open('scratch/input.jsx', 'w', encoding='utf-8') as f: f.write(input_panel.group(1) if input_panel else 'none')
with open('scratch/results.jsx', 'w', encoding='utf-8') as f: f.write(results_panel_str)
with open('scratch/history.jsx', 'w', encoding='utf-8') as f: f.write(history_panel.group(1) if history_panel else 'none')

print("Extraction done.")

# Let's rebuild App.jsx
header = content[:content.find('        <div className="dashboard-container">')]
footer = content[content.find('      </div>\n    </div>\n  );\n}'):]

new_content = header + """        <div className="dashboard-container">
          {activeTab === 'Dashboard' && (
            <>
""" + (banner.group(1) if banner else '') + "\n" + (top_cards.group(1) if top_cards else '') + "\n" + """              <div className="main-grid">
""" + (input_panel.group(1) if input_panel else '') + "\n" + results_panel_str + """              </div>
""" + (history_panel.group(1) if history_panel else '') + """
            </>
          )}

          {activeTab === 'Battery Analysis' && (
            <>
              <div className="main-grid">
""" + (input_panel.group(1) if input_panel else '') + "\n" + results_panel_str + """              </div>
            </>
          )}

          {activeTab === 'Prediction History' && (
            <>
""" + (history_panel.group(1) if history_panel else '') + """            </>
          )}

          {activeTab === 'Visualizations' && (
            <>
              <div className="main-grid">
""" + results_panel_str + """              </div>
            </>
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
""" + footer

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Rewrite done.")
