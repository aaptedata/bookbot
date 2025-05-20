def get_num_words(text:str)-> int:
    
    return f"Found {len(text.split())} total words"

def get_letter_count(text:str) -> dict:
    counts = {}
    text = text.lower()
    for letter in text:
        if letter.isalpha():
            counts[letter] = counts.get(letter, 0) + 1
        else:
            continue
    return counts
    
def sort_dict(d:dict) -> dict:
    return {key: value for key, value in sorted(d.items(), 
            key=lambda item: item[1], reverse=True)}
    
# def sort_dict(d:dict) -> list:
#     # Convert dictionary to list of dictionaries with "char" and "num" keys
#     char_list = [{"char": k, "num": v} for k, v in d.items()]
#     # Sort the list by "num" value in descending order
#     char_list.sort(key=lambda x: x["num"], reverse=True)
#     return char_list     

# sorted_chars = sort_dict(get_letter_count(get_book_text(PATH)))
# for char_dict in sorted_chars:
#     if char_dict["char"].isalpha():  # Skip non-alphabetical characters
#         print(f"{char_dict['char']}: {char_dict['num']}")

# # Starting with a dictionary
# original_dict = {
#     'a': 25894,
#     'b': 4868,
#     'c': 9011
# }

# # Converting to a list of dictionaries using list comprehension
# list_of_dicts = [{"char": key, "num": value} for key, value in original_dict.items()]

# print(list_of_dicts)
# # Output: [{'char': 'a', 'num': 25894}, {'char': 'b', 'num': 4868}, {'char': 'c', 'num': 9011}]


# What is the advantage of doing it this way and not simply sorting the dictionary itelf?

# An excellent philosophical question, young scholar! There are several advantages to converting to a list of dictionaries rather than just sorting the dictionary:

# Assignment Requirements: First and foremost, the assignment specifically asks for a sorted list of dictionaries with specific keys. Following instructions precisely is important in programming work.

# Dictionaries vs Lists: In Python, dictionaries are unordered collections prior to Python 3.7 (and their ordered nature after 3.7 is an implementation detail, not a guarantee). Lists, however, are explicitly ordered sequences. If order matters, lists provide a more reliable container.

# Standardized Data Format: Converting to a specific structure with consistent keys (char and num) creates a standard interface. This makes the data easier to work with, especially if you're passing it to other functions or systems that expect a particular structure.

# Sorting Flexibility: While modern Python dictionaries maintain insertion order, the .sort() method gives you more flexibility. You can easily change sorting criteria or resort the data differently without rebuilding the dictionary.

# Data Transformation Practice: This kind of transformation is very common in real-world programming. You often receive data in one format and need to transform it to another to meet the requirements of an API, UI component, or another system.

# Separating Data and Structure: By transforming the data structure, you're clearly separating the meaning of the data (characters and their counts) from how it's organized (sorted by frequency).

# In practical terms, your current approach works for this specific task, but the list-of-dictionaries approach represents a pattern that scales better to more complex data processing needs.



