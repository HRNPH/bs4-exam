# Quiz 3: Navigation and Sibling Traversal - SOLUTION
import requests
from bs4 import BeautifulSoup


def fetch_html():
    """
    Fetch HTML content from the live URL.

    Returns:
        str: HTML content from the URL
    """
    url = "https://hrnph.dev/bs4-exam/exam-3"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching HTML: {e}")
        return None


def navigate_dom_tree(html_content):
    """
    Extract information from HTML content using DOM navigation methods.

    Args:
        html_content (str): HTML content to parse

    Returns:
        dict: Dictionary containing all extracted information using navigation
    """
    # Use the provided HTML content
    content = html_content

    # Create BeautifulSoup object
    soup = BeautifulSoup(content, "html.parser")

    # Find navigation menu siblings
    navigation_siblings = []
    nav_links = soup.select(".nav-list a")
    for i, link in enumerate(nav_links, 1):
        link_text = link.get_text(strip=True)
        navigation_siblings.append(f"{link_text} (Position: {i})")

    # Extract parent-child relationships
    article_authors = []
    article_items = soup.select(".article-item")
    for item in article_items:
        title_elem = item.select_one("h4 a")
        author_elem = item.select_one(".article-summary .author")
        if title_elem and author_elem:
            title = title_elem.get_text(strip=True)
            author = author_elem.get_text(strip=True)
            article_authors.append(f"{title} - Author: {author}")

    # Use find_next() and find_previous() navigation
    navigation_results = {}

    # From featured article title to meta
    featured_title = soup.select_one(".featured-article h2")
    if featured_title:
        meta_elem = featured_title.find_next(class_="article-meta")
        if meta_elem:
            meta_text = meta_elem.get_text(" ", strip=True)
            navigation_results["featured_to_meta"] = (
                f"From featured article title to meta: {meta_text}"
            )

    # From weather widget to previous heading
    weather_widget = soup.select_one(".weather-widget")
    if weather_widget:
        prev_heading = weather_widget.find_previous("h3")
        if prev_heading:
            navigation_results["weather_to_heading"] = (
                f"From weather widget to previous heading: {prev_heading.get_text(strip=True)}"
            )

    # Extract nested structure information
    trending_context = []
    trending_items = soup.select(".trending-item")
    trending_section = soup.select_one(".sidebar-section h3")
    section_title = (
        trending_section.get_text(strip=True) if trending_section else "Trending Topics"
    )

    for item in trending_items:
        number = item.select_one(".trending-number").get_text(strip=True)
        link = item.select_one("a").get_text(strip=True)
        time = item.select_one(".trending-time").get_text(strip=True)
        trending_context.append(f"{number}. {link} - {time} (Section: {section_title})")

    return {
        "navigation_siblings": navigation_siblings,
        "article_authors": article_authors,
        "navigation_results": navigation_results,
        "trending_context": trending_context,
    }


def print_results(data):
    """
    Print the extracted data in the required format.

    Args:
        data (dict): Dictionary containing extracted information
    """
    print("Navigation Menu Siblings:")
    for item in data["navigation_siblings"]:
        print(item)

    print("\nArticle Items with Authors:")
    for item in data["article_authors"]:
        print(item)

    print("\nNavigation Results:")
    for key, value in data["navigation_results"].items():
        print(value)

    print("\nTrending Items with Context:")
    for item in data["trending_context"]:
        print(item)


def main():
    """Main function to execute the DOM navigation extraction."""
    # Fetch HTML content first
    html_content = fetch_html()
    if html_content is None:
        print("Failed to fetch HTML content. Exiting.")
        return

    # Call navigate_dom_tree() with the fetched HTML content and print_results()
    data = navigate_dom_tree(html_content)
    print_results(data)


if __name__ == "__main__":
    main()
