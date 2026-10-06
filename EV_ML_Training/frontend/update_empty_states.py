import os

with open('src/App.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Charts
charts_start = content.find('<div className="charts-row">')
charts_end = content.find('                  </div>\n                </div>\n              )}')
if charts_start != -1 and charts_end != -1:
    old_charts = content[charts_start:charts_end]
    new_charts = '''{results ? (
                  <div className="charts-row">''' + old_charts[28:] + '''
                ) : (
                  <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)' }}>
                    <p>Run a battery analysis to see prediction charts.</p>
                  </div>
                )}'''
    content = content.replace(old_charts, new_charts)

# Bottom info
bottom_start = content.find('<div className="bottom-info-row" style={{ marginTop: \'24px\' }}>')
bottom_end = content.find('</div>\n              )}\n            </div>\n          )}\n\n          {(activeTab === \'Prediction History\'')
if bottom_start != -1 and bottom_end != -1:
    old_bottom = content[bottom_start:bottom_end]
    new_bottom = '''{results && (
                <div className="bottom-info-row" style={{ marginTop: '24px' }}>''' + old_bottom[65:] + '''
              )}'''
    content = content.replace(old_bottom, new_bottom)

# History
hist_start = content.find('<div className="table-container">')
hist_end = content.find('</div>\n            </div>\n          )}\n\n          {activeTab === \'About Project\'')
if hist_start != -1 and hist_end != -1:
    old_hist = content[hist_start:hist_end]
    new_hist = '''{history.length > 0 ? (
              <div className="table-container">''' + old_hist[33:] + '''
            ) : (
              <div style={{ padding: '24px', textAlign: 'center', color: 'var(--text-muted)' }}>
                <p>No predictions yet. Run a battery analysis to see your prediction history.</p>
              </div>
            )}'''
    content = content.replace(old_hist, new_hist)

with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated UI successfully")
