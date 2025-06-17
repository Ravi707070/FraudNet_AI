from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np
from urllib.parse import urlparse
import os
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Global variables to store models
phishing_model = None
cc_fraud_model = None

def load_models():
    """Load the trained models from pickle files"""
    global phishing_model, cc_fraud_model
    
    
    try:
        # Load phishing model
        phishing_path = "phishing_model.pkl"
        if os.path.exists(phishing_path):
            with open(phishing_path, 'rb') as file:
                phishing_model = pickle.load(file)
            logger.info(f"Loaded phishing model: {type(phishing_model)}")
        else:
            logger.warning(f"Phishing model file not found: {phishing_path}")
        
        # Load credit card fraud model
        cc_path = "creditcrad_model.pkl"
        if os.path.exists(cc_path):
            with open(cc_path, 'rb') as file:
                cc_fraud_model = pickle.load(file)
            logger.info(f"Loaded CC fraud model: {type(cc_fraud_model)}")
        else:
            logger.warning(f"Credit card model file not found: {cc_path}")
            
    except Exception as e:
        logger.error(f"Error loading models: {e}")

def extract_url_features(url):
    """Extract features from URL for phishing detection"""
    try:
        parsed_url = urlparse(url)
        
        features = {
        'url_length': len(url),
        'count_digits': sum(c.isdigit() for c in url),
        'count_letters': sum(c.isalpha() for c in url),
        'count_special_chars': len(re.findall(r'[^\w]', url)),
        'count_dots': url.count('.'),
        'has_https': int('https' in url),
        'has_http': int('http' in url),
        'has_at': int('@' in url),
        'has_hyphen': int('-' in url),
        'has_double_slash': int('//' in url),
        'has_suspicious_words': int(any(word in url.lower() for word in ['login', 'secure', 'bank', 'account', 'verify', 'update']))
        }
        
        return features
    except Exception as e:
        logger.error(f"Error extracting URL features: {e}")
        return None

@app.route('/')
def index():
    """Serve the main HTML page"""
    try:
        with open('frontend.html', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return jsonify({'error': 'Frontend file not found'}), 404

@app.route('/predict-phishing', methods=['POST'])
def predict_phishing():
    """Predict if a URL is phishing"""
    try:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        if phishing_model is None:
            return jsonify({'error': 'Phishing model not available'}), 503
        
        # Extract features
        features = extract_url_features(url)
        if features is None:
            return jsonify({'error': 'Failed to extract URL features'}), 400
        
        # Convert to DataFrame
        features_df = pd.DataFrame([features])
        
        # Make prediction
        prediction = phishing_model.predict(features_df)[0]
        result = "Phishing" if prediction == 1 else "Legitimate"
        
        
        
        return jsonify({
            'prediction': result,
            'features': features
        })
        
    except Exception as e:
        logger.error(f"Error in phishing prediction: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/predict-fraud', methods=['POST'])
def predict_fraud():
    """Predict if a credit card transaction is fraudulent"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'Amount']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        if cc_fraud_model is None:
            return jsonify({'error': 'Credit card fraud model not available'}), 503
        
        # Prepare transaction data
        transaction_data = {
            'Time': float(data['Time']),
            'V1': float(data['V1']),
            'V2': float(data['V2']),
            'V3': float(data['V3']),
            'V4': float(data['V4']),
            'V5': float(data['V5']),
            'Amount': float(data['Amount'])
        }
        
        # Convert to DataFrame
        df = pd.DataFrame([transaction_data])
        
        # Make prediction
        prediction = cc_fraud_model.predict(df)[0]
        result = "Fraudulent" if prediction == 1 else "Legitimate"
        
        
        
        return jsonify({
            'prediction': result,
            'transaction_data': transaction_data
        })
        
    except Exception as e:
        logger.error(f"Error in fraud prediction: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'phishing_model_loaded': phishing_model is not None,
        'cc_fraud_model_loaded': cc_fraud_model is not None
    })

if __name__ == '__main__':

    load_models()
    
    app.run(debug=True, host='0.0.0.0', port=5000)
