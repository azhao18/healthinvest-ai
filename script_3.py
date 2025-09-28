# Create comprehensive JavaScript application
js_content = '''// HealthInvest AI - Healthcare Investment Platform
// GPT-5 Powered Analytics and Consulting

// Sample data for demonstrations
const healthcareData = {
    investments: [
        { name: "MedTech Innovations", sector: "Medical Devices", stage: "Series B", valuation: "$150M", roi: "25%", risk: "Medium", growth: 12.5 },
        { name: "AI Diagnostics Corp", sector: "Healthcare AI", stage: "Series A", valuation: "$80M", roi: "35%", risk: "High", growth: 45.2 },
        { name: "Digital Therapeutics Inc", sector: "Digital Health", stage: "Seed", valuation: "$25M", roi: "45%", risk: "High", growth: 67.8 },
        { name: "Pharma Pipeline Partners", sector: "Pharmaceuticals", stage: "Growth", valuation: "$500M", roi: "18%", risk: "Low", growth: 8.3 },
        { name: "Telemedicine Solutions", sector: "Telehealth", stage: "Series C", valuation: "$300M", roi: "22%", risk: "Medium", growth: 28.7 }
    ],
    
    competitiveData: [
        { name: "Company A", marketShare: 25, innovation: 85 },
        { name: "Company B", marketShare: 18, innovation: 72 },
        { name: "Company C", marketShare: 15, innovation: 90 },
        { name: "Company D", marketShare: 12, innovation: 68 },
        { name: "Our Target", marketShare: 8, innovation: 95 }
    ]
};

// Initialize application when DOM loads
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    setupNavigation();
    loadDashboard();
    setupChatInterface();
    setupCalculators();
    setupFrameworks();
    
    console.log('🚀 HealthInvest AI Platform Initialized');
}

// Navigation Management
function setupNavigation() {
    const navTabs = document.querySelectorAll('.nav-tab');
    
    navTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const targetTab = tab.dataset.tab;
            switchTab(targetTab);
        });
    });
}

function switchTab(tabName) {
    // Update navigation
    document.querySelectorAll('.nav-tab').forEach(tab => {
        tab.classList.toggle('active', tab.dataset.tab === tabName);
    });
    
    // Update content
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.toggle('active', content.id === tabName);
    });
    
    // Load tab-specific content
    switch(tabName) {
        case 'dashboard':
            loadDashboard();
            break;
        case 'market':
            loadMarketIntelligence();
            break;
        case 'consulting':
            loadConsultingFrameworks();
            break;
    }
}

// Dashboard Functions
function loadDashboard() {
    renderInvestmentsList();
    renderPortfolioChart();
}

function renderInvestmentsList() {
    const container = document.getElementById('investmentsList');
    if (!container) return;
    
    const html = healthcareData.investments.map(investment => `
        <div class="investment-item">
            <div class="investment-info">
                <h4>${investment.name}</h4>
                <p>${investment.sector} • ${investment.stage}</p>
            </div>
            <div class="investment-metrics">
                <div class="roi">${investment.roi}</div>
                <div class="risk-badge ${investment.risk.toLowerCase()}">${investment.risk}</div>
            </div>
        </div>
    `).join('');
    
    container.innerHTML = html;
}

function renderPortfolioChart() {
    const ctx = document.getElementById('portfolioChart');
    if (!ctx) return;
    
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: healthcareData.investments.map(inv => inv.sector),
            datasets: [{
                data: healthcareData.investments.map(inv => inv.growth),
                backgroundColor: [
                    '#2563eb',
                    '#10b981', 
                    '#f59e0b',
                    '#ef4444',
                    '#8b5cf6'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
}

// Market Intelligence
function loadMarketIntelligence() {
    renderCompetitiveChart();
}

function renderCompetitiveChart() {
    const ctx = document.getElementById('competitiveChart');
    if (!ctx) return;
    
    new Chart(ctx, {
        type: 'bubble',
        data: {
            datasets: [{
                label: 'Competitive Positioning',
                data: healthcareData.competitiveData.map(company => ({
                    x: company.marketShare,
                    y: company.innovation,
                    r: company.name === 'Our Target' ? 15 : 8
                })),
                backgroundColor: healthcareData.competitiveData.map(company => 
                    company.name === 'Our Target' ? '#ef4444' : '#2563eb'
                )
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Market Share (%)'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Innovation Score'
                    }
                }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const company = healthcareData.competitiveData[context.dataIndex];
                            return `${company.name}: ${company.marketShare}% market share, ${company.innovation} innovation score`;
                        }
                    }
                }
            }
        }
    });
}

// Feature Functions
function showFeature(feature) {
    const messages = {
        'due-diligence': 'GPT-5 Analysis: Processing 247 documents... Found key insights on regulatory compliance, competitive positioning, and financial projections. Risk score: Medium-High.',
        'valuation': 'GPT-5 Valuation: Based on comparable analysis and DCF modeling, estimated valuation range: $85M - $120M with 68% confidence interval.',
        'portfolio': 'GPT-5 Recommendation: Increase healthcare AI allocation by 15%, reduce traditional pharma by 8%. Expected portfolio improvement: +12.3% ROI.'
    };
    
    alert(messages[feature] || 'GPT-5 Analysis in progress...');
}

// Valuation Calculator
function setupCalculators() {
    // Trial risk calculator
    const trialPhaseSelect = document.getElementById('trialPhase');
    const indicationSelect = document.getElementById('indication');
    
    if (trialPhaseSelect && indicationSelect) {
        [trialPhaseSelect, indicationSelect].forEach(select => {
            select.addEventListener('change', updateTrialRisk);
        });
    }
}

function calculateValuation() {
    const companyType = document.getElementById('companyType').value;
    const revenue = parseFloat(document.getElementById('revenue').value) || 0;
    const growthRate = parseFloat(document.getElementById('growthRate').value) || 0;
    const stage = document.getElementById('stage').value;
    
    // Simple valuation calculation (demonstration)
    const multipliers = {
        'Biotech': { base: 8, growth: 0.5 },
        'Medical Device': { base: 6, growth: 0.3 },
        'Digital Health': { base: 12, growth: 0.8 },
        'Healthcare AI': { base: 15, growth: 1.2 }
    };
    
    const stageMultipliers = {
        'Seed': 0.5,
        'Series A': 0.8,
        'Series B': 1.0,
        'Growth': 1.3
    };
    
    const mult = multipliers[companyType];
    const valuation = revenue * (mult.base + growthRate * mult.growth) * stageMultipliers[stage];
    
    const resultDiv = document.getElementById('valuationResult');
    if (resultDiv) {
        resultDiv.style.display = 'block';
        resultDiv.innerHTML = `
            <h4>🤖 GPT-5 Valuation Analysis</h4>
            <p><strong>Estimated Valuation:</strong> $${valuation.toFixed(1)}M</p>
            <p><strong>Revenue Multiple:</strong> ${(valuation/revenue).toFixed(1)}x</p>
            <p><strong>Confidence Level:</strong> 78%</p>
            <p><strong>Key Factors:</strong> ${companyType} sector shows ${growthRate}% growth in ${stage} stage companies.</p>
        `;
    }
}

function updateTrialRisk() {
    const phase = document.getElementById('trialPhase').value;
    const indication = document.getElementById('indication').value;
    
    // Simplified risk calculation
    const baseRisks = { '1': 85, '2': 63, '3': 45 };
    const indicationMultipliers = {
        'Oncology': 0.8,
        'Cardiology': 1.1,
        'Neurology': 0.9,
        'Other': 1.0
    };
    
    const probability = Math.round(baseRisks[phase] * indicationMultipliers[indication]);
    
    const probDisplay = document.getElementById('successProb');
    if (probDisplay) {
        probDisplay.textContent = `${probability}%`;
    }
}

function calculateTrialRisk() {
    updateTrialRisk();
    alert('🤖 GPT-5 Analysis: Updated clinical trial success probability based on historical data from 15,000+ similar trials. Includes FDA feedback patterns and regulatory pathway optimization suggestions.');
}

// Consulting Frameworks
function setupFrameworks() {
    const frameworkCards = document.querySelectorAll('.framework-card');
    
    frameworkCards.forEach(card => {
        card.addEventListener('click', () => {
            const framework = card.dataset.framework;
            switchFramework(framework);
        });
    });
}

function switchFramework(framework) {
    // Update cards
    document.querySelectorAll('.framework-card').forEach(card => {
        card.classList.toggle('active', card.dataset.framework === framework);
    });
    
    // Update content
    document.querySelectorAll('.framework-content').forEach(content => {
        content.classList.toggle('active', content.id === `${framework}-detail`);
    });
}

function loadConsultingFrameworks() {
    // Initialize Porter's Five Forces visualization
    animateForceMeters();
}

function animateForceMeters() {
    const forceMeters = document.querySelectorAll('.force-level');
    forceMeters.forEach((meter, index) => {
        setTimeout(() => {
            meter.style.width = meter.style.width || '0%';
        }, index * 200);
    });
}

function generateFrameworkReport(framework) {
    const reports = {
        'porters': '🤖 GPT-5 Porter\\'s Five Forces Analysis: High competitive rivalry (4/5) driven by 47 active AI diagnostic startups. Buyer power elevated due to hospital consolidation. Regulatory barriers moderate entry threats. Strategic recommendation: Focus on specialized niches with high switching costs.',
        'vbc': '🤖 GPT-5 Value-Based Care Analysis: Clinical outcomes improved 23% vs. baseline. Cost per episode reduced $2,847. Patient satisfaction: 94%. Population health metrics exceed CMS benchmarks. ROI projection: 156% over 3 years.',
        'revenue': '🤖 GPT-5 Revenue Cycle Analysis: Current DSO: 47 days. Denial rate: 12%. Optimization potential: $2.3M annually. Key improvements: automated prior auth (87% faster), AI coding assistance (94% accuracy), patient engagement platform (+31% collections).'
    };
    
    alert(reports[framework] || 'GPT-5 framework analysis in progress...');
}

// Chat Interface
function setupChatInterface() {
    const chatToggle = document.getElementById('chatToggle');
    const chatSend = document.getElementById('chatSend');
    const chatInput = document.getElementById('chatInput');
    const chatMessages = document.getElementById('chatMessages');
    
    if (chatToggle) {
        chatToggle.addEventListener('click', toggleChat);
    }
    
    if (chatSend && chatInput) {
        chatSend.addEventListener('click', sendMessage);
        chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') sendMessage();
        });
    }
}

function toggleChat() {
    const chatContainer = document.getElementById('chatContainer');
    const chatToggle = document.getElementById('chatToggle');
    
    if (chatContainer.style.height === '60px') {
        chatContainer.style.height = 'auto';
        chatToggle.textContent = '−';
    } else {
        chatContainer.style.height = '60px';
        chatToggle.textContent = '+';
    }
}

function sendMessage() {
    const chatInput = document.getElementById('chatInput');
    const message = chatInput.value.trim();
    
    if (!message) return;
    
    addChatMessage(message, 'user');
    chatInput.value = '';
    
    // Simulate GPT-5 response
    setTimeout(() => {
        const response = generateGPTResponse(message);
        addChatMessage(response, 'ai');
    }, 1500);
}

function addChatMessage(message, sender) {
    const chatMessages = document.getElementById('chatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    
    const avatar = sender === 'ai' ? '🤖' : '👤';
    
    messageDiv.innerHTML = `
        <div class="avatar">${avatar}</div>
        <div class="content">
            <p>${message}</p>
        </div>
    `;
    
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function askGPT(question) {
    const chatInput = document.getElementById('chatInput');
    chatInput.value = question;
    sendMessage();
}

function generateGPTResponse(message) {
    const responses = {
        'ai diagnostics': '🤖 AI diagnostics market is projected to reach $37.4B by 2027, growing at 32% CAGR. Key drivers: radiological AI (40% market share), pathology solutions (23%), and clinical decision support (18%). Top investment opportunities include companies with FDA-cleared algorithms and established hospital partnerships.',
        
        'telemedicine roi': '🤖 Telemedicine investments show strong ROI metrics: average 156% ROI over 3 years, 67% reduction in operational costs, and 23% improvement in patient satisfaction scores. Key value drivers: reduced real estate costs, increased provider utilization, and expanded market reach. Current valuation multiples: 8-15x revenue.',
        
        'regulatory risks': '🤖 Digital therapeutics face moderate-high regulatory risk. FDA\\'s Digital Therapeutics Guidance requires clinical validation, with approval timelines averaging 18-24 months. Success rates: 73% for Class II devices, 45% for Class III. Mitigation strategies: early FDA engagement, robust clinical data, and experienced regulatory team.',
        
        'default': '🤖 I can help you analyze healthcare investments, market opportunities, consulting frameworks, and risk assessments. Try asking about specific sectors like AI diagnostics, digital therapeutics, or telemedicine. I can also run valuations, assess clinical trial risks, or apply consulting frameworks like Porter\\'s Five Forces.'
    };
    
    const lowerMessage = message.toLowerCase();
    
    for (const [key, response] of Object.entries(responses)) {
        if (key !== 'default' && lowerMessage.includes(key)) {
            return response;
        }
    }
    
    return responses.default;
}

// Utility Functions
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 0,
        maximumFractionDigits: 1
    }).format(amount * 1000000);
}

function showNotification(message, type = 'info') {
    // Simple notification system
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 2rem;
        right: 2rem;
        padding: 1rem;
        background: var(--primary-color);
        color: white;
        border-radius: 0.5rem;
        box-shadow: var(--shadow-lg);
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Add slide-in animation
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
`;
document.head.appendChild(style);

// Export functions for global access
window.calculateValuation = calculateValuation;
window.calculateTrialRisk = calculateTrialRisk;
window.showFeature = showFeature;
window.generateFrameworkReport = generateFrameworkReport;
window.askGPT = askGPT;

console.log('💊 HealthInvest AI - Powered by GPT-5 - Ready for Healthcare Investment Analysis');'''

with open('healthinvest-ai/src/app.js', 'w') as f:
    f.write(js_content)

print("✅ Created comprehensive JavaScript application")