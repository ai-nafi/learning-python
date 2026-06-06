print("\n---------------------")
print("     ATM SYSTEM")
print("---------------------")

pin = '4321'
attempt = 0
login = False
balance = 10000

while attempt < 3:
  user_pin = input("\nEnter pin: ")
  if user_pin == pin:
    print("\nLogin successful")
    login = True
    break
  
  else:
    attempt += 1
    print("Incorrect PIN!")
    print("Attempts left: ", 3 - attempt)
    continue

if attempt == 3:
  print("\nAccount blocked!")
  print("Too many incorrect attempts.\n")

if login:
  while True:
   print("\n----------")
   print("   MENU")
   print("----------")
   print("1. Check Balance")
   print("2. Deposit")
   print("3. Withdraw")
   print("4. Exit")

   choice = int(input("\nEnter choice: "))

   if choice == 1:
     print(f"\nCurrent balance: {balance} TK")

   elif choice == 2:
     deposit = int(input("\nEnter amount to deposit: "))

     if deposit <= 0:
       print("\nDeposit amount must be greater than 0.")
     else:
       balance = balance + deposit
       print(f"\nDeposit Successful!\n\nDeposited: {deposit} TK\nNew Balance: {balance} TK")

    
   elif choice == 3:
     withdraw = int(input("\nEnter amount to withdraw: "))
    
     if withdraw <= 0:
       print("\nWithdraw amount must be greater than 0.")

     elif withdraw <= 6000:
       if withdraw > balance:
         print(f"\nInsufficient Balance!\nAvailable Balance: {balance} TK")
       else:
         balance = balance - withdraw
         print(f"\nWithdrawal Successful!\n\nCollected: {withdraw} TK\nRemaining Balance: {balance} TK")
     else:
       print(f"\nWithdrawal Limit Exceeded!\nMaximum withdrawal amount is 6000 TK.")

   elif choice == 4:
     print("\nThank you for using our ATM.\nHave a nice day!\n")
     break
   
   else:
     print("Invalid choice!")
