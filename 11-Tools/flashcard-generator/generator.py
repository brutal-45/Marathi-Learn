#!/usr/bin/env python3
"""
Flashcard Generator for Marathi Learning

This script generates customizable flashcards for Marathi vocabulary practice. 
It supports various input formats and can export to multiple output formats
including plain text, JSON, and Anki-compatible format.

Example:
    >>> generator = FlashcardGenerator()
    >>> generator.add_card("नमस्कार", "Hello/Greeting")
    >>> generator.export_to_json("greetings.json")
"""

import json
import random
import os
from datetime import datetime
from typing import List, Dict, Optional, Tuple


class FlashCard:
    """
    Represents a single flashcard with front and back content.
    
    Attributes:
        front (str): The question side of the card (Marathi word)
        back (str): The answer side of the card (English meaning)
        category (str): Category/topic of the flashcard
        difficulty (str): Difficulty level (easy, medium, hard)
        examples (list): Example sentences using the word
        created_at (str): Timestamp of card creation
    """
    
    def __init__(self, front: str, back: str, category: str = "general",
                 difficulty: str = "medium", examples: List[str] = None):
        """
        Initialize a flashcard.
        
        Args:
            front: The front side content (Marathi)
            back: The back side content (English)
            category: Category for grouping cards
            difficulty: Difficulty level
            examples: List of example sentences
        """
        self.front = front
        self.back = back
        self.category = category
        self.difficulty = difficulty
        self.examples = examples or []
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert flashcard to dictionary representation."""
        return {
            'front': self.front,
            'back': self.back,
            'category': self.category,
            'difficulty': self.difficulty,
            'examples': self.examples,
            'created_at': self.created_at
        }
    
    def __str__(self) -> str:
        return f"Front: {self.front}\nBack: {self.back}"
    
    def __repr__(self) -> str:
        return f"FlashCard('{self.front}', '{self.back}')"


class FlashcardGenerator:
    """
    Main class for generating and managing flashcards.
    
    This class provides functionality to create, organize, and export
    flashcards for Marathi language learning.
    
    Example:
        >>> gen = FlashcardGenerator()
        >>> gen.add_card("फुलं", "Flowers", category="nature")
        >>> gen.export_to_json("nature_cards.json")
    """
    
    def __init__(self):
        """Initialize the flashcard generator with empty card collection."""
        self.cards: List[FlashCard] = []
        self.categories: set = set()
    
    def add_card(self, front: str, back: str, category: str = "general",
                 difficulty: str = "medium", examples: List[str] = None) -> None:
        """
        Add a new flashcard to the collection.
        
        Args:
            front: The Marathi word/phrase
            back: The English translation/meaning
            category: Category for organization
            difficulty: Difficulty level (easy, medium, hard)
            examples: List of example sentences
            
        Example:
            >>> gen.add_card("आई", "Mother", category="family", difficulty="easy")
        """
        card = FlashCard(front, back, category, difficulty, examples)
        self.cards.append(card)
        self.categories.add(category)
    
    def add_cards_from_list(self, card_list: List[Tuple[str, str]], 
                            category: str = "general") -> None:
        """
        Add multiple flashcards from a list of tuples.
        
        Args:
            card_list: List of (front, back) tuples
            category: Category for all cards
            
        Example:
            >>> cards = [("आई", "Mother"), ("वडील", "Father")]
            >>> gen.add_cards_from_list(cards, category="family")
        """
        for front, back in card_list:
            self.add_card(front, back, category)
    
    def add_cards_from_dict(self, card_dict: Dict[str, str], 
                           category: str = "general") -> None:
        """
        Add flashcards from a dictionary.
        
        Args:
            card_dict: Dictionary with Marathi words as keys and English as values
            category: Category for all cards
            
        Example:
            >>> cards = {"आई": "Mother", "वडील": "Father"}
            >>> gen.add_cards_from_dict(cards, category="family")
        """
        for front, back in card_dict.items():
            self.add_card(front, back, category)
    
    def get_cards_by_category(self, category: str) -> List[FlashCard]:
        """
        Get all flashcards in a specific category.
        
        Args:
            category: The category to filter by
            
        Returns:
            List of FlashCard objects in the specified category
        """
        return [card for card in self.cards if card.category == category]
    
    def get_cards_by_difficulty(self, difficulty: str) -> List[FlashCard]:
        """
        Get all flashcards of a specific difficulty.
        
        Args:
            difficulty: The difficulty level (easy, medium, hard)
            
        Returns:
            List of FlashCard objects with the specified difficulty
        """
        return [card for card in self.cards if card.difficulty == difficulty]
    
    def shuffle_cards(self) -> None:
        """Shuffle the order of all flashcards."""
        random.shuffle(self.cards)
    
    def export_to_json(self, filename: str) -> None:
        """
        Export flashcards to a JSON file.
        
        Args:
            filename: Output file path
            
        Example:
            >>> gen.export_to_json("my_flashcards.json")
        """
        data = {
            'metadata': {
                'total_cards': len(self.cards),
                'categories': list(self.categories),
                'exported_at': datetime.now().isoformat()
            },
            'cards': [card.to_dict() for card in self.cards]
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"Exported {len(self.cards)} cards to {filename}")
    
    def export_to_text(self, filename: str, separator: str = " | ") -> None:
        """
        Export flashcards to a plain text file.
        
        Args:
            filename: Output file path
            separator: Separator between front and back
            
        Example:
            >>> gen.export_to_text("flashcards.txt", separator=" -> ")
        """
        with open(filename, 'w', encoding='utf-8') as f:
            for card in self.cards:
                f.write(f"{card.front}{separator}{card.back}\n")
        
        print(f"Exported {len(self.cards)} cards to {filename}")
    
    def export_to_csv(self, filename: str) -> None:
        """
        Export flashcards to a CSV file.
        
        Args:
            filename: Output file path
            
        Example:
            >>> gen.export_to_csv("flashcards.csv")
        """
        import csv
        
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['front', 'back', 'category', 'difficulty', 'examples'])
            
            for card in self.cards:
                writer.writerow([
                    card.front,
                    card.back,
                    card.category,
                    card.difficulty,
                    '|'.join(card.examples) if card.examples else ''
                ])
        
        print(f"Exported {len(self.cards)} cards to {filename}")
    
    def export_to_anki(self, filename: str) -> None:
        """
        Export flashcards in Anki-compatible format.
        
        Creates a text file that can be imported directly into Anki.
        
        Args:
            filename: Output file path (without extension)
            
        Example:
            >>> gen.export_to_anki("marathi_vocab")
        """
        # Create the deck file
        deck_file = f"{filename}.txt"
        
        with open(deck_file, 'w', encoding='utf-8') as f:
            for card in self.cards:
                # Anki format: front\tback\ttags
                tags = f"{card.category} {card.difficulty}"
                examples_html = "<br>".join(card.examples) if card.examples else ""
                back_with_examples = f"{card.back}"
                if examples_html:
                    back_with_examples += f"<br><br><i>Examples:</i><br>{examples_html}"
                
                f.write(f"{card.front}\t{back_with_examples}\t{tags}\n")
        
        print(f"Exported {len(self.cards)} cards to {deck_file} (Anki format)")
    
    def import_from_json(self, filename: str) -> None:
        """
        Import flashcards from a JSON file.
        
        Args:
            filename: Input JSON file path
            
        Example:
            >>> gen.import_from_json("existing_cards.json")
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for card_data in data.get('cards', []):
                self.add_card(
                    front=card_data['front'],
                    back=card_data['back'],
                    category=card_data.get('category', 'general'),
                    difficulty=card_data.get('difficulty', 'medium'),
                    examples=card_data.get('examples', [])
                )
            
            print(f"Imported {len(data.get('cards', []))} cards from {filename}")
            
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in '{filename}'.")
    
    def practice_mode(self, reverse: bool = False) -> None:
        """
        Interactive practice mode for flashcard review.
        
        Args:
            reverse: If True, show English first and ask for Marathi
            
        Example:
            >>> gen.practice_mode(reverse=False)  # Show Marathi, guess English
        """
        if not self.cards:
            print("No flashcards available. Add some cards first!")
            return
        
        print("\n" + "=" * 50)
        print("Flashcard Practice Mode")
        print("=" * 50)
        print(f"Total cards: {len(self.cards)}")
        print("Press Enter to flip, 'n' for next, 'q' to quit\n")
        
        correct = 0
        total = 0
        
        for i, card in enumerate(self.cards, 1):
            front = card.back if reverse else card.front
            back = card.front if reverse else card.back
            
            print(f"\n[{i}/{len(self.cards)}] Category: {card.category}")
            print(f"{'English' if reverse else 'Marathi'}: {front}")
            
            user_input = input("Press Enter to reveal answer... ")
            
            if user_input.lower() == 'q':
                break
            
            print(f"{'Marathi' if reverse else 'English'}: {back}")
            
            if card.examples:
                print("Examples:")
                for ex in card.examples:
                    print(f"  • {ex}")
            
            response = input("\nDid you get it right? (y/n/s to skip): ").lower()
            
            if response == 's':
                continue
            elif response == 'y':
                correct += 1
            total += 1
        
        if total > 0:
            percentage = (correct / total) * 100
            print(f"\n{'=' * 50}")
            print(f"Practice complete!")
            print(f"Score: {correct}/{total} ({percentage:.1f}%)")
            print(f"{'=' * 50}\n")
    
    def generate_quiz(self, num_questions: int = 10) -> Dict:
        """
        Generate a multiple-choice quiz from flashcards.
        
        Args:
            num_questions: Number of questions to generate
            
        Returns:
            Dictionary containing quiz data
        """
        if len(self.cards) < 4:
            print("Need at least 4 cards to generate a quiz.")
            return {}
        
        num_questions = min(num_questions, len(self.cards))
        selected_cards = random.sample(self.cards, num_questions)
        
        quiz = {
            'title': 'Marathi Vocabulary Quiz',
            'created_at': datetime.now().isoformat(),
            'questions': []
        }
        
        for card in selected_cards:
            # Get wrong answers
            other_cards = [c for c in self.cards if c != card]
            wrong_answers = random.sample(other_cards, min(3, len(other_cards)))
            
            options = [card.back] + [c.back for c in wrong_answers]
            random.shuffle(options)
            
            quiz['questions'].append({
                'question': card.front,
                'correct_answer': card.back,
                'options': options
            })
        
        return quiz
    
    def __len__(self) -> int:
        return len(self.cards)
    
    def __str__(self) -> str:
        return f"FlashcardGenerator({len(self.cards)} cards, {len(self.categories)} categories)"


