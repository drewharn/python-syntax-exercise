def print_upper_words(words):
    """Print each word on sep line uppercased.
        
        >>> print_upper_words(["Engineering", "does", "take", "practice"])
        ENGINEERING
        DOES
        TAKE
        PRACTICE
    """

    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """Print each word on sep line, uppercased, if it starts with E or e.
    
        >>> print_upper_words2(["Everett", "evermore", "Cooper", "deprive"])
        EVERETT
        EVERMORE
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given
    
        >>> print_upper_words3(["Everett", "evermore", "Cooper", "deprive", "zone"],
        ...                   must_start_with=["E", "C"])
        EVERETT
        COOPER
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break