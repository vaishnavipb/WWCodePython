# Day 33: Write a test case for a function that checks if a number is prime.

def is_prime(n):
    prime = True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            prime = False
            break
    return prime

#
# n = int(input("Enter a number\n"))
#
# print(f"The number {n} is prime? {is_prime(n)}")
