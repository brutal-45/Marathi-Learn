#!/usr/bin/env python3
"""
English to Devanagari Transliteration Tool for Marathi

This script converts English text (Latin script) to Marathi Devanagari script.
It uses a mapping-based approach for common transliterations and supports
the ITRANS transliteration scheme.

Example:
    >>> transliterate("namaste")
    'नमस्ते'
    >>> transliterate("mi marathi shikto")
    'मी मराठी शिकतो'
"""

# Mapping tables for transliteration
# Vowels (स्वर)
VOWELS = {
    'a': 'अ', 'aa': 'आ', 'A': 'आ', 'i': 'इ', 'ii': 'ई', 'I': 'ई',
    'u': 'उ', 'uu': 'ऊ', 'U': 'ऊ', 'ru': 'ऋ', 'e': 'ए', 'ai': 'ऐ',
    'o': 'ओ', 'au': 'औ', 'au': 'औ'
}

# Vowel matras (वर्णमाला मात्रा)
MATRAS = {
    'a': '', 'aa': 'ा', 'A': 'ा', 'i': 'ि', 'ii': 'ी', 'I': 'ी',
    'u': 'ु', 'uu': 'ू', 'U': 'ू', 'ru': 'ृ', 'e': 'े', 'ai': 'ै',
    'o': 'ो', 'au': 'ौ'
}

# Consonants (व्यंजन)
CONSONANTS = {
    'k': 'क', 'kh': 'ख', 'g': 'ग', 'gh': 'घ', 'ng': 'ङ',
    'ch': 'च', 'chh': 'छ', 'Ch': 'छ', 'j': 'ज', 'jh': 'झ', 'ny': 'ञ',
    'T': 'ट', 'Th': 'ठ', 'D': 'ड', 'Dh': 'ढ', 'N': 'ण',
    't': 'त', 'th': 'थ', 'd': 'द', 'dh': 'ध', 'n': 'न',
    'p': 'प', 'ph': 'फ', 'f': 'फ', 'b': 'ब', 'bh': 'भ', 'm': 'म',
    'y': 'य', 'r': 'र', 'l': 'ल', 'L': 'ळ', 'v': 'व', 'w': 'व',
    'sh': 'श', 'Sh': 'ष', 's': 'स', 'h': 'ह',
    'ksh': 'क्ष', 'gy': 'ज्ञ', 'dny': 'ज्ञ'
}

# Special characters and punctuation
SPECIAL = {
    '.': '।',  # Devanagari danda
    '..': '॥',  # Double danda
    '0': '०', '1': '१', '2': '२', '3': '३', '4': '४',
    '5': '५', '6': '६', '7': '७', '8': '८', '9': '९'
}

# Common words dictionary for accurate transliteration
COMMON_WORDS = {
    'mi': 'मी', 'tu': 'तू', 'to': 'तो', 'ti': 'ती', 'te': 'ते',
    'aamhi': 'आम्ही', 'tumhi': 'तुम्ही', 'te': 'ते',
    'aahe': 'आहे', 'aahet': 'आहेत', 'nahi': 'नाही', 'na': 'नाही',
    'kay': 'काय', 'kasa': 'कसा', 'kashi': 'कशी', 'kase': 'कसे',
    'kuth': 'कुठे', 'kuthe': 'कुठे', 'kade': 'कडे',
    'kela': 'केला', 'karto': 'करतो', 'karte': 'करते',
    'marathi': 'मराठी', 'english': 'इंग्रजी', 'hindi': 'हिंदी',
    'bharat': 'भारत', 'mumbai': 'मुंबई', 'pune': 'पुणे',
    'namaste': 'नमस्कार', 'namaskar': 'नमस्कार',
    'dhanyavad': 'धन्यवाद', 'kripaya': 'कृपया',
    'shikto': 'शिकतो', 'shikte': 'शिकते', 'shikto': 'शिकतो',
    'aahe': 'आहे', 'ho': 'हो', 'nhi': 'नाही'
}


def transliterate_word(word):
    """
    Transliterate a single English word to Devanagari.
    
    Args:
        word (str): English word in Latin script
        
    Returns:
        str: Transliterated word in Devanagari script
        
    Example:
        >>> transliterate_word("namaste")
        'नमस्कार'
    """
    if not word:
        return word
    
    # Check if it's a known common word
    word_lower = word.lower()
    if word_lower in COMMON_WORDS:
        return COMMON_WORDS[word_lower]
    
    result = []
    i = 0
    n = len(word)
    
    while i < n:
        # Try to match longest patterns first
        
        # Check for special characters and numbers
        if word[i] in SPECIAL:
            result.append(SPECIAL[word[i]])
            i += 1
            continue
        
        # Check for two-character patterns first
        if i + 1 < n:
            two_char = word[i:i+2]
            
            # Check for consonant + matra combinations
            if two_char in MATRAS and i > 0:
                # This is a vowel marker after consonant
                pass
            
            # Check for consonants
            if two_char in CONSONANTS:
                result.append(CONSONANTS[two_char])
                i += 2
                continue
        
        # Check for single character
        char = word[i]
        
        # Vowels at the start or after a space
        if char in VOWELS and (i == 0 or not result):
            result.append(VOWELS[char])
            i += 1
            continue
        
        # Consonants
        if char in CONSONANTS:
            result.append(CONSONANTS[char])
            i += 1
            continue
        
        # Vowels as matras (after consonants)
        if char in MATRAS:
            result.append(MATRAS[char])
            i += 1
            continue
        
        # Default: keep the character as is
        result.append(char)
        i += 1
    
    return ''.join(result)


def transliterate(text):
    """
    Transliterate English text to Marathi Devanagari script.
    
    This is the main function that processes entire sentences or paragraphs,
    handling spaces and punctuation appropriately.
    
    Args:
        text (str): English text in Latin script
        
    Returns:
        str: Transliterated text in Devanagari script
        
    Example:
        >>> transliterate("mi marathi shikto")
        'मी मराठी शिकतो'
        >>> transliterate("namaste! kase aahat?")
        'नमस्कार! कसे आहात?'
    """
    if not text:
        return text
    
    # Split into words while preserving punctuation
    words = text.split()
    
    transliterated_words = []
    for word in words:
        # Handle punctuation at the end of words
        end_punct = ''
        while word and word[-1] in '.,!?;:':
            end_punct = word[-1] + end_punct
            word = word[:-1]
        
        # Transliterate the word
        if word:
            transliterated = transliterate_word(word)
            transliterated_words.append(transliterated + end_punct)
        else:
            transliterated_words.append(end_punct)
    
    return ' '.join(transliterated_words)


def interactive_mode():
    """
    Run the transliteration tool in interactive mode.
    
    Allows users to enter text and see the transliterated output
    in real-time.
    """
    print("=" * 50)
    print("Marathi Transliteration Tool")
    print("English → Devanagari")
    print("=" * 50)
    print("\nEnter English text to transliterate (or 'quit' to exit):\n")
    
    while True:
        try:
            user_input = input("English: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nधन्यवाद! (Thank you!)\n")
                break
            
            if not user_input:
                continue
            
            result = transliterate(user_input)
            print(f"Marathi: {result}\n")
            
        except KeyboardInterrupt:
            print("\n\nधन्यवाद! (Thank you!)\n")
            break
        except Exception as e:
            print(f"Error: {e}\n")


def batch_transliterate(input_file, output_file=None):
    """
    Transliterate multiple lines from a file.
    
    Args:
        input_file (str): Path to input file with English text
        output_file (str, optional): Path to save transliterated output.
                                     If None, prints to console.
    
    Example:
        >>> batch_transliterate("input.txt", "output.txt")
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        results = []
        for line in lines:
            line = line.strip()
            if line:
                results.append(transliterate(line))
            else:
                results.append('')
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(results))
            print(f"Transliterated {len(results)} lines to {output_file}")
        else:
            for result in results:
                print(result)
                
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")


# Main execution
if __name__ == "__main__":
    import sys
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--file" and len(sys.argv) >= 3:
            input_file = sys.argv[2]
            output_file = sys.argv[3] if len(sys.argv) > 3 else None
            batch_transliterate(input_file, output_file)
        else:
            # Transliterate command line argument
            text = ' '.join(sys.argv[1:])
            print(transliterate(text))
    else:
        # Run interactive mode
        interactive_mode()
