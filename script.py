# Create complete healthcare investing app files for GitHub upload
import os
import json

# Create project structure
os.makedirs('healthinvest-ai', exist_ok=True)
os.makedirs('healthinvest-ai/src', exist_ok=True)
os.makedirs('healthinvest-ai/public', exist_ok=True)
os.makedirs('healthinvest-ai/docs', exist_ok=True)

# 1. Create package.json
package_json = {
    "name": "healthinvest-ai",
    "version": "1.0.0",
    "description": "GPT-5 powered healthcare investment and consulting platform",
    "main": "index.html",
    "scripts": {
        "start": "python -m http.server 8080",
        "dev": "python -m http.server 3000",
        "build": "echo 'Static build - no compilation needed'",
        "deploy": "gh-pages -d ."
    },
    "keywords": ["healthcare", "investment", "consulting", "gpt-5", "ai"],
    "author": "HealthInvest Team",
    "license": "MIT",
    "dependencies": {
        "chart.js": "^4.4.0"
    },
    "devDependencies": {
        "gh-pages": "^6.0.0"
    }
}

with open('healthinvest-ai/package.json', 'w') as f:
    json.dump(package_json, f, indent=2)

print("✅ Created package.json")