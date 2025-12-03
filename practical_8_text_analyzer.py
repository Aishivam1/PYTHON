text = input("Enter text to analyze: ")

word_count = len(text.split())
char_count = len(text)
space_count = text.count(" ")

vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)

consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
consonant_count = sum(1 for char in text if char in consonants)

print("\n--- Text Analysis ---")
print(f"Total characters: {char_count}")
print(f"Total words: {word_count}")
print(f"Spaces: {space_count}")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
