#!/usr/bin/env python3
"""
FraudNet AI - Startup Script
This script helps you run the FraudNet AI application with proper setup.
"""

import os
import sys
import subprocess
import webbrowser
import time
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def check_models():
    """Check if model files exist"""
    models = {
        'phishing_model.pkl': 'Phishing Detection Model',
        'creditcrad_model.pkl': 'Credit Card Fraud Detection Model'
    }
    
    missing_models = []
    for model_file, model_name in models.items():
        if os.path.exists(model_file):
            print(f"✅ {model_name} found")
        else:
            print(f"❌ {model_name} not found ({model_file})")
            missing_models.append(model_file)
    
    return len(missing_models) == 0, missing_models

def install_requirements():
    """Install required packages"""
    print("\n📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install packages: {e}")
        return False

def start_server():
    """Start the Flask server"""
    print("\n🚀 Starting FraudNet AI server...")
    print("📍 Server will be available at: http://localhost:5000")
    print("🔄 Loading models and starting server...")
    
    try:
        # Start the Flask app
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

def main():
    """Main function"""
    print("🛡️  FraudNet AI - Advanced Fraud Detection Suite")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ app.py not found. Please run this script from the FraudNet AI directory.")
        return
    
    # Check models
    models_ok, missing = check_models()
    if not models_ok:
        print(f"\n⚠️  Warning: {len(missing)} model file(s) missing:")
        for model in missing:
            print(f"   - {model}")
        print("\n💡 The application will run in demo mode without real model predictions.")
        
        response = input("\nDo you want to continue anyway? (y/n): ").lower().strip()
        if response != 'y':
            print("Exiting...")
            return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Start server
    print("\n" + "=" * 50)
    start_server()

if __name__ == "__main__":
    main()