# Sample vocabulary data for demonstration
SAMPLE_VOCABULARY = {
    'family': {
        'आई': 'Mother',
        'वडील': 'Father',
        'बहीण': 'Sister',
        'भाऊ': 'Brother',
        'आजी': 'Grandmother',
        'आजोबा': 'Grandfather'
    },
    'numbers': {
        'एक': 'One',
        'दोन': 'Two',
        'तीन': 'Three',
        'चार': 'Four',
        'पाच': 'Five'
    },
    'greetings': {
        'नमस्कार': 'Hello/Greeting',
        'धन्यवाद': 'Thank you',
        'काय वेगळं?': "What's new?",
        'भेटून आनंद झाला': 'Nice to meet you'
    },
    'colors': {
        'लाल': 'Red',
        'निळा': 'Blue',
        'पांढरा': 'White',
        'काळा': 'Black',
        'हिरवा': 'Green',
        'पिवळा': 'Yellow'
    }
}


def create_sample_flashcards() -> FlashcardGenerator:
    """
    Create a sample flashcard set with common Marathi vocabulary.
    
    Returns:
        FlashcardGenerator populated with sample cards
    """
    generator = FlashcardGenerator()
    
    # Add cards from sample vocabulary
    for category, words in SAMPLE_VOCABULARY.items():
        generator.add_cards_from_dict(words, category=category)
    
    return generator


