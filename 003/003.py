# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

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

print(factors)

print('Largest prime factor: ' + str(factors[-1]))
