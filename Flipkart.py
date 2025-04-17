import requests
from bs4 import BeautifulSoup

# Open your saved Flipkart HTML file
with open("flipkart.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find all product containers
product_cards = soup.find_all("div", class_="tUxRFH")

for card in product_cards:
    try:
        # Laptop Name
        name = card.find("div", class_="KzDlHZ").get_text(strip=True)

        # Discounted Price
        discounted_price = card.find("div", class_="Nx9bqj _4b5DiR").get_text(strip=True)

        # Original Price
        original_price_tag = card.find("div", class_="yRaY8j")
        original_price = original_price_tag.get_text(strip=True) if original_price_tag else "N/A"

        # Discount Percentage
        discount_percent_tag = card.find("div", class_="UkUFwK")
        discount_percent = discount_percent_tag.get_text(strip=True) if discount_percent_tag else "N/A"

        # Rating
        rating_tag = card.find("div", class_="XQDdHH")
        rating = rating_tag.get_text(strip=True) if rating_tag else "N/A"

        # Number of reviews & ratings
        reviews_tag = card.find("span", class_="Wphh3N")
        reviews = reviews_tag.get_text(strip=True) if reviews_tag else "N/A"

        # Highlights / product info
        highlights_ul = card.find("ul")  # Removed class filter to find any <ul> tag
        if highlights_ul:
            highlights = [li.get_text(strip=True) for li in highlights_ul.find_all("li")]
            product_info = "; ".join(highlights)
        else:
            product_info = "N/A"

        # Image URL
        image_tag = card.find("img", class_="DByuf4")
        image_url = image_tag["src"] if image_tag else "N/A"

        # Bank Offer
        bank_offer_tag = card.find("li", class_="KzDlHZ Jx6MS8")  # Update class name if incorrect
        bank_offer = bank_offer_tag.get_text(strip=True) if bank_offer_tag else "No bank offer available"

        # Output all fields
        print("Laptop Name:", name)
        print("Discounted Price:", discounted_price)
        print("Original Price:", original_price)
        print("Discount Percentage:", discount_percent)
        print("Rating:", rating)
        print("Number of Reviews:", reviews)
        print("Product Info:", product_info)
        print("Image URL:", image_url)
        print("Bank Offer:", bank_offer)
        print("-" * 80)

    except Exception as e:
        print("Error parsing a product:", e)
