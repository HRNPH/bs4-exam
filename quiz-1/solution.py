# Quiz 1: Basic HTML Parsing - SOLUTION
import requests
from bs4 import BeautifulSoup


def fetch_html():
    """
    Fetch HTML content from the live URL.

    Returns:
        str: HTML content from the URL
    """
    url = "https://hrnph.dev/bs4-exam/exam-1"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching HTML: {e}")
        return None


def parse_html(html_content):
    """
    Parse HTML content and extract post information.

    Args:
        html_content (str): HTML content to parse

    Returns:
        dict: Dictionary containing titles, authors, dates, and total posts
    """
    # Use the provided HTML content
    content = html_content

    # Create BeautifulSoup object
    soup = BeautifulSoup(content, "html.parser")

    # Extract all post titles (h2 tags within articles)
    titles = [h2.get_text(strip=True) for h2 in soup.select("article.post h2")]

    # Extract author names (p with class="author")
    authors = [
        p.get_text(strip=True).replace("By ", "") for p in soup.select("p.author")
    ]

    # Extract post dates (p with class="date")
    dates = [p.get_text(strip=True) for p in soup.select("p.date")]

    # Count total posts (article with class="post")
    total_posts = len(soup.select("article.post"))

    # Return a dictionary with the extracted information
    return {
        "titles": titles,
        "authors": authors,
        "dates": dates,
        "total_posts": total_posts,
    }


def print_results(data):
    """
    Print the extracted data in the required format.

    Args:
        data (dict): Dictionary containing extracted information
    """
    print("Post Titles:")
    for title in data["titles"]:
        print(title)

    print("\nAuthors:")
    for author in data["authors"]:
        print(author)

    print("\nDates:")
    for date in data["dates"]:
        print(date)

    print(f"\nTotal Posts: {data['total_posts']}")


def main():
    """Main function to execute the HTML parsing."""
    # Fetch HTML content first
    html_content = fetch_html()
    if html_content is None:
        print("Failed to fetch HTML content. Exiting.")
        return

    # Call parse_html() with the fetched HTML content and print_results()
    data = parse_html(html_content)
    print_results(data)


if __name__ == "__main__":
    main()
