username = 'Nafifi'
password = '966969'

name = input("Please enter your username: ")
passcode = input("Enter your password: ")

if name == "" or passcode == "":
  print("Please enter username and password")

elif name == username and passcode == password:
  print("Login successful!")
  print(f"Welcome, {username}!")

elif name != username and passcode != password:
  print("Both username and password are incorrect")

elif name != username:
  print("Incorrect username")

else:
  print("Incorrect password")