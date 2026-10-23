text = input("Enter text: ")
pattern = input("Enter pattern: ")

for i in range(len(text) - len(pattern) + 1):
    if text[i:i + len(pattern)] == pattern:
        print("Pattern found at index", i)