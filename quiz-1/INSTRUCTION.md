# Quiz 1: Basic HTML Parsing with Beautiful Soup

## Objective
Practice basic HTML parsing using Beautiful Soup library and web fetching.

## Task
Complete the `main.py` file to fetch HTML from the live website and extract information. Your program should:

1. **Fetch HTML from remote URL** (5 points)
   - Use `requests` library to fetch HTML from: `https://hrnph.dev/bs4-exam/exam-1`
   - Handle potential network errors gracefully
   - Parse the fetched HTML content

2. **Extract all post titles** (5 points)
   - Get the text content of all `<h2>` tags within articles
   - Print each title on a new line

3. **Extract author names** (5 points)
   - Get the text content of all `<p class="author">` tags
   - Print each author name on a new line

4. **Extract post dates** (5 points)
   - Get the text content of all `<p class="date">` tags
   - Print each date on a new line

5. **Count total posts** (5 points)
   - Count the number of `<article class="post">` elements
   - Print the total count

## Expected Output Format
```
Post Titles:
First Post
Second Post
Third Post

Authors:
John Doe
Jane Smith
Bob Johnson

Dates:
2023-01-15
2023-01-20
2023-02-01

Total Posts: 3
```

## Requirements
- Use Beautiful Soup library (bs4) for parsing
- Use `requests` library for web fetching
- Handle HTTP errors (404, timeout, etc.)
- Your solution should work with the live URL: `https://hrnph.dev/bs4-exam/exam-1`
- Make sure to handle proper encoding and response parsing
- Follow the exact output format shown above
- Add error handling for network issues

## Installation
Install required packages:
```bash
pip install beautifulsoup4 requests
```

## Testing
Run `python grader.py` to check your solution and see your score.