def main():
    """Main function demonstrating flashcard generator usage."""
    print("=" * 50)
    print("Marathi Flashcard Generator")
    print("=" * 50)
    
    # Create sample flashcards
    generator = create_sample_flashcards()
    
    print(f"\nCreated {len(generator)} sample flashcards")
    print(f"Categories: {', '.join(generator.categories)}")
    
    # Interactive menu
    while True:
        print("\n" + "-" * 30)
        print("Options:")
        print("1. Practice flashcards (Marathi → English)")
        print("2. Practice flashcards (English → Marathi)")
        print("3. Export to JSON")
        print("4. Export to CSV")
        print("5. Export to Anki format")
        print("6. Generate quiz")
        print("7. Add new card")
        print("8. Show all cards")
        print("9. Quit")
        print("-" * 30)
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            generator.practice_mode(reverse=False)
        elif choice == '2':
            generator.practice_mode(reverse=True)
        elif choice == '3':
            filename = input("Enter filename (default: flashcards.json): ").strip()
            filename = filename or "flashcards.json"
            generator.export_to_json(filename)
        elif choice == '4':
            filename = input("Enter filename (default: flashcards.csv): ").strip()
            filename = filename or "flashcards.csv"
            generator.export_to_csv(filename)
        elif choice == '5':
            filename = input("Enter filename (default: marathi_cards): ").strip()
            filename = filename or "marathi_cards"
            generator.export_to_anki(filename)
        elif choice == '6':
            num = input("Number of questions (default: 10): ").strip()
            num = int(num) if num.isdigit() else 10
            quiz = generator.generate_quiz(num)
            if quiz:
                print(f"\nGenerated quiz with {len(quiz['questions'])} questions")
                generator.export_to_json("quiz.json")
        elif choice == '7':
            front = input("Enter Marathi word: ").strip()
            back = input("Enter English meaning: ").strip()
            category = input("Enter category (default: general): ").strip() or "general"
            generator.add_card(front, back, category)
            print(f"Added: {front} → {back}")
        elif choice == '8':
            print(f"\nTotal cards: {len(generator)}")
            for card in generator.cards:
                print(f"  {card.front} → {card.back} [{card.category}]")
        elif choice == '9':
            print("\nधन्यवाद! (Thank you!)\n")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
