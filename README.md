# Beautiful Soup Exam

A comprehensive 4-quiz examination covering Beautiful Soup web scraping techniques, from basic HTML parsing to advanced real-world scenarios.

## 🌐 Live Demo

This exam is deployed on GitHub Pages at: [hrnph.dev/bs4-exam](https://hrnph.dev/bs4-exam)

- **Main Page**: [hrnph.dev/bs4-exam](https://hrnph.dev/bs4-exam)
- **Quiz 1**: [hrnph.dev/bs4-exam/exam-1](https://hrnph.dev/bs4-exam/exam-1)
- **Quiz 2**: [hrnph.dev/bs4-exam/exam-2](https://hrnph.dev/bs4-exam/exam-2)
- **Quiz 3**: [hrnph.dev/bs4-exam/exam-3](https://hrnph.dev/bs4-exam/exam-3)
- **Quiz 4**: [hrnph.dev/bs4-exam/exam-4](https://hrnph.dev/bs4-exam/exam-4)

## Structure

```
bs4-exam/
├── quiz-1/          # Basic HTML Parsing
├── quiz-2/          # Advanced CSS Selectors  
├── quiz-3/          # Navigation and Sibling Traversal
├── quiz-4/          # Advanced Techniques and Real-World Scenarios
├── exam-1/          # HTML files for GitHub Pages deployment
├── exam-2/          
├── exam-3/          
├── exam-4/          
├── .github/workflows/  # GitHub Actions deployment
├── index.html       # Main landing page
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

## 🚀 GitHub Pages Deployment

This project is automatically deployed to GitHub Pages using GitHub Actions.

### Setup Instructions

1. **Fork or create this repository** on GitHub
2. **Enable GitHub Pages** in repository settings:
   - Go to Settings → Pages
   - Source: Deploy from a branch
   - Branch: main, folder: /root
3. **Push to main branch** - the workflow will automatically deploy
4. **Access your site** at `https://your-username.github.io/bs4-exam`

### Automatic Deployment Process

- The `.github/workflows/deploy.yml` workflow triggers on push to main
- HTML files are copied from `quiz-*/` to `exam-*/` directories
- Site is automatically deployed to GitHub Pages
- Accessible at your configured custom domain or GitHub Pages URL

### Custom Domain Setup

If you want to use a custom domain (like `hrnph.dev`):

1. **Add DNS records** pointing to GitHub Pages servers
2. **Create CNAME file** in root: `hrnph.dev`
3. **Update repository settings** with custom domain
4. **Configure HTTPS** in repository settings

### Manual Deployment (Alternative)

If you prefer manual deployment:

1. **Copy HTML files**:
   ```bash
   mkdir -p exam-1 exam-2 exam-3 exam-4
   cp quiz-1/index.html exam-1/
   cp quiz-2/index.html exam-2/
   cp quiz-3/index.html exam-3/
   cp quiz-4/index.html exam-4/
   ```

2. **Enable GitHub Pages** in repository settings
3. **Select main branch as source** in Pages settings

Good luck and happy scraping! 🕷️