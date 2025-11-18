# Quiz 1: Basic HTML Parsing
# TODO: Complete this file to extract information from index.html

from bs4 import BeautifulSoup

def parse_html():
    """
    Parse index.html and extract post information.

    Returns:
        dict: Dictionary containing titles, authors, dates, and total posts
    """
    # TODO: Read the index.html file
    # TODO: Create BeautifulSoup object
    # TODO: Extract all post titles (h2 tags within articles)
    # TODO: Extract author names (p with class="author")
    # TODO: Extract post dates (p with class="date")
    # TODO: Count total posts (article with class="post")

    # Return a dictionary with the extracted information
    return {
        'titles': [],
        'authors': [],
        'dates': [],
        'total_posts': 0
    }

def print_results(data):
    """
    Print the extracted data in the required format.

    Args:
        data (dict): Dictionary containing extracted information
    """
    # TODO: Print the results in the format shown in INSTRUCTION.md
    pass

def main():
    """Main function to execute the HTML parsing."""
    # TODO: Call parse_html() and print_results()
    pass

if __name__ == "__main__":
    main()
