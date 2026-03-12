# Tools

This section contains useful tools and utilities to enhance your Marathi learning experience. These Python scripts are designed to help you practice, test, and reinforce your Marathi language skills.

## Available Tools

### 1. Transliteration Tool
**Location:** `transliteration-tool/script.py`

Convert English text (Latin script) to Devanagari script. This tool helps learners who are more comfortable with English script to write Marathi.

**Features:**
- English to Devanagari transliteration
- Support for common Marathi words and phrases
- Handles special characters and combinations

### 2. Flashcard Generator
**Location:** `flashcard-generator/generator.py`

Generate customizable flashcards for vocabulary practice. Create your own flashcard sets from word lists.

**Features:**
- Create flashcards from CSV or JSON input
- Support for bidirectional learning (Marathi ↔ English)
- Export to various formats (text, JSON, Anki-compatible)

### 3. Quiz Maker
**Location:** `quiz-maker/quiz-generator.py`

Generate interactive quizzes to test your Marathi knowledge. Perfect for self-assessment and practice.

**Features:**
- Multiple question types (multiple choice, fill-in-blank, translation)
- Customizable difficulty levels
- Randomized question selection
- Score tracking

## Requirements

All tools require Python 3.6 or higher. Some tools may have additional dependencies:

```bash
# Optional: For enhanced transliteration
pip install indic-transliteration

# Optional: For flashcard export features
pip install genanki

# Optional: For rich terminal output
pip install rich
```

## Quick Start

Each tool can be run independently:

```bash
# Run transliteration tool
python transliteration-tool/script.py

# Run flashcard generator
python flashcard-generator/generator.py

# Run quiz maker
python quiz-maker/quiz-generator.py
```

## Contributing

Feel free to improve these tools or add new ones! See the main [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## Tool Ideas

Planning to add more tools? Here are some suggestions:

- **Pronunciation Checker** - Compare your pronunciation with native speaker audio
- **Grammar Checker** - Basic Marathi grammar validation
- **Word Frequency Analyzer** - Analyze text for vocabulary learning priorities
- **Conversation Simulator** - Practice dialogues with AI responses
- **Script Converter** - Convert between Devanagari and Modi scripts
