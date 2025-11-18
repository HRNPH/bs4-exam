# Quiz 1: Basic HTML Parsing with Beautiful Soup

## Objective
Practice basic HTML parsing using Beautiful Soup library.

## Task
Complete the `main.py` file to extract information from `index.html`. Your program should:

1. **Extract all post titles** (5 points)
   - Get the text content of all `<h2>` tags within articles
   - Print each title on a new line

2. **Extract author names** (5 points)
   - Get the text content of all `<p class="author">` tags
   - Print each author name on a new line

3. **Extract post dates** (5 points)
   - Get the text content of all `<p class="date">` tags
   - Print each date on a new line

4. **Count total posts** (5 points)
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
- Use Beautiful Soup library (bs4)
- Your solution should work with the provided index.html file
- Make sure to handle proper encoding and file reading
- Follow the exact output format shown above

## Testing
Run `python grader.py` to check your solution and see your score.
