import json
import os
import re
from flask import Flask, request, jsonify
from scraper import scrape_brand_page
from replit import web
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv("API_KEY")  # From .env (sikeee)
EXTENSION_ID = "bmfcaoaiaclbdibjflmmodfnnooblfol"
CACHE_FILE = "brand_cache.json"

# Load brand cache if available
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "r") as f:
        brand_cache = json.load(f)
else:
    brand_cache = {}

@app.before_request
def check_authorization():
    key = request.headers.get("X-API-Key")
    origin = request.headers.get("Origin") or request.headers.get("Referer")

    if key != API_KEY:
        return jsonify({"error": "Unauthorized – Invalid API Key"}), 401

    # Only allow from your Chrome extension
    if origin and not origin.startswith(f"chrome-extension://{EXTENSION_ID}"):
        return jsonify({"error": "Forbidden origin"}), 403

@app.route("/")
def home():
    return "Sustainability API is running."

@app.route("/brand", methods=["GET"])
def get_brand_info():
    brand = request.args.get("name", "").lower().strip()
    if not brand:
        return jsonify({"error": "Missing brand name"}), 400

    # Try cache
    if brand in brand_cache:
        slug = brand_cache[brand]
        url = f"https://directory.goodonyou.eco/brand/{slug}"
        try:
            data = scrape_brand_page(url)
            data.update({"brand": brand, "source": url})
            return jsonify(data)
        except:
            pass

    # Try slug fallback
    slug = re.sub(r'[^a-z0-9]+', "-", brand).strip("-")
    url = f"https://directory.goodonyou.eco/brand/{slug}"

    try:
        data = scrape_brand_page(url)
        brand_cache[brand] = slug
        with open(CACHE_FILE, "w") as f:
            json.dump(brand_cache, f, indent=2)
        data.update({"brand": brand, "source": url})
        return jsonify(data)
    except Exception as e:
        return jsonify({
            "error": "Could not retrieve brand info",
            "details": str(e),
            "attempted_url": url
        }), 404

web.run(app)
