# Quiz 3: Navigation and Sibling Traversal with Beautiful Soup

## Objective
Practice navigating the DOM tree and using Beautiful Soup's navigation methods and sibling traversal.

## Task
Complete the `main.py` file to extract information using navigation methods by first fetching HTML content from the live URL, then processing the data. Your program should:

1. **Fetch HTML from live URL** (5 points)
   - Use the `requests` library to fetch HTML content from https://hrnph.dev/bs4-exam/exam-3
   - Implement proper error handling for network requests
   - Handle HTTP status codes and connection errors
   - Return the HTML content for parsing

2. **Find sibling elements** (5 points)
   - Find all `<li>` elements in the navigation menu
   - Extract the text of the next sibling after each navigation link
   - Print navigation links with their positions

3. **Extract parent and child relationships** (5 points)
   - Find all article summaries and get their parent article items
   - Extract the title (h4) from each parent article item
   - Print titles with their corresponding summary authors

4. **Use find_next() and find_previous()** (5 points)
   - Starting from the featured article title, find the next element with class "article-meta"
   - Starting from the weather widget, find the previous h3 element
   - Print the results of these navigation operations

5. **Extract text from complex nested structures** (5 points)
   - Navigate from trending items to extract: number, title link, and time
   - Get parent section titles for different sidebar sections
   - Print structured information from nested elements

## Expected Output Format
```
Navigation Menu Siblings:
Home (Position: 1)
Politics (Position: 2) 
Sports (Position: 3)
Technology (Position: 4)
Business (Position: 5)

Article Items with Authors:
Sports: Championship Finals This Weekend - Author: Mike Thompson
Politics: New Policy Reform Announced - Author: Emily Davis
Business: Stock Market Reaches New Heights - Author: Robert Chen

Navigation Results:
From featured article title to meta: Sarah Johnson 10:30 AM Technology
From weather widget to previous heading: Weather Update

Trending Items with Context:
1. Breaking: Major Tech Announcement - 2 hours ago (Section: Trending Topics)
2. Sports Championship Results - 4 hours ago (Section: Trending Topics)
3. Political Debate Tonight - 6 hours ago (Section: Trending Topics)
```

## Requirements
- Use the `requests` library to fetch HTML content from the live URL
- Implement proper error handling for network requests (HTTP errors, connection issues)
- Use Beautiful Soup navigation methods:
  - `find_next()`, `find_previous()`
  - `find_next_sibling()`, `find_previous_sibling()`
  - `parent`, `children`
  - `find_parent()`, `find_parents()`
- Demonstrate understanding of DOM traversal
- Handle both upward and downward navigation
- Follow the exact output format shown above

## Testing
Run `python grader.py` to check your solution and see your score.