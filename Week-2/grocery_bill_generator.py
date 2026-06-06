print("\n------------------")
print("   DAILY BASKET   ")
print("------------------")
print("\nAvailable items:\n")
items = ["Rice (1 kg)", 
         "Eggs (12 pcs)", 
         "Milk (1 L)", 
         "Bread (1 loaf)", 
         "Sugar (1 kg)", 
         "Cooking Oil (1 L)", 
         "Chicken (1 kg)", 
         "Potatoes (1 kg)",	
         "Onions (1 kg)", 
         "Bananas (12 pcs)"]
prices = [80, 150, 110, 60, 120, 180, 280, 50, 70, 100]

for i in range(len(items)):
  print(f"{i + 1}. {items[i]} - {prices[i]} TK")

choice = ""
total = 0

while choice != 'no':
  item = int(input("\nPlease enter the item number: "))

  if item < 1 or item > 10:
    print("Invalid item number. Try again.")
    continue

  quantity = int(input("Enter quantity: "))

  item_name = items[item - 1]
  price = prices[item - 1]

  cost = price * quantity 

  print(f"{item_name} x {quantity} = {cost} TK")

  total += cost 

  choice = input("\nAnything else?(yes/no): ").lower()

if total < 500: 
  discount = 0
  vat = total * 5/100
  bill = total + vat

elif total >= 500 and total < 1000:
  discount = total * 10/100
  vat = (total - discount) * 5/100 
  bill = total - discount + vat

else:
  discount = total * 20/100
  vat = (total - discount) * 5/100 
  bill = total - discount + vat

print("\n--------------------")
print("        BILL       ")
print("--------------------")

print(f"\nSubtotal: {total} TK")
print(f"Discount: {discount} TK")
print(f"VAT: {vat} TK")
print(f"Final Bill: {bill} TK\n")
