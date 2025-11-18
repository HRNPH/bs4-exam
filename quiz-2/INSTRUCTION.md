# Quiz 2: Advanced CSS Selectors with Beautiful Soup

## Objective
Practice advanced CSS selectors and attribute extraction using Beautiful Soup and web fetching.

## Task
Complete the `main.py` file to fetch HTML from the live website and extract specific information. Your program should:

1. **Fetch HTML from remote URL** (4 points)
   - Use `requests` library to fetch HTML from: `https://hrnph.dev/bs4-exam/exam-2`
   - Handle potential network errors gracefully
   - Parse the fetched HTML content

2. **Extract all product titles** (4 points)
   - Get text from all elements with class `product-title`
   - Print each title on a new line

3. **Extract current prices** (4 points)
   - Get text from all elements with class `price-current`
   - Print each price on a new line

4. **Find products with rating 4.5 or higher** (4 points)
   - Check `data-rating` attribute on elements with class `product-rating`
   - Print the corresponding product titles for high-rated products

5. **Extract data attributes** (4 points)
   - Get `data-category` and `data-price` attributes from all product cards
   - Print category and price for each product

6. **Find elements with multiple classes** (4 points)
   - Extract text from elements that have both `btn` and `btn-primary` classes
   - Extract text from elements with class `featured`

## Expected Output Format
```
Product Titles:
Gaming Laptop Pro
SmartPhone X
Tablet Pro 12
UltraBook Elite

Current Prices:
$999.99
$699.99
$349.99
$1499.99

High Rated Products (4.5+):
Gaming Laptop Pro
SmartPhone X
UltraBook Elite

Product Data:
Gaming Laptop Pro - Category: laptops, Price: 999
SmartPhone X - Category: phones, Price: 699
Tablet Pro 12 - Category: tablets, Price: 349
UltraBook Elite - Category: laptops, Price: 1499

Elements with Multiple Classes:
Button texts: Add to Cart, Add to Cart, Add to Cart, Add to Cart
Featured product: UltraBook Elite
```

## Requirements
- Use Beautiful Soup with CSS selectors (`select()` method)
- Use `requests` library for web fetching from: `https://hrnph.dev/bs4-exam/exam-2`
- Handle HTTP errors (404, timeout, connection errors)
- Use various CSS selector techniques:
  - Class selectors (`.classname`)
  - Attribute selectors (`[attribute]`)
  - Attribute value selectors (`[attribute="value"]`)
  - Multiple class selectors (`.class1.class2`)
- Handle data attributes properly
- Follow the exact output format shown above
- Add error handling for network issues

## Installation
Install required packages:
```bash
pip install beautifulsoup4 requests
```

## Testing
Run `python grader.py` to check your solution and see your score.