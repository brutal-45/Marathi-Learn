#!/usr/bin/env python3
"""
Quiz Generator for Marathi Language Learning

This script generates interactive quizzes for testing Marathi language skills.
It supports multiple question types, difficulty levels, and can create
customized quizzes from vocabulary lists.

Example:
    >>> quiz_gen = QuizGenerator()
    >>> quiz_gen.add_question("What is 'नमस्कार' in English?", "Hello", ["Goodbye", "Thanks", "Sorry"])
    >>> quiz_gen.run_quiz()
"""

import json
import random
import os
from datetime import datetime
from typing import List, Dict, Tuple, Optional, Callable
from enum import Enum


class QuestionType(Enum):
    """Types of quiz questions available."""
    MULTIPLE_CHOICE = "multiple_choice"
    FILL_IN_BLANK = "fill_in_blank"
    TRANSLATION = "translation"
    MATCHING = "matching"
    TRUE_FALSE = "true_false"


class Difficulty(Enum):
    """Difficulty levels for quiz questions."""
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    MIXED = "mixed"


class QuizQuestion:
    """
    Represents a single quiz question.
    
    Attributes:
        question (str): The question text
        correct_answer (str): The correct answer
        options (list): List of possible answers (for multiple choice)
        question_type (QuestionType): Type of question
        difficulty (Difficulty): Difficulty level
        explanation (str): Explanation of the correct answer
        points (int): Points awarded for correct answer
    """
    
    def __init__(self, question: str, correct_answer: str, 
                 options: List[str] = None, 
                 question_type: QuestionType = QuestionType.MULTIPLE_CHOICE,
                 difficulty: Difficulty = Difficulty.MEDIUM,
                 explanation: str = "",
                 points: int = 1):
        """
        Initialize a quiz question.
        
        Args:
            question: The question text
            correct_answer: The correct answer
            options: List of options for multiple choice
            question_type: Type of question
            difficulty: Difficulty level
            explanation: Explanation shown after answering
            points: Points for correct answer
        """
        self.question = question
        self.correct_answer = correct_answer
        self.options = options or []
        self.question_type = question_type
        self.difficulty = difficulty
        self.explanation = explanation
        self.points = points
    
    def to_dict(self) -> Dict:
        """Convert question to dictionary representation."""
        return {
            'question': self.question,
            'correct_answer': self.correct_answer,
            'options': self.options,
            'question_type': self.question_type.value,
            'difficulty': self.difficulty.value,
            'explanation': self.explanation,
            'points': self.points
        }
    
    def check_answer(self, user_answer: str) -> bool:
        """
        Check if the user's answer is correct.
        
        Args:
            user_answer: The user's submitted answer
            
        Returns:
            True if correct, False otherwise
        """
        # Normalize answers for comparison
        normalized_user = user_answer.strip().lower()
        normalized_correct = self.correct_answer.strip().lower()
        
        # Check exact match
        if normalized_user == normalized_correct:
            return True
        
        # Check if answer is in options (for multiple choice)
        if self.options:
            for option in self.options:
                if normalized_user == option.strip().lower():
                    return option.strip().lower() == normalized_correct
        
        return False


class QuizGenerator:
    """
    Main class for generating and running Marathi language quizzes.
    
    This class provides functionality to create, customize, and run
    quizzes with various question types and difficulty levels.
    
    Example:
        >>> quiz = QuizGenerator(title="Basic Greetings")
        >>> quiz.add_multiple_choice("What is 'नमस्कार'?", "Hello", ["Bye", "Hi", "Hey"])
        >>> quiz.run()
    """
    
    def __init__(self, title: str = "Marathi Quiz", 
                 difficulty: Difficulty = Difficulty.MIXED):
        """
        Initialize the quiz generator.
        
        Args:
            title: Title of the quiz
            difficulty: Default difficulty level
        """
        self.title = title
        self.difficulty = difficulty
        self.questions: List[QuizQuestion] = []
        self.score = 0
        self.total_points = 0
        self.answers: List[Dict] = []
    
    def add_question(self, question: str, correct_answer: str,
                     options: List[str] = None,
                     question_type: QuestionType = QuestionType.MULTIPLE_CHOICE,
                     difficulty: Difficulty = None,
                     explanation: str = "",
                     points: int = 1) -> None:
        """
        Add a question to the quiz.
        
        Args:
            question: The question text
            correct_answer: The correct answer
            options: List of options for multiple choice
            question_type: Type of question
            difficulty: Difficulty level (uses default if None)
            explanation: Explanation shown after answering
            points: Points for correct answer
            
        Example:
            >>> quiz.add_question("Translate 'आई'", "Mother", ["Father", "Sister", "Brother"])
        """
        q = QuizQuestion(
            question=question,
            correct_answer=correct_answer,
            options=options,
            question_type=question_type,
            difficulty=difficulty or self.difficulty,
            explanation=explanation,
            points=points
        )
        self.questions.append(q)
        self.total_points += points
    
    def add_multiple_choice(self, question: str, correct_answer: str,
                            wrong_answers: List[str], 
                            difficulty: Difficulty = None,
                            explanation: str = "",
                            points: int = 1) -> None:
        """
        Add a multiple choice question with auto-shuffled options.
        
        Args:
            question: The question text
            correct_answer: The correct answer
            wrong_answers: List of incorrect options (typically 3)
            difficulty: Difficulty level
            explanation: Explanation shown after answering
            points: Points for correct answer
            
        Example:
            >>> quiz.add_multiple_choice("What is 'पाणी'?", "Water", ["Fire", "Air", "Earth"])
        """
        options = [correct_answer] + wrong_answers
        random.shuffle(options)
        
        self.add_question(
            question=question,
            correct_answer=correct_answer,
            options=options,
            question_type=QuestionType.MULTIPLE_CHOICE,
            difficulty=difficulty,
            explanation=explanation,
            points=points
        )
    
    def add_fill_in_blank(self, sentence: str, answer: str,
                          hint: str = None,
                          difficulty: Difficulty = None,
                          points: int = 2) -> None:
        """
        Add a fill-in-the-blank question.
        
        Args:
            sentence: Sentence with '___' as placeholder
            answer: The correct answer to fill in
            hint: Optional hint for the learner
            difficulty: Difficulty level
            points: Points for correct answer
            
        Example:
            >>> quiz.add_fill_in_blank("माझे नाव ___ आहे", "राम", hint="My name is Ram")
        """
        question = sentence
        if hint:
            question += f"\n(Hint: {hint})"
        
        self.add_question(
            question=question,
            correct_answer=answer,
            question_type=QuestionType.FILL_IN_BLANK,
            difficulty=difficulty,
            points=points
        )
    
    def add_translation(self, text: str, translation: str,
                        direction: str = "marathi_to_english",
                        difficulty: Difficulty = None,
                        points: int = 2) -> None:
        """
        Add a translation question.
        
        Args:
            text: The text to translate
            translation: The correct translation
            direction: "marathi_to_english" or "english_to_marathi"
            difficulty: Difficulty level
            points: Points for correct answer
            
        Example:
            >>> quiz.add_translation("धन्यवाद", "Thank you")
        """
        if direction == "marathi_to_english":
            question = f"Translate to English: {text}"
        else:
            question = f"Translate to Marathi: {text}"
        
        self.add_question(
            question=question,
            correct_answer=translation,
            question_type=QuestionType.TRANSLATION,
            difficulty=difficulty,
            points=points
        )
    
    def add_true_false(self, statement: str, is_true: bool,
                       explanation: str = "",
                       difficulty: Difficulty = Difficulty.EASY,
                       points: int = 1) -> None:
        """
        Add a true/false question.
        
        Args:
            statement: The statement to evaluate
            is_true: Whether the statement is true
            explanation: Explanation of the correct answer
            difficulty: Difficulty level
            points: Points for correct answer
            
        Example:
            >>> quiz.add_true_false("'आई' means Father", False, "'आई' means Mother")
        """
        self.add_question(
            question=f"True or False: {statement}",
            correct_answer="True" if is_true else "False",
            options=["True", "False"],
            question_type=QuestionType.TRUE_FALSE,
            difficulty=difficulty,
            explanation=explanation,
            points=points
        )
    
    def generate_from_vocabulary(self, vocabulary: Dict[str, str],
                                 num_questions: int = 10,
                                 question_types: List[QuestionType] = None) -> None:
        """
        Generate quiz questions automatically from a vocabulary dictionary.
        
        Args:
            vocabulary: Dictionary of {Marathi: English} word pairs
            num_questions: Number of questions to generate
            question_types: Types of questions to include
            
        Example:
            >>> vocab = {"आई": "Mother", "वडील": "Father", "भाऊ": "Brother"}
            >>> quiz.generate_from_vocabulary(vocab, num_questions=5)
        """
        if not question_types:
            question_types = [QuestionType.MULTIPLE_CHOICE, QuestionType.TRANSLATION]
        
        items = list(vocabulary.items())
        random.shuffle(items)
        num_questions = min(num_questions, len(items))
        
        # Get wrong answer pool
        all_english = list(vocabulary.values())
        
        for i in range(num_questions):
            marathi, english = items[i]
            
            # Alternate question types
            q_type = question_types[i % len(question_types)]
            
            if q_type == QuestionType.MULTIPLE_CHOICE:
                # Get 3 wrong answers
                wrong = [e for e in all_english if e != english]
                wrong_answers = random.sample(wrong, min(3, len(wrong)))
                self.add_multiple_choice(
                    question=f"What does '{marathi}' mean?",
                    correct_answer=english,
                    wrong_answers=wrong_answers
                )
            elif q_type == QuestionType.TRANSLATION:
                direction = random.choice(["marathi_to_english", "english_to_marathi"])
                if direction == "marathi_to_english":
                    self.add_translation(marathi, english, direction)
                else:
                    self.add_translation(english, marathi, "english_to_marathi")
    
    def shuffle_questions(self) -> None:
        """Randomize the order of questions."""
        random.shuffle(self.questions)
    
    def run(self, show_answers: bool = True) -> Dict:
        """
        Run the quiz interactively.
        
        Args:
            show_answers: Whether to show correct answers after each question
            
        Returns:
            Dictionary with quiz results
        """
        if not self.questions:
            print("No questions in the quiz. Add questions first!")
            return {}
        
        print("\n" + "=" * 50)
        print(f"  {self.title}")
        print("=" * 50)
        print(f"Total Questions: {len(self.questions)}")
        print(f"Total Points: {self.total_points}")
        print("\nPress Enter to start...\n")
        input()
        
        self.score = 0
        self.answers = []
        
        for i, q in enumerate(self.questions, 1):
            print(f"\n{'─' * 50}")
            print(f"Question {i}/{len(self.questions)} [{q.difficulty.value}]")
            print(f"Points: {q.points}")
            print(f"{'─' * 50}")
            print(q.question)
            
            if q.question_type == QuestionType.MULTIPLE_CHOICE:
                print("\nOptions:")
                for j, option in enumerate(q.options, 1):
                    print(f"  {j}. {option}")
                
                while True:
                    try:
                        answer = input("\nYour answer (number or text): ").strip()
                        if answer.isdigit():
                            idx = int(answer) - 1
                            if 0 <= idx < len(q.options):
                                user_answer = q.options[idx]
                                break
                        else:
                            user_answer = answer
                            break
                    except ValueError:
                        print("Invalid input. Please try again.")
            
            elif q.question_type == QuestionType.TRUE_FALSE:
                answer = input("\nYour answer (T/F or True/False): ").strip().lower()
                user_answer = "True" if answer in ['t', 'true', 'yes'] else "False"
            
            else:
                user_answer = input("\nYour answer: ").strip()
            
            # Check answer
            is_correct = q.check_answer(user_answer)
            
            result = {
                'question': q.question,
                'user_answer': user_answer,
                'correct_answer': q.correct_answer,
                'is_correct': is_correct,
                'points_earned': q.points if is_correct else 0
            }
            self.answers.append(result)
            
            if is_correct:
                self.score += q.points
                print("\n✓ Correct!")
            else:
                print(f"\n✗ Incorrect. The correct answer is: {q.correct_answer}")
            
            if q.explanation and show_answers:
                print(f"\nExplanation: {q.explanation}")
        
        # Show final results
        percentage = (self.score / self.total_points) * 100 if self.total_points > 0 else 0
        
        print("\n" + "=" * 50)
        print("  QUIZ COMPLETE!")
        print("=" * 50)
        print(f"Score: {self.score}/{self.total_points} ({percentage:.1f}%)")
        
        # Grade
        if percentage >= 90:
            grade = "A (Excellent!)"
        elif percentage >= 80:
            grade = "B (Good job!)"
        elif percentage >= 70:
            grade = "C (Keep practicing!)"
        elif percentage >= 60:
            grade = "D (Need more practice)"
        else:
            grade = "F (Review the material and try again)"
        
        print(f"Grade: {grade}")
        print("=" * 50 + "\n")
        
        return {
            'title': self.title,
            'score': self.score,
            'total_points': self.total_points,
            'percentage': percentage,
            'grade': grade,
            'answers': self.answers,
            'completed_at': datetime.now().isoformat()
        }
    
    def export_to_json(self, filename: str) -> None:
        """
        Export the quiz to a JSON file.
        
        Args:
            filename: Output file path
        """
        data = {
            'title': self.title,
            'difficulty': self.difficulty.value,
            'total_questions': len(self.questions),
            'total_points': self.total_points,
            'questions': [q.to_dict() for q in self.questions]
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"Quiz exported to {filename}")
    
    def import_from_json(self, filename: str) -> None:
        """
        Import a quiz from a JSON file.
        
        Args:
            filename: Input JSON file path
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.title = data.get('title', self.title)
            self.questions = []
            self.total_points = 0
            
            for q_data in data.get('questions', []):
                self.add_question(
                    question=q_data['question'],
                    correct_answer=q_data['correct_answer'],
                    options=q_data.get('options'),
                    question_type=QuestionType(q_data.get('question_type', 'multiple_choice')),
                    difficulty=Difficulty(q_data.get('difficulty', 'medium')),
                    explanation=q_data.get('explanation', ''),
                    points=q_data.get('points', 1)
                )
            
            print(f"Imported {len(self.questions)} questions from {filename}")
            
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in '{filename}'.")
    
    def get_summary(self) -> Dict:
        """Get a summary of the quiz contents."""
        return {
            'title': self.title,
            'total_questions': len(self.questions),
            'total_points': self.total_points,
            'difficulty_breakdown': {
                difficulty.value: len([q for q in self.questions if q.difficulty == difficulty])
                for difficulty in Difficulty if difficulty != Difficulty.MIXED
            },
            'type_breakdown': {
                qtype.value: len([q for q in self.questions if q.question_type == qtype])
                for qtype in QuestionType
            }
        }


# Sample vocabulary for demo quizzes
SAMPLE_VOCABULARY = {
    # Family
    'आई': 'Mother', 'वडील': 'Father', 'बहीण': 'Sister', 'भाऊ': 'Brother',
    'आजी': 'Grandmother', 'आजोबा': 'Grandfather',
    # Greetings
    'नमस्कार': 'Hello', 'धन्यवाद': 'Thank you', 'क्षमा करा': 'Sorry',
    # Numbers
    'एक': 'One', 'दोन': 'Two', 'तीन': 'Three', 'चार': 'Four', 'पाच': 'Five',
    # Colors
    'लाल': 'Red', 'निळा': 'Blue', 'पांढरा': 'White', 'काळा': 'Black',
    # Common words
    'पाणी': 'Water', 'अन्न': 'Food', 'घर': 'House', 'पुस्तक': 'Book'
}


def create_beginner_quiz() -> QuizGenerator:
    """Create a beginner-level quiz with basic vocabulary."""
    quiz = QuizGenerator(title="Marathi Basics - Beginner Quiz", 
                        difficulty=Difficulty.EASY)
    
    # Multiple choice questions
    quiz.add_multiple_choice(
        "What does 'नमस्कार' mean?",
        "Hello",
        ["Goodbye", "Thank you", "Sorry"],
        explanation="'नमस्कार' is a common greeting in Marathi"
    )
    
    quiz.add_multiple_choice(
        "What does 'आई' mean?",
        "Mother",
        ["Father", "Sister", "Brother"],
        explanation="'आई' is the Marathi word for Mother"
    )
    
    quiz.add_multiple_choice(
        "What does 'धन्यवाद' mean?",
        "Thank you",
        ["Hello", "Sorry", "Please"],
        explanation="'धन्यवाद' is used to express gratitude"
    )
    
    # True/False
    quiz.add_true_false(
        "'वडील' means Mother",
        False,
        "'वडील' means Father, 'आई' means Mother"
    )
    
    quiz.add_true_false(
        "'पाणी' means Water",
        True,
        "'पाणी' is the Marathi word for Water"
    )
    
    # Translation
    quiz.add_translation("एक", "One", difficulty=Difficulty.EASY)
    quiz.add_translation("दोन", "Two", difficulty=Difficulty.EASY)
    
    return quiz


def create_intermediate_quiz() -> QuizGenerator:
    """Create an intermediate-level quiz."""
    quiz = QuizGenerator(title="Marathi Intermediate Quiz",
                        difficulty=Difficulty.MEDIUM)
    
    # Fill in the blank
    quiz.add_fill_in_blank(
        "माझे नाव ___ आहे (My name is ___)",
        "राम",
        hint="Common Indian name",
        difficulty=Difficulty.MEDIUM
    )
    
    quiz.add_fill_in_blank(
        "मी मराठी ___ शिकतो (I am learning ___)",
        "बोलत",
        hint="Speaking/talking",
        difficulty=Difficulty.HARD
    )
    
    # Translation
    quiz.add_translation("तुम्ही कसे आहात?", "How are you?", difficulty=Difficulty.MEDIUM)
    quiz.add_translation("मी ठीक आहे", "I am fine", difficulty=Difficulty.MEDIUM)
    
    # Multiple choice
    quiz.add_multiple_choice(
        "What is the plural of 'फूल' (flower)?",
        "फुलं",
        ["फूले", "फुलां", "फुल"],
        explanation="In Marathi, 'फूल' becomes 'फुलं' in plural"
    )
    
    return quiz


def main():
    """Main function demonstrating quiz generator usage."""
    print("=" * 50)
    print("Marathi Quiz Generator")
    print("=" * 50)
    
    while True:
        print("\n" + "-" * 40)
        print("Options:")
        print("1. Take Beginner Quiz")
        print("2. Take Intermediate Quiz")
        print("3. Generate Quiz from Vocabulary")
        print("4. Create Custom Quiz")
        print("5. Import Quiz from File")
        print("6. Quit")
        print("-" * 40)
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            quiz = create_beginner_quiz()
            quiz.run()
            
        elif choice == '2':
            quiz = create_intermediate_quiz()
            quiz.run()
            
        elif choice == '3':
            num = input("Number of questions (default: 10): ").strip()
            num = int(num) if num.isdigit() else 10
            
            quiz = QuizGenerator(title="Vocabulary Quiz")
            quiz.generate_from_vocabulary(SAMPLE_VOCABULARY, num_questions=num)
            quiz.run()
            
        elif choice == '4':
            title = input("Quiz title: ").strip() or "Custom Quiz"
            quiz = QuizGenerator(title=title)
            
            while True:
                print("\nAdd Question:")
                print("1. Multiple Choice")
                print("2. True/False")
                print("3. Translation")
                print("4. Fill in Blank")
                print("5. Finish and Start Quiz")
                
                q_choice = input("Select: ").strip()
                
                if q_choice == '1':
                    q_text = input("Question: ").strip()
                    correct = input("Correct answer: ").strip()
                    wrong = input("Wrong answers (comma-separated): ").strip()
                    wrong_list = [w.strip() for w in wrong.split(',')]
                    quiz.add_multiple_choice(q_text, correct, wrong_list)
                    
                elif q_choice == '2':
                    statement = input("Statement: ").strip()
                    is_true = input("Is this true? (y/n): ").strip().lower() == 'y'
                    quiz.add_true_false(statement, is_true)
                    
                elif q_choice == '3':
                    text = input("Text to translate: ").strip()
                    translation = input("Translation: ").strip()
                    quiz.add_translation(text, translation)
                    
                elif q_choice == '4':
                    sentence = input("Sentence (use ___ for blank): ").strip()
                    answer = input("Answer: ").strip()
                    quiz.add_fill_in_blank(sentence, answer)
                    
                elif q_choice == '5':
                    if quiz.questions:
                        quiz.run()
                    break
            
        elif choice == '5':
            filename = input("Enter filename: ").strip()
            quiz = QuizGenerator()
            quiz.import_from_json(filename)
            if quiz.questions:
                quiz.run()
            
        elif choice == '6':
            print("\nधन्यवाद! (Thank you!)\n")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
