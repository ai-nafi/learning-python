sentence = input("Write a sentence: ")

words = sentence.split()

print(f"Total words: {len(words)}")

longest = words[0]

for word in words:
  if len(word) > len(longest):
    longest = word

print(f"Longest word: {longest}")
