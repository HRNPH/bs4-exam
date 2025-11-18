# Quiz 2: Advanced CSS Selectors
# TODO: Complete this file to extract information using CSS selectors

from bs4 import BeautifulSoup


def extract_with_css_selectors():
    """
    Extract information from index.html using CSS selectors.

    Returns:
        dict: Dictionary containing all extracted information
    """
    # TODO: Read the index.html file
    # TODO: Create BeautifulSoup object

    # TODO: Extract product titles using class selector
    # TODO: Extract current prices using class selector

    # TODO: Find high-rated products (4.5+) using data attributes

    # TODO: Extract data attributes (data-category, data-price)

    # TODO: Find elements with multiple classes
    # TODO: Extract button text from .btn.btn-primary
    # TODO: Extract featured product information

    return {
        "product_titles": [],
        "current_prices": [],
        "high_rated_products": [],
        "product_data": [],
        "multiple_class_elements": {"buttons": [], "featured_products": []},
    }


def print_results(data):
    """
    Print the extracted data in the required format.

    Args:
        data (dict): Dictionary containing extracted information
    """
    # TODO: Print all results in the format shown in INSTRUCTION.md
    pass


def main():
    """Main function to execute the CSS selector extraction."""
    # TODO: Call extract_with_css_selectors() and print_results()
    pass


if __name__ == "__main__":
    main()
