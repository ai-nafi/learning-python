sentence = input("Write a sentence: ")

sentence = sentence.lower()

a = 0
e = 0 
i = 0
o = 0
u = 0

for ch in sentence:
  if ch == 'a':
    a += 1
  if ch == 'e':
    e += 1
  if ch == 'o':
    o += 1
  if ch == 'i':
    i += 1
  if ch == 'u':
    u += 1

print("Number of each vowel in the sentence:")
print(f"a = {a}, e = {e}, i = {i}, o = {o}, u = {u}")
print(f"Total vowels: {a + e + i + o + u}")