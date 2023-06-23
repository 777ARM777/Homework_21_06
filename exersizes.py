def find_factorial():
    """Takes a positive integer as input and calculates its factorial"""
    num = int(input("Enter a number to count a factorial: "))
    if num <= 0:
        pass
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact


print(find_factorial())


# Write a Python program that prints all the prime numbers between 1 and 100 using a for loop and the break keyword.
print("Here are prime numbers between 1 and 100")
for i in range(2, 100):
    is_prime = True
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)

# Implement a Python program that asks the user to enter a password. If the password matches a predefined secret
# password, display a success message. Otherwise, display an error message using an if/else ternary expression
password = 'user1234'
userPassword = input("Enter password: ")
if userPassword == password:
    print("Login succeeded")
else:
    print("Wrong password")


# Create a Python function called print_pattern that takes an integer
# as input and prints the following pattern using a while loop:
def print_pattern(count):
    """takes an integer as input and prints a pattern"""
    tmp = 1
    while tmp <= count:
        i = 1
        while i <= tmp:
            print(i, end=' ')
            i += 1
        tmp += 1
        print()


n = int(input("Enter a number to print a pattern: "))
print_pattern(n)
print()


# Write a Python function called find_common_elements that takes two lists as input and returns a new list containing
# the common elements between the two input lists. Use a for loop and an if statement to check for common elements
def find_common_elements(l1, l2):
    new_list = []
    for item in l1:
        if item in l2:
            new_list.append(item)
    return new_list


list1 = [1, 2, 3, 5, 6, 9, 8]
list2 = [1, 25, 74, 5, 95, 8, 884]
print(find_common_elements(list1, list2))


# Implement a Python function called find_prime_factors that takes a positive integer as input and
# returns a list of its prime factors. Use a while loop and an if statement to find and add prime factors to the list.
def find_prime_factors(num):
    arr = []
    count = 2
    while num > 1:
        if num % count == 0:
            num = num // count
            if count not in arr:
                arr.append(count)
        else:
            count += 1
    return arr


number = int(input("Enter a number to find prime factors: "))
print(find_prime_factors(number))

