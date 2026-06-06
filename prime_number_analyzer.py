n = int(input("Show primes up to: "))

prime_count = 0
prime_sum = 0
largest_prime = 0

print(f"Primes upto {n}:") 
for num in range(2, n + 1):
  isprime = True

  for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
      isprime = False
      break
  
  if isprime:
      print(num)
      prime_count += 1
      prime_sum += num
      largest_prime = num

print(f"Total primes upto {n}: {prime_count}")
print(f"Largest prime upto {n}: {largest_prime}")
print(f"Sum of all primes upto {n}: {prime_sum}")