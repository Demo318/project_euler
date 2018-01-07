# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# Function to test if a number is prime.
def test_prime(num):
    # Number too small not to be prime.
    if abs(num) < 4:
        return True
    for i in range(2, int(num)):
        if num % i == 0:
            return False
    return True

# Ask for user input
print("Find the largest prime factor of a given number.")
user_num = float(input("Please enter a number: "))

# Declare initial factor & list for storing factors
cur_factor = 2
factors = []

# Try to divide by factor, factor ++ if user_num % factor != 0
while (user_num / cur_factor) != 1:
    if user_num % cur_factor == 0:
        factors.append(cur_factor)
        user_num = user_num / cur_factor
    else:
        cur_factor += 1
factors.append(int(user_num))



prime_factors = list(filter(test_prime, factors))

print(factors)
print(prime_factors)

print('Largest prime factor: ' str(prime_factors[-1]))