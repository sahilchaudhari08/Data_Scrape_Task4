from bs4 import BeautifulSoup

# Load the HTML content from the file
with open("Flipkart.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup

soup = BeautifulSoup(html_content, "html.parser")

# Find all laptop containers
laptop_containers = soup.find_all("div", class_="tUxRFH")

for container in laptop_containers:
    # Extract laptop name
    name = container.find("div", class_="KzDlHZ")
    laptop_name = name.text.strip() if name else "N/A"

    # Extract laptop features
    features = container.find("ul", class_="G4BRas")
    laptop_features = [li.text.strip() for li in features.find_all("li")] if features else []

    # Extract original price 
    original_price = container.select_one("div.BfVC2z > div.cN1yYO div._4b5DiR")
    laptop_original_price = original_price.text.strip() if original_price else "N/A"

    # Extract discounted price
    discounted_price = container.select_one("div.BfVC2z > div.cN1yYO div.ZYYwLA")
    laptop_discounted_price = discounted_price.text.strip() if discounted_price else "N/A"

    # Extract discount percentage
    discount = container.select_one("div.BfVC2z > div.cN1yYO div.UkUFwK")
    laptop_discount = discount.text.strip() if discount else "N/A"

    # Extract ratings
    ratings = container.find("div", class_="XQDdHH")
    laptop_ratings = ratings.text.strip() if ratings else "N/A"

    # Extract reviews
    reviews = container.find("span", class_="Wphh3N")
    laptop_reviews = reviews.text.strip() if reviews else "N/A"

    # Extract bank offers
    bank_offers = container.select_one("div.M4DNwV > div.n5vj9c > div.yiggsN.O5Fpg8")
    laptop_bank_offers = bank_offers.text.strip() if bank_offers else "N/A"

    # Extract laptop image URL
    image = container.find("img", class_="DByuf4")
    laptop_image = image["src"] if image else "N/A"

    # Append the extracted data to the laptops list
    
    print("Name:",laptop_name)
    print("Original Price:",laptop_original_price)  
    print("Discounted Price:",laptop_discounted_price)
    print("Discount:",laptop_discount)
    print("\nFeatures:",laptop_features)
    print("Ratings:",laptop_ratings)
    print("Reviews:",laptop_reviews)
    print("\nBank Offers:",laptop_bank_offers)
    print("Image URL:",laptop_image)
    print("-" * 80)
