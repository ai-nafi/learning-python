name = input("Enter your name: ")

username = name.replace(" ", "")
username = username.lower()

print(f"Cleaned username: {username}")

if len(username) >= 5:
  print("Valid username")
else:
  print("Invalid username")