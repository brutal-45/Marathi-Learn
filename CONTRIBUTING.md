# Contributing to Learn Marathi | मराठी शिका मध्ये योगदान

Thank you for your interest in contributing to the Learn Marathi project! This document provides guidelines and instructions for contributing.

धन्यवाद! मराठी शिका प्रकल्पात योगदान देण्याच्या तुमच्या रसाबद्दल! हा दस्तावेज योगदानासाठी मार्गदर्शक तत्त्वे आणि सूचना प्रदान करतो.

---

## 📋 Table of Contents | अनुक्रमणिका

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Content Guidelines](#content-guidelines)
- [Style Guide](#style-guide)
- [Pull Request Process](#pull-request-process)
- [Community](#community)

---

## 📜 Code of Conduct | आचार संहिता

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

हा प्रकल्प आणि त्यात सहभागी होणारे प्रत्येकजण आमच्या आचार संहितेद्वारे शासित आहेत. सहभागी होऊन, तुम्ही हा संहिता राखण्याची अपेक्षा आहे.

---

## 🤔 How Can I Contribute? | मी कसे योगदान करू शकतो?

### Reporting Bugs | दोष नोंदवणे

If you find errors in the content, broken links, or any issues with the materials:

1. Check if the issue has already been reported in [Issues](https://github.com/your-username/learn-marathi/issues)
2. If not, create a new issue using the **Bug Report** template
3. Include as much detail as possible:
   - Location of the error (file path)
   - Description of the error
   - Suggested correction (if applicable)

### Suggesting Content | सामग्री सुचवणे

Have ideas for new content?

1. Check existing [Issues](https://github.com/your-username/learn-marathi/issues) and [Discussions](https://github.com/your-username/learn-marathi/discussions)
2. Create a new issue using the **Content Suggestion** template
3. Describe your idea clearly:
   - What topic would you like to add?
   - Why would it be valuable?
   - Any resources or references?

### Contributing Content | सामग्री योगदान

Want to add lessons, vocabulary, exercises, or other content?

1. Fork the repository
2. Create a feature branch
3. Add your content following our [Style Guide](#style-guide)
4. Submit a Pull Request

### Audio Contributions | ऑडिओ योगदान

Native speakers can contribute by:

- Recording pronunciation guides for alphabet
- Recording word pronunciations
- Recording conversation dialogues
- Providing voice-overs for lessons

### Translations | अनुवाद

Help improve our bilingual content:

- Review existing translations for accuracy
- Add transliterations where missing
- Improve English or Marathi explanations

---

## 🚀 Getting Started | सुरुवात करा

### Prerequisites | पूर्वअटी

- A GitHub account
- Basic knowledge of Markdown
- Understanding of Marathi (for content contributions)
- Git installed on your local machine

### Setting Up | सेटअप

1. **Fork the repository**

   Click the "Fork" button at the top right of the repository page.

2. **Clone your fork**

   ```bash
   git clone https://github.com/your-username/learn-marathi.git
   cd learn-marathi
   ```

3. **Create a branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**

   Follow the content guidelines and style guide below.

5. **Commit your changes**

   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

6. **Push to your fork**

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**

   Go to your fork on GitHub and click "Create Pull Request".

---

## 📝 Content Guidelines | सामग्री मार्गदर्शक तत्त्वे

### General Principles | सामान्य तत्त्वे

1. **Bilingual Content**: All content should be in both English and Marathi
2. **Accurate Information**: Verify facts with reliable sources
3. **Progressive Difficulty**: Content should progress from simple to complex
4. **Practical Focus**: Include real-world examples and usage
5. **Cultural Context**: Add cultural notes where relevant

### File Naming | फाइल नामकरण

- Use lowercase letters
- Use hyphens (-) instead of spaces
- Be descriptive but concise
- Use `.md` extension for Markdown files

**Examples:**
- ✅ `present-tense.md`
- ✅ `common-greetings.md`
- ✅ `ganesh-chaturthi.md`
- ❌ `Present Tense.md`
- ❌ `present_tense.md`

### Lesson Structure | धड्याची रचना

Each lesson file should include:

```markdown
# Title in English | मराठी शीर्षक

## Learning Objectives | शिक्षण उद्दिष्टे

- Objective 1
- Objective 2

## Introduction | परिचय

Brief introduction to the topic.

## Main Content | मुख्य सामग्री

### Section 1

Content with explanations...

### Examples | उदाहरणे

| English | Marathi | Transliteration |
|---------|---------|-----------------|
| Example 1 | उदाहरण १ | udharn ek |

## Practice Exercises | सराव व्यायाम

1. Exercise 1
2. Exercise 2

## Common Mistakes | सामान्य चुका

- Mistake 1: Explanation
- Mistake 2: Explanation

## Related Lessons | संबंधित धडे

- [Link to related lesson](path/to/lesson.md)

## Progress Checklist | प्रगती तपासणी सूची

- [ ] I understand the concept
- [ ] I can use it in sentences
- [ ] I have completed the exercises
```

### Vocabulary Format | शब्दसंग्रह स्वरूप

```markdown
| English | Marathi | Transliteration | Pronunciation | Example Sentence |
|---------|---------|-----------------|---------------|------------------|
| word | शब्द | shabd | shuh-bd | This is an example word. |
```

### Grammar Format | व्याकरण स्वरूप

```markdown
## Rule Explanation | नियम स्पष्टीकरण

Clear explanation of the grammar rule.

## Examples | उदाहरणे

| Marathi | Transliteration | English |
|---------|-----------------|---------|
| मी जातो | mi jato | I go (male) |

## Conjugation Table | रूपयोजन सारणी

| Person | Singular | Plural |
|--------|----------|--------|
| First | मी जातो | आम्ही जातो |

## Exceptions | अपवाद

- Exception 1: Explanation
```

### Conversation Format | संवाद स्वरूप

```markdown
## Dialogue | संवाद

**Person A:** नमस्कार, तुम्ही कसे आहात?
**Person B:** नमस्कार, मी ठीक आहे. तुम्ही कसे आहात?

## Transliteration | लिप्यंतरण

**Person A:** Namaskar, tumhi kase aahat?
**Person B:** Namaskar, mi thik ahe. Tumhi kase aahat?

## Translation | अनुवाद

**Person A:** Hello, how are you?
**Person B:** Hello, I am fine. How are you?

## Vocabulary Breakdown | शब्दसंग्रह विश्लेषण

| Word | Meaning | Notes |
|------|---------|-------|
| नमस्कार | Hello | Formal greeting |

## Cultural Notes | सांस्कृतिक टीपा

Additional cultural context...
```

---

## 📖 Style Guide | शैली मार्गदर्शक

### Markdown Formatting | मार्कडाउन स्वरूपन

- Use `#` for main titles (one per file)
- Use `##` for major sections
- Use `###` for subsections
- Use tables for organized data
- Use code blocks for examples
- Use bold (`**text**`) for emphasis
- Use italics (`*text*`) for transliterations

### Language Style | भाषा शैली

#### English
- Use simple, clear language
- Explain technical terms
- Provide examples for every concept
- Use inclusive language

#### Marathi
- Use standard Marathi (मानक मराठी)
- Avoid heavy dialect unless specified
- Provide transliterations
- Include pronunciation guides

### Transliteration System | लिप्यंतरण पद्धत

Use the following transliteration system:

| Marathi | Transliteration |
|---------|-----------------|
| अ | a |
| आ | aa |
| इ | i |
| ई | ii |
| उ | u |
| ऊ | uu |
| ऋ | ru |
| ए | e |
| ऐ | ai |
| ओ | o |
| औ | au |
| अं | am |
| अः | aha |
| क | ka |
| ख | kha |
| ग | ga |
| घ | gha |
| च | cha |
| छ | chha |
| ज | ja |
| झ | jha |
| ट | Ta (retroflex) |
| ठ | Tha (retroflex) |
| ड | Da (retroflex) |
| ढ | Dha (retroflex) |
| ण | Na (retroflex) |
| त | ta |
| थ | tha |
| द | da |
| ध | dha |
| न | na |
| प | pa |
| फ | pha |
| ब | ba |
| भ | bha |
| म | ma |
| य | ya |
| र | ra |
| ल | la |
| व | va |
| श | sha |
| ष | Sha (retroflex) |
| स | sa |
| ह | ha |

---

## 🔄 Pull Request Process | पुल विनंती प्रक्रिया

### Before Submitting | सबमिट करण्यापूर्वी

1. Ensure your code follows the style guide
2. Test all links and references
3. Update the README if needed
4. Add your name to CONTRIBUTORS.md (if desired)

### PR Checklist | पीआर चेकलिस्ट

- [ ] Content is bilingual (English + Marathi)
- [ ] Transliterations are provided
- [ ] Tables are properly formatted
- [ ] Links are working
- [ ] File naming follows conventions
- [ ] No duplicate content

### Review Process | पुनरावलोकन प्रक्रिया

1. Maintainers will review your PR
2. Feedback may be provided
3. Make necessary changes
4. Once approved, your PR will be merged

---

## 👥 Community | समुदाय

### Getting Help | मदत मिळवणे

- Open a [Discussion](https://github.com/your-username/learn-marathi/discussions) for questions
- Check existing discussions for answers
- Tag maintainers if urgent

### Recognition | मान्यता

All contributors are recognized in:

- CONTRIBUTORS.md file
- Release notes
- Project README

---

## 📚 Resources for Contributors | योगदानकर्त्यांसाठी संसाधने

### Markdown Guide

- [Basic Markdown Syntax](https://www.markdownguide.org/basic-syntax/)
- [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/)

### Marathi Language Resources

- [Marathi Wikipedia](https://mr.wikipedia.org/)
- [Marathi Dictionary](https://www.shabdkosh.com/marathi/)
- [Devanagari Unicode](https://unicode.org/charts/PDF/U0900.pdf)

### Tools

- [Devanagari Keyboard](https://www.google.com/inputtools/try/)
- [Marathi Spell Checker](https://www.rekhta.org/spell-check/marathi)

---

## ❓ Questions? | प्रश्न?

If you have any questions about contributing, please:

1. Check the [FAQ](https://github.com/your-username/learn-marathi/discussions/categories/q-a)
2. Open a [Discussion](https://github.com/your-username/learn-marathi/discussions)
3. Email: your-email@example.com

---

<div align="center">

**Thank you for helping make Marathi learning accessible to everyone!**

**मराठी शिक्षण सर्वांसाठी सुलभ करण्यास मदत केल्याबद्दल धन्यवाद!**

</div>
