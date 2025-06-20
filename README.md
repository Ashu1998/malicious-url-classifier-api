# Malicious URL Classifier API

A Flask-based REST API that uses machine learning to classify URLs as either benign or malicious. This service leverages a pre-trained transformer model to provide real-time URL threat assessment.

## �� Features

- **Real-time URL Classification**: Instantly classify URLs as benign or malicious
- **Machine Learning Powered**: Uses the `rocker417/malicious-url-detection` transformer model
- **RESTful API**: Simple HTTP POST endpoint for easy integration
- **Docker Support**: Containerized deployment for consistent environments
- **Confidence Scoring**: Returns classification confidence scores
- **Production Ready**: Includes logging and error handling

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **ML Model**: Hugging Face Transformers with PyTorch
- **Model**: `rocker417/malicious-url-detection`
- **Containerization**: Docker & Docker Compose
- **Python Version**: 3.10

## 📋 Prerequisites

- Python 3.10 or higher
- Docker and Docker Compose (for containerized deployment)
- Git

## 🚀 Quick Start

### Option 1: Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd malicious-url-classifier-api
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **The API will be available at**
   ```
   http://localhost:8999
   ```

### Option 2: Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd malicious-url-classifier-api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

## �� API Usage

### Endpoint: `POST /scan`

Classify a URL as benign or malicious.

**Request:**
```json
{
  "url": "https://example.com/suspicious-page"
}
```

**Response:**
```json
{
  "label": "malicious",
  "score": 0.9876
}
```

### Example Usage

#### Using curl
```bash
curl -X POST http://localhost:8999/scan \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/suspicious-page"}'
```

#### Using Python requests
```python
import requests

url = "http://localhost:8999/scan"
data = {"url": "https://example.com/suspicious-page"}

response = requests.post(url, json=data)
result = response.json()

print(f"Classification: {result['label']}")
print(f"Confidence: {result['score']}")
```

#### Using JavaScript/Node.js
```javascript
const response = await fetch('http://localhost:8999/scan', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    url: 'https://example.com/suspicious-page'
  })
});

const result = await response.json();
console.log(`Classification: ${result.label}`);
console.log(`Confidence: ${result.score}`);
```

## �� Configuration

### Environment Variables

The application uses the following default configuration:
- **Port**: 8999
- **Host**: 0.0.0.0 (all interfaces)
- **Model**: `rocker417/malicious-url-detection`

### Docker Configuration

The Docker setup includes:
- **Container Name**: `malicious-url-api`
- **Port Mapping**: `8999:8999`
- **Restart Policy**: `unless-stopped`

## 📊 Model Information

This API uses the `rocker417/malicious-url-detection` model, which is a fine-tuned transformer model specifically designed for URL classification. The model:

- Accepts URLs as input text
- Outputs binary classification (benign/malicious)
- Provides confidence scores for predictions
- Handles URLs up to 128 tokens in length

## 🧪 Testing

### Test with Sample URLs

```bash
# Test with a benign URL
curl -X POST http://localhost:8999/scan \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.google.com"}'

# Test with a potentially malicious URL
curl -X POST http://localhost:8999/scan \
  -H "Content-Type: application/json" \
  -d '{"url": "http://malicious-example.com/fake-login"}'
```

## 📝 API Response Format

### Success Response
```json
{
  "label": "benign|malicious",
  "score": 0.9876
}
```

### Error Response
```json
{
  "error": "No URL provided"
}
```

## 🔍 Logging

The application includes comprehensive logging:
- Request logging with URL information
- Classification results
- Error logging
- Timestamp and log level information

## 🚀 Deployment

### Production Deployment

For production deployment, consider:

1. **Environment Variables**: Set appropriate environment variables
2. **Reverse Proxy**: Use nginx or similar for load balancing
3. **SSL/TLS**: Enable HTTPS for secure communication
4. **Monitoring**: Add health checks and monitoring
5. **Rate Limiting**: Implement rate limiting for API protection

### Docker Production Build

```bash
# Build production image
docker build -t malicious-url-api:latest .

# Run with custom port
docker run -p 8080:8999 malicious-url-api:latest
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This API is for educational and research purposes. The classification results should not be the sole basis for security decisions. Always use multiple security tools and human judgment for critical security assessments.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page for existing problems
2. Create a new issue with detailed information
3. Include logs and error messages when reporting bugs

## 📈 Performance

- **Model Loading**: ~30 seconds on first startup
- **Inference Time**: ~100-500ms per URL (depending on URL length)
- **Memory Usage**: ~2-3GB RAM (includes model weights)
- **Concurrent Requests**: Supports multiple concurrent requests

---

**Built with ❤️ using Flask, Transformers, and PyTorch**