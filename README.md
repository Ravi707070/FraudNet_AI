# 🛡️ FraudNet AI - Advanced Fraud Detection Suite

A comprehensive fraud detection system powered by machine learning, featuring real-time phishing URL detection and credit card fraud analysis.

## ✨ Features

- **🔍 Phishing Detection**: Advanced URL analysis using machine learning to identify malicious websites
- **💳 Credit Card Fraud Detection**: Sophisticated transaction analysis to detect fraudulent activities
- **🎨 Modern Web Interface**: Beautiful, responsive frontend with real-time results
- **🚀 Real-time Processing**: Instant analysis with confidence scores
- **📊 Visual Analytics**: Interactive charts and statistics
- **🔒 Secure**: No data storage, all processing done locally

## 🏗️ Architecture

```
FraudNet AI/
├── app.py                          # Flask backend server
├── frontend.html                   # Modern web interface
├── phishing_model.pkl              # Trained phishing detection model
├── creditcrad_model.pkl            # Trained credit card fraud model
├── requirements.txt                # Python dependencies
├── run_fraudnet.py                 # Easy startup script
└── README.md                       # This file
```

## 🚀 Quick Start

### Option 1: Easy Setup (Recommended)
```bash
# Navigate to the FraudNet AI directory
cd "FraudNet AI"

# Run the startup script
python run_fraudnet.py
```

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```

### Option 3: Using Streamlit (Alternative)
```bash
# Run the Streamlit version
streamlit run fraudnetai.py
```

## 🌐 Access the Application

Once the server is running, open your web browser and navigate to:
- **Main Application**: http://localhost:5000
- **Health Check**: http://localhost:5000/health

## 🔧 API Endpoints

### Phishing Detection
```http
POST /predict-phishing
Content-Type: application/json

{
  "url": "https://example.com"
}
```

**Response:**
```json
{
  "prediction": "Phishing" | "Legitimate",
  "confidence": 0.95,
  "features": { ... }
}
```

### Credit Card Fraud Detection
```http
POST /predict-fraud
Content-Type: application/json

{
  "Time": 86400,
  "V1": -1.3598,
  "V2": -0.0728,
  "V3": 2.5363,
  "V4": 1.3782,
  "V5": -0.3383,
  "Amount": 149.62
}
```

**Response:**
```json
{
  "prediction": "Fraudulent" | "Legitimate",
  "confidence": 0.87,
  "transaction_data": { ... }
}
```

## 📊 Model Information

### Phishing Detection Model
- **Algorithm**: Random Forest Classifier
- **Features**: 11 URL-based features including length, character counts, suspicious patterns
- **Accuracy**: ~99.1%
- **Input**: Website URL
- **Output**: Phishing/Legitimate classification with confidence score

### Credit Card Fraud Detection Model
- **Algorithm**: Random Forest Classifier
- **Features**: Time, V1-V5 (PCA components), Amount
- **Accuracy**: ~99.9%
- **Input**: Transaction details
- **Output**: Fraudulent/Legitimate classification with confidence score

## 🎯 Usage Examples

### Phishing Detection
1. Click "Phishing Detection" button
2. Enter a URL (e.g., `https://suspicious-site.com`)
3. Click "Analyze URL Security"
4. View results with confidence score

### Credit Card Fraud Detection
1. Click "Fraud Detection" button
2. Fill in transaction details:
   - Time: 86400
   - V1-V5: Principal component values
   - Amount: Transaction amount
3. Use "Fill Sample Data" for testing
4. Click "Analyze Transaction"
5. View fraud analysis results

## 🛠️ Technical Requirements

- **Python**: 3.7 or higher
- **Dependencies**: Flask, pandas, numpy, scikit-learn
- **Models**: Pre-trained .pkl files
- **Browser**: Modern web browser with JavaScript enabled

## 🔍 Troubleshooting

### Model Files Missing
If you see "model not available" errors:
1. Ensure `phishing_model.pkl` and `creditcrad_model.pkl` are in the directory
2. Check file permissions
3. The app will run in demo mode without real models

### Port Already in Use
If port 5000 is busy:
```bash
# Kill process using port 5000
lsof -ti:5000 | xargs kill -9

# Or change port in app.py
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Installation Issues
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install with specific versions
pip install -r requirements.txt --force-reinstall
```

## 🎨 Frontend Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Dark Theme**: Modern dark UI with gradient effects
- **Animated Elements**: Smooth transitions and loading states
- **Real-time Charts**: Interactive accuracy visualization
- **Form Validation**: Input validation and error handling
- **Demo Mode**: Fallback simulation when models unavailable

## 🔒 Security Notes

- All processing is done locally
- No data is stored or transmitted to external servers
- Models run entirely on your machine
- CORS enabled for development (disable in production)

## 📈 Performance

- **Response Time**: < 100ms for most predictions
- **Memory Usage**: ~50MB with models loaded
- **Concurrent Users**: Supports multiple simultaneous requests
- **Scalability**: Can be deployed with gunicorn for production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Scikit-learn for machine learning algorithms
- Flask for the web framework
- Chart.js for data visualization
- Tailwind CSS for styling

---

**FraudNet AI** - Protecting the digital world, one prediction at a time. 🛡️
