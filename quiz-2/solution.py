# Quiz 2: Advanced CSS Selectors - SOLUTION
from bs4 import BeautifulSoup


def extract_with_css_selectors():
    """
    Extract information from index.html using CSS selectors.

    Returns:
        dict: Dictionary containing all extracted information
    """
    # Read the index.html file
    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()

    # Create BeautifulSoup object
    soup = BeautifulSoup(content, "html.parser")

    # Extract product titles using class selector
    product_titles = [
        title.get_text(strip=True) for title in soup.select(".product-title")
    ]

    # Extract current prices using class selector
    current_prices = [
        price.get_text(strip=True) for price in soup.select(".price-current")
    ]

    # Find high-rated products (4.5+) using data attributes
    high_rated_products = []
    products = soup.select(".product-card")
    for product in products:
        rating_elem = product.select_one(".product-rating")
        if rating_elem and rating_elem.get("data-rating"):
            try:
                rating = float(rating_elem.get("data-rating"))
                if rating >= 4.5:
                    title = product.select_one(".product-title")
                    if title:
                        high_rated_products.append(title.get_text(strip=True))
            except ValueError:
                continue

    # Extract data attributes (data-category, data-price)
    product_data = []
    for product in products:
        title = product.select_one(".product-title")
        category = product.get("data-category", "")
        price = product.get("data-price", "")
        if title:
            product_data.append(
                {
                    "title": title.get_text(strip=True),
                    "category": category,
                    "price": price,
                }
            )

    # Find elements with multiple classes
    # Extract button text from .btn.btn-primary
    buttons = [btn.get_text(strip=True) for btn in soup.select(".btn.btn-primary")]

    # Extract featured product information
    featured_products = [
        fp.get_text(strip=True)
        for fp in soup.select(".product-card.featured .product-title")
    ]

    return {
        "product_titles": product_titles,
        "current_prices": current_prices,
        "high_rated_products": high_rated_products,
        "product_data": product_data,
        "multiple_class_elements": {
            "buttons": buttons,
            "featured_products": featured_products,
        },
    }


def print_results(data):
    """
    Print the extracted data in the required format.

    Args:
        data (dict): Dictionary containing extracted information
    """
    print("Product Titles:")
    for title in data["product_titles"]:
        print(title)

    print("\nCurrent Prices:")
    for price in data["current_prices"]:
        print(price)

    print("\nHigh Rated Products (4.5+):")
    for product in data["high_rated_products"]:
        print(product)

    print("\nProduct Data:")
    for item in data["product_data"]:
        print(f"{item['title']} - Category: {item['category']}, Price: {item['price']}")

    print("\nElements with Multiple Classes:")
    buttons_text = ", ".join(data["multiple_class_elements"]["buttons"])
    print(f"Button texts: {buttons_text}")

    featured_products = data["multiple_class_elements"]["featured_products"]
    if featured_products:
        print(f"Featured product: {featured_products[0]}")


def main():
    """Main function to execute the CSS selector extraction."""
    # Call extract_with_css_selectors() and print_results()
    data = extract_with_css_selectors()
    print_results(data)


if __name__ == "__main__":
    main()
