string = input("Write a word: ")

print(f"\nYour word: {string}")

print(f"First character: {string[0]}")
print(f"Last character: {string[len(string) - 1]}")

if len(string) % 2 == 0:
  print(f"Middle characters: {string[len(string)//2-1]}{string[len(string)//2]}")
else:
  print(f"Middle character: {string[len(string)//2]}\n")