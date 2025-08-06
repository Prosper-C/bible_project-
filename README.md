# Bible Project 📖

A simple Python project for searching and interacting with Bible data.
# Bible Search CLI App

This is a command-line Bible search application written in Python. It allows users to search for words in a sample King James Version (KJV) Bible JSON file and returns matching verses.

## Features
- Search for any word in the Bible
- Returns book, chapter, verse, and content
- Simple and easy to use from the terminal

## Project Structure
```
bible_project/
├── app/
│   └── search.py
├── bible_data/
│   └── kjv_sample.json
├── tests/
│   └── test_search.py
├── .venv/
└── README.md
```

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Prosper-C/bible_project.git
cd bible_project
```

### 2. Create and activate a virtual environment
**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```
**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install pytest
```

### 4. Run the application
```bash
python app/search.py
```

### 5. Run tests
```bash
pytest tests/
```

## Author
Prosper C

## License
This project is open source and available under the [MIT License](LICENSE).
