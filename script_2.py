# Create comprehensive CSS styling
css_content = '''/* Healthcare Investment Platform Styles */

:root {
  --primary-color: #2563eb;
  --secondary-color: #10b981;
  --accent-color: #f59e0b;
  --danger-color: #ef4444;
  --bg-color: #f8fafc;
  --surface-color: #ffffff;
  --text-color: #1e293b;
  --text-secondary: #64748b;
  --border-color: #e2e8f0;
  --shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: var(--bg-color);
  color: var(--text-color);
  line-height: 1.6;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

/* Header */
.header {
  background: var(--surface-color);
  border-bottom: 1px solid var(--border-color);
  box-shadow: var(--shadow);
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 0;
}

.logo h1 {
  color: var(--primary-color);
  font-size: 1.8rem;
  margin-bottom: 0.25rem;
}

.subtitle {
  color: var(--text-secondary);
  font-size: 0.875rem;
}

.gpt5-badge {
  background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 2rem;
  font-size: 0.875rem;
  font-weight: 600;
}

/* Navigation */
.nav {
  background: var(--surface-color);
  border-bottom: 1px solid var(--border-color);
}

.nav-tabs {
  display: flex;
  overflow-x: auto;
}

.nav-tab {
  background: none;
  border: none;
  padding: 1rem 1.5rem;
  cursor: pointer;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text-secondary);
  border-bottom: 2px solid transparent;
  transition: all 0.2s;
  white-space: nowrap;
}

.nav-tab:hover {
  color: var(--primary-color);
}

.nav-tab.active {
  color: var(--primary-color);
  border-bottom-color: var(--primary-color);
}

/* Main Content */
.main {
  padding: 2rem 0;
}

.tab-content {
  display: none;
}

.tab-content.active {
  display: block;
}

.dashboard-header {
  text-align: center;
  margin-bottom: 2rem;
}

.dashboard-header h2 {
  font-size: 2rem;
  color: var(--text-color);
  margin-bottom: 0.5rem;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: var(--surface-color);
  padding: 1.5rem;
  border-radius: 0.5rem;
  box-shadow: var(--shadow);
  text-align: center;
}

.stat-card h3 {
  font-size: 0.875rem;
  color: var(--text-secondary);
  margin-bottom: 0.5rem;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--text-color);
  margin-bottom: 0.5rem;
}

.stat-change {
  font-size: 0.875rem;
  font-weight: 600;
}

.stat-change.positive {
  color: var(--secondary-color);
}

.stat-change.negative {
  color: var(--danger-color);
}

/* Dashboard Grid */
.dashboard-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
  margin-bottom: 2rem;
}

.chart-container,
.investments-list {
  background: var(--surface-color);
  padding: 1.5rem;
  border-radius: 0.5rem;
  box-shadow: var(--shadow);
}

.chart-container h3,
.investments-list h3 {
  margin-bottom: 1rem;
  color: var(--text-color);
}

/* Investment List */
.investment-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 0;
  border-bottom: 1px solid var(--border-color);
}

.investment-item:last-child {
  border-bottom: none;
}

.investment-info h4 {
  font-size: 0.875rem;
  color: var(--text-color);
  margin-bottom: 0.25rem;
}

.investment-info p {
  font-size: 0.75rem;
  color: var(--text-secondary);
}

.investment-metrics {
  text-align: right;
}

.roi {
  font-weight: 600;
  color: var(--secondary-color);
}

.risk-badge {
  font-size: 0.75rem;
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  font-weight: 500;
}

.risk-badge.high {
  background: #fee2e2;
  color: #dc2626;
}

.risk-badge.medium {
  background: #fef3c7;
  color: #d97706;
}

.risk-badge.low {
  background: #dcfce7;
  color: #16a34a;
}

/* Analysis Grid */
.analysis-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.analysis-card {
  background: var(--surface-color);
  padding: 1.5rem;
  border-radius: 0.5rem;
  box-shadow: var(--shadow);
  text-align: center;
}

.analysis-card h3 {
  color: var(--primary-color);
  margin-bottom: 1rem;
}

.analysis-card p {
  color: var(--text-secondary);
  margin-bottom: 1.5rem;
}

/* Buttons */
.btn-primary {
  background: var(--primary-color);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.375rem;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.2s;
}

.btn-primary:hover {
  background: #1d4ed8;
}

/* Valuation Calculator */
.valuation-calculator {
  background: var(--surface-color);
  padding: 2rem;
  border-radius: 0.5rem;
  box-shadow: var(--shadow);
  margin-top: 2rem;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: var(--text-color);
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid var(--border-color);
  border-radius: 0.375rem;
  font-size: 0.875rem;
}

#valuationResult {
  margin-top: 1rem;
  padding: 1rem;
  background: #f0f9ff;
  border: 1px solid #bae6fd;
  border-radius: 0.375rem;
  display: none;
}

/* Frameworks */
.frameworks-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.framework-card {
  background: var(--surface-color);
  padding: 1.5rem;
  border-radius: 0.5rem;
  box-shadow: var(--shadow);
  cursor: pointer;
  transition: all 0.2s;
  border: 2px solid transparent;
}

.framework-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.framework-card.active {
  border-color: var(--primary-color);
}

.framework-detail {
  background: var(--surface-color);
  padding: 2rem;
  border-radius: 0.5rem;
  box-shadow: var(--shadow);
}

.framework-content {
  display: none;
}

.framework-content.active {
  display: block;
}

/* Porter's Five Forces */
.forces-grid {
  display: grid;
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.force-item {
  padding: 1rem;
  border-left: 4px solid var(--primary-color);
  background: #f8fafc;
}

.force-item h4 {
  margin-bottom: 0.5rem;
  color: var(--text-color);
}

.force-meter {
  background: #e2e8f0;
  height: 0.5rem;
  border-radius: 0.25rem;
  margin: 0.5rem 0;
  overflow: hidden;
}

.force-level {
  height: 100%;
  background: linear-gradient(90deg, var(--secondary-color), var(--accent-color));
  transition: width 0.3s;
}

/* Market Intelligence */
.market-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-bottom: 2rem;
}

.market-card {
  background: var(--surface-color);
  padding: 2rem;
  border-radius: 0.5rem;
  box-shadow: var(--shadow);
  text-align: center;
}

.tam-sam-som {
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin-top: 1rem;
}

.market-circle {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: white;
  font-weight: 600;
  font-size: 0.875rem;
}

.market-circle.tam {
  background: var(--primary-color);
}

.market-circle.sam {
  background: var(--secondary-color);
}

.market-circle.som {
  background: var(--accent-color);
}

.market-trends {
  background: var(--surface-color);
  padding: 2rem;
  border-radius: 0.5rem;
  box-shadow: var(--shadow);
}

.trend-list {
  margin-top: 1rem;
}

.trend-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 0;
  border-bottom: 1px solid var(--border-color);
}

.trend-item:last-child {
  border-bottom: none;
}

.competitive-landscape {
  background: var(--surface-color);
  padding: 2rem;
  border-radius: 0.5rem;
  box-shadow: var(--shadow);
  margin-top: 2rem;
}

/* Risk Assessment */
.risk-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.risk-category {
  background: var(--surface-color);
  padding: 1.5rem;
  border-radius: 0.5rem;
  box-shadow: var(--shadow);
}

.risk-category h3 {
  margin-bottom: 1rem;
  color: var(--text-color);
}

.risk-level {
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: 600;
  display: inline-block;
  margin-bottom: 1rem;
}

.risk-level.high {
  background: #fee2e2;
  color: #dc2626;
}

.risk-level.medium {
  background: #fef3c7;
  color: #d97706;
}

.risk-level.low {
  background: #dcfce7;
  color: #16a34a;
}

.risk-category ul {
  list-style: none;
  padding-left: 0;
}

.risk-category li {
  padding: 0.25rem 0;
  color: var(--text-secondary);
  position: relative;
  padding-left: 1rem;
}

.risk-category li:before {
  content: "•";
  color: var(--primary-color);
  position: absolute;
  left: 0;
}

/* Risk Calculator */
.risk-calculator {
  background: var(--surface-color);
  padding: 2rem;
  border-radius: 0.5rem;
  box-shadow: var(--shadow);
}

.calculator-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 2rem;
  margin-bottom: 1.5rem;
}

.calc-input label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.calc-input select {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid var(--border-color);
  border-radius: 0.375rem;
}

.calc-result {
  text-align: center;
}

.probability-display {
  background: var(--primary-color);
  color: white;
  padding: 1rem;
  border-radius: 0.5rem;
  font-size: 2rem;
  font-weight: 700;
  margin-top: 0.5rem;
}

/* Chat Interface */
.chat-container {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  width: 400px;
  max-width: calc(100vw - 4rem);
  background: var(--surface-color);
  border-radius: 0.5rem;
  box-shadow: var(--shadow-lg);
  z-index: 1000;
}

.chat-header {
  background: var(--primary-color);
  color: white;
  padding: 1rem;
  border-radius: 0.5rem 0.5rem 0 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.chat-header h3 {
  font-size: 1rem;
}

.chat-toggle {
  background: none;
  border: none;
  color: white;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 0;
  width: 2rem;
  height: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.chat-messages {
  max-height: 300px;
  overflow-y: auto;
  padding: 1rem;
}

.message {
  display: flex;
  gap: 0.75rem;
  margin-bottom: 1rem;
}

.avatar {
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
  flex-shrink: 0;
}

.message.ai .avatar {
  background: var(--primary-color);
}

.message.user .avatar {
  background: var(--secondary-color);
}

.content {
  flex: 1;
}

.content p {
  margin-bottom: 0.5rem;
  font-size: 0.875rem;
  line-height: 1.4;
}

.suggestions {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-top: 1rem;
}

.suggestions button {
  background: #f1f5f9;
  border: 1px solid var(--border-color);
  padding: 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  cursor: pointer;
  text-align: left;
  transition: background 0.2s;
}

.suggestions button:hover {
  background: #e2e8f0;
}

.chat-input {
  display: flex;
  border-top: 1px solid var(--border-color);
}

.chat-input input {
  flex: 1;
  border: none;
  padding: 1rem;
  font-size: 0.875rem;
  border-radius: 0 0 0 0.5rem;
}

.chat-input input:focus {
  outline: none;
}

.chat-input button {
  background: var(--primary-color);
  color: white;
  border: none;
  padding: 1rem 1.5rem;
  cursor: pointer;
  border-radius: 0 0 0.5rem 0;
  font-size: 0.875rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .dashboard-grid {
    grid-template-columns: 1fr;
  }
  
  .market-grid {
    grid-template-columns: 1fr;
  }
  
  .calculator-grid {
    grid-template-columns: 1fr;
  }
  
  .tam-sam-som {
    flex-direction: column;
    gap: 1rem;
  }
  
  .chat-container {
    width: calc(100vw - 2rem);
    right: 1rem;
    bottom: 1rem;
  }
  
  .nav-tabs {
    padding: 0 1rem;
  }
  
  .nav-tab {
    font-size: 0.75rem;
    padding: 0.75rem 1rem;
  }
}

/* Loading Animation */
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.loading {
  animation: pulse 2s infinite;
}

/* Feature Highlights */
.feature-highlight {
  background: linear-gradient(45deg, #f0f9ff, #ecfdf5);
  border: 1px solid #bae6fd;
  border-radius: 0.5rem;
  padding: 1rem;
  margin: 1rem 0;
}

.feature-highlight h4 {
  color: var(--primary-color);
  margin-bottom: 0.5rem;
}'''

with open('healthinvest-ai/src/style.css', 'w') as f:
    f.write(css_content)

print("✅ Created comprehensive CSS styles")