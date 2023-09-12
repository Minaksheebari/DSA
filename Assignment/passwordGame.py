import math

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def smallest_prime(numbers):
    for num in numbers:
        if is_prime(num):
            return num
    return None

def smallest_prime_divisor_of_sum(numbers):
    sum_of_numbers = sum(numbers)
    for i in range(2, sum_of_numbers + 1):
        if sum_of_numbers % i == 0 and is_prime(i):
            return i

def anticlockwise_rotation(numbers, times):
    times %= len(numbers)
    return numbers[times:] + numbers[:times]

def main():
    n = int(input("Enter N: "))
    numbers = list(map(int, input("Enter the list of numbers separated by space: ").split()))

    smallest_prime_number = smallest_prime(numbers)
    
    if smallest_prime_number:
        modulo_result = sum(numbers) % smallest_prime_number
    else:
        smallest_prime_divisor = smallest_prime_divisor_of_sum(numbers)
        modulo_result = sum(numbers) % smallest_prime_divisor
    
    password = anticlockwise_rotation(numbers, modulo_result)
    
    print("Password:", " ".join(map(str, password)))

if __name__ == "__main__":
    main()
