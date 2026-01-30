#!/bin/bash

echo "🚀 HTML to PDF Converter - Quick Start Script"
echo "=============================================="
echo ""

# Check if running in project directory
if [ ! -f "README.md" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Check for Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install it first:"
    echo "   https://nodejs.org/"
    exit 1
fi

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install it first:"
    echo "   https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Prerequisites check passed!"
echo ""

# Install Static Web Apps CLI if not installed
if ! command -v swa &> /dev/null; then
    echo "📦 Installing Azure Static Web Apps CLI..."
    npm install -g @azure/static-web-apps-cli
    echo "✅ SWA CLI installed!"
else
    echo "✅ SWA CLI already installed"
fi

# Install Azure Functions Core Tools if not installed
if ! command -v func &> /dev/null; then
    echo "📦 Installing Azure Functions Core Tools..."
    npm install -g azure-functions-core-tools@4
    echo "✅ Functions Core Tools installed!"
else
    echo "✅ Functions Core Tools already installed"
fi

# Install Python dependencies
echo ""
echo "📦 Installing Python dependencies..."
cd api
python3 -m pip install -r requirements.txt
cd ..
echo "✅ Python dependencies installed!"

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the development server, run:"
echo "   swa start public --api-location api"
echo ""
echo "Then open: http://localhost:4280"
echo ""
