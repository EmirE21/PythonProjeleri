def get_prime_numbers(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_numbers = filter(lambda n: is_prime(n), numbers)
    return list(prime_numbers)