# Quiz 1: Basic HTML Parsing - SOLUTION
from bs4 import BeautifulSoup


def parse_html():
    """
    Parse index.html and extract post information.

    Returns:
        dict: Dictionary containing titles, authors, dates, and total posts
    """
    # Read the index.html file
    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()

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
    # Call parse_html() and print_results()
    data = parse_html()
    print_results(data)


if __name__ == "__main__":
    main()
