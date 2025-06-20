from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch, logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
MODEL_NAME = "rocker417/malicious-url-detection"

LABELS = ["benign", "malicious"]

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

app = Flask(__name__)

@app.route("/scan", methods=["POST"])
def scan_url():
    url = request.get_json().get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    logging.info(f"Scanning URL: {url}")
    tokens = tokenizer(url, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**tokens)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
        score, label_id = torch.max(probs, dim=1)
        label = LABELS[label_id.item()]

    logging.info(f"Result for {url}: {label}")
    return jsonify({
        "label": label,
        "score": round(score.item(), 4)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8999)
