#!/bin/bash
# Check for existing environment
if [ -d "fyp-env" ]; then
    echo "🗑️ Existing environment found. Removing..."
    rm -rf fyp-env
fi

# Clean environment setup and server launch
echo "🚀 Creating fresh FYP environment..."
python3 -m venv fyp-env
source fyp-env/bin/activate
echo "📦 Installing requirements..."
pip install -r requirements.txt
echo "🌐 Starting Streamlit server..."
streamlit run ui.py 