string = input("Enter the string:").lower()
vowels = ['a', 'e', 'i', 'o', 'u']

if any(vowel in string for vowel in vowels):
    print("Character found")
else:
    print("Not found")
