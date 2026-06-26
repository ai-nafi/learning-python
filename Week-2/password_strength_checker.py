password = input("Enter password: ")

uppercase = False
lowercase = False
digit = False
special_character = False

if len(password) >= 8:

  i = 0
  while i < len(password):

    char = password[i]

    if char >= 'A' and char <= 'Z':
      uppercase = True
    elif char >= 'a' and char <= 'z':
      lowercase = True
    elif char >= '0' and char <= '9':
      digit = True
    else:
      special_character = True

    i += 1

  rule_check = 0

  if uppercase:
    rule_check += 1

  if lowercase:
    rule_check += 1

  if digit:
    rule_check += 1

  if special_character:
    rule_check += 1

  if rule_check == 4:
    print("Strong")
  elif rule_check >= 2:
    print("Medium")
  else:
    print("Weak")

else:
  print("Weak")