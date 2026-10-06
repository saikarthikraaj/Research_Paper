          {/* Top Stats Cards */}
          <div className="top-cards-grid">
            <div className="stat-card glass-panel">
              <div className="stat-icon health"><Battery size={24} /></div>
              <div className="stat-info">
                <h3>Battery Health (SOH)</h3>
                <div className="value">{results.soh.toFixed(1)}%</div>
                <p>State of Health</p>
              </div>