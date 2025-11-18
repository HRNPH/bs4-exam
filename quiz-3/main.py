# Quiz 3: Navigation and Sibling Traversal
# TODO: Complete this file to extract information using navigation methods

from bs4 import BeautifulSoup


def navigate_dom_tree():
    """
    Extract information from index.html using DOM navigation methods.

    Returns:
        dict: Dictionary containing all extracted information using navigation
    """
    # TODO: Read the index.html file
    # TODO: Create BeautifulSoup object

    # TODO: Find navigation menu siblings
    # TODO: Use find_next_sibling() or similar methods

    # TODO: Extract parent-child relationships
    # TODO: Use parent, find_parent(), children methods

    # TODO: Use find_next() and find_previous() navigation
    # TODO: Start from specific elements and navigate

    # TODO: Extract nested structure information
    # TODO: Navigate complex parent-child relationships

    return {
        "navigation_siblings": [],
        "article_authors": [],
        "navigation_results": {},
        "trending_context": [],
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
    """Main function to execute the DOM navigation extraction."""
    # TODO: Call navigate_dom_tree() and print_results()
    pass


if __name__ == "__main__":
    main()
