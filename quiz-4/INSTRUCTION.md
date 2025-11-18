# Quiz 4: Advanced Techniques and Real-World Scenarios

## Objective
Practice advanced Beautiful Soup techniques including regex, data processing, and real-world extraction scenarios.

## Task
Complete the `main.py` file to perform complex data extraction and analysis by first fetching HTML content from the live URL, then processing the data. Your program should:

1. **Fetch HTML from live URL** (5 points)
   - Use the `requests` library to fetch HTML content from https://hrnph.dev/bs4-exam/exam-4
   - Implement proper error handling for network requests
   - Handle HTTP status codes and connection errors
   - Return the HTML content for parsing

2. **Extract and process recipe data** (5 points)
   - Extract all recipe information including name, difficulty, prep time, servings, calories
   - Parse numerical values from text (e.g., extract numbers from "20 mins", "320 cal")
   - Store structured data in a list of dictionaries

3. **Use regular expressions for text processing** (5 points)
   - Extract numeric values from prep time, calorie count, and serving size
   - Parse rating numbers from rating text (e.g., extract 4.7 from "4.7/5.0 - 156 reviews")
   - Handle various text formats and extract consistent data

4. **Calculate statistics and summaries** (5 points)
   - Calculate average prep time across all recipes
   - Find the recipe with highest and lowest calorie count
   - Count recipes by difficulty level
   - Calculate average rating from all recipes

5. **Handle missing data and edge cases** (5 points)
   - Check for missing attributes or elements
   - Provide default values for missing data
   - Handle different data formats gracefully
   - Validate extracted data before using it

## Expected Output Format
```
Recipe Data Extraction:
1. Fluffy Pancakes (Easy) - 20 mins, 4 servings, 320 cal, Rating: 4.7
2. Grilled Salmon with Herbs (Medium) - 35 mins, 2 servings, 450 cal, Rating: 4.9
3. Chocolate Lava Cake (Hard) - 45 mins, 4 servings, 580 cal, Rating: 4.8

Statistics:
- Average prep time: 33.3 minutes
- Highest calories: Chocolate Lava Cake (580 cal)
- Lowest calories: Fluffy Pancakes (320 cal)
- Average rating: 4.8/5.0
- Recipes by difficulty: Easy: 1, Medium: 1, Hard: 1

Data Validation:
- All recipes have required fields: ✓
- Numeric data successfully extracted: ✓
- Ratings within valid range: ✓
- No missing critical data: ✓
```

## Requirements
- Use the `requests` library to fetch HTML content from the live URL
- Implement proper error handling for network requests (HTTP errors, connection issues)
- Use regular expressions (`re` module) for text processing
- Handle different text formats and edge cases
- Perform data validation and error checking
- Calculate meaningful statistics from extracted data
- Use proper data structures (lists, dictionaries) to organize information
- Handle missing or malformed data gracefully

## Testing
Run `python grader.py` to check your solution and see your score.