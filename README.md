# Beautiful Soup Exam

A comprehensive 4-quiz examination covering Beautiful Soup web scraping techniques, from basic HTML parsing to advanced real-world scenarios.

## Structure

```
bs4-exam/
├── quiz-1/          # Basic HTML Parsing
├── quiz-2/          # Advanced CSS Selectors  
├── quiz-3/          # Navigation and Sibling Traversal
├── quiz-4/          # Advanced Techniques and Real-World Scenarios
└── README.md
```

Each quiz folder contains:
- `index.html` - Sample HTML document to scrape
- `INSTRUCTION.md` - Detailed instructions and requirements
- `main.py` - Boilerplate code for students to complete
- `grader.py` - Automated grading and feedback system

## Quiz Overview

### Quiz 1: Basic HTML Parsing (20 points)
- Extract text from specific HTML tags
- Handle class-based selection
- Count elements
- Basic Beautiful Soup operations

**Skills:** Basic tag selection, text extraction, element counting

### Quiz 2: Advanced CSS Selectors (20 points)
- Use complex CSS selectors
- Extract data attributes
- Handle multiple class elements
- Advanced selection techniques

**Skills:** CSS selectors, attribute extraction, complex queries

### Quiz 3: Navigation and Sibling Traversal (20 points)
- Navigate DOM tree structure
- Use find_next(), find_previous()
- Handle parent-child relationships
- Sibling element traversal

**Skills:** DOM navigation, tree traversal, element relationships

### Quiz 4: Advanced Techniques and Real-World Scenarios (20 points)
- Use regular expressions with Beautiful Soup
- Process and validate extracted data
- Calculate statistics
- Handle edge cases and missing data

**Skills:** Regex, data processing, validation, error handling

## How to Use

### For Students

1. Navigate to any quiz folder (e.g., `cd quiz-1`)
2. Read the `INSTRUCTION.md` file to understand requirements
3. Complete the `main.py` file by implementing the TODO sections
4. Test your solution by running: `python grader.py`
5. Review feedback and improve your solution

### For Instructors

1. Each quiz is self-contained and can be used independently
2. Graders provide detailed feedback and scoring
3. Progressively builds skills from basic to advanced
4. Real-world HTML scenarios prepare students for actual web scraping

## Prerequisites

Students should have:
- Basic Python knowledge
- Understanding of HTML structure
- Beautiful Soup library installed: `pip install beautifulsoup4`
- (Quiz 4) Basic regular expressions knowledge

## Installation

```bash
# Install Beautiful Soup
pip install beautifulsoup4

# Install lxml parser (recommended)
pip install lxml
```

## Grading System

Each quiz is worth 20 points with automated grading that checks:
- ✅ Correct output format
- ✅ Required content presence
- ✅ Technical implementation quality
- ✅ Code best practices

Graders provide:
- Detailed score breakdown
- Specific feedback on missing elements
- Encouragement based on performance level
- Suggestions for improvement

## Learning Progression

1. **Quiz 1** builds foundational skills
2. **Quiz 2** introduces advanced selection techniques  
3. **Quiz 3** teaches DOM navigation concepts
4. **Quiz 4** combines all skills with real-world complexity

This progression ensures students master Beautiful Soup systematically and are prepared for actual web scraping projects.

## Tips for Students

1. **Start with Quiz 1** - Don't skip the basics
2. **Read instructions carefully** - Output format matters
3. **Test frequently** - Run the grader often to check progress
4. **Study the HTML** - Understand the structure before coding
5. **Use Beautiful Soup documentation** - It's your best reference

Good luck and happy scraping! 🕷️