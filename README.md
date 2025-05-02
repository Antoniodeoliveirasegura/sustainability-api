# 🌱 Sustainability API

A lightweight Flask API that fetches sustainability ratings for fashion brands by scraping data from [Good On You](https://directory.goodonyou.eco).  
It powers the [Sustainability Chrome Extension](https://github.com/Antoniodeoliveirasegura/sustainabilityExtension) by providing real-time brand insights such as rating, location, and price category.

---

## ⚙️ Features

- 🔍 Automatically slugifies and scrapes brand pages (e.g., `/brand?name=zara`)
- ⚡ Fast lookup via local brand cache (`brand_cache.json`)
- 🔐 Secured with `X-API-Key` header and Chrome extension origin checks
- 🌍 Hosted on Render.com

---

## 🚀 Example Usage

```
GET /brand?name=zara
Headers: X-API-Key: your-api-key
```

Response:

```json
{
  "brand": "zara",
  "location": "Spain",
  "price": "$$$$",
  "rating": "It's a start",
  "source": "https://directory.goodonyou.eco/brand/zara"
}
```

---

## 🔧 Setup Instructions

1. Clone the repo

```bash
git clone https://github.com/your-username/sustainability-api.git
cd sustainability-api
```

2. Create a `.env` file

```env
API_KEY=your-api-key
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the API

```bash
python main.py
```

---

## 🛰️ Deploying to Render.com

1. Connect the repo to your Render account
2. Set the build command: `pip install -r requirements.txt`
3. Set the start command: `python main.py`
4. Add the environment variable: `API_KEY=your-api-key`

---

## 🔐 Security Notes

- Requires a valid `X-API-Key` header
- Rejects requests that don't match the expected Chrome Extension origin
- Brand slugs are cached after successful fetches to improve speed

---

## 📁 Project Structure

```
main.py            # Flask API
scraper.py         # HTML parsing and logic
brand_cache.json   # Local brand-to-slug cache
requirements.txt   # Python dependencies
.env (not tracked) # Stores API_KEY securely
```

---

## 📄 License

MIT License – use freely with attribution.
