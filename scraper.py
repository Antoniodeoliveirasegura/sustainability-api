import requests
from bs4 import BeautifulSoup

def scrape_brand_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    # Brand rating
    rating_section = soup.find("p", id="brand-rating")
    rating = rating_section.get_text(strip=True).replace("Rated:", "").strip() if rating_section else "Rating not found"

    # Price level
    price_box = soup.select_one("div.PriceRating__InlineBox-sc-cbcbni-0")
    price = price_box.get_text(strip=True) if price_box else "Price not found"

    # Location
    location_tag = rating_section.find_next("p") if rating_section else None
    location = location_tag.get_text(strip=True).replace("location:", "").strip() if location_tag else "Location not found"

    return {
        "rating": rating,
        "price": price,
        "location": location
    }
