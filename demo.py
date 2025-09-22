print("addition: 5 + 3 = ",5+3)

print("this is from feature1 branch")


def greet_name(name):
    return f"welcome {name} from branching demo"

greet_name("pawan kumar")


def table(number):
    for i in range(1,11):
        return f"{number} * {i} = {number*i}"
    

table(7)


def check_age(age):
    if age >= 18:
        return "your able to vote"
    else:
        return "not able to vote"
check_age(20)


print("this is another test line")
print("this is testing")

def recur(num):
    if num <= 0:
        return 0
    else:
        result = num + recur(num - 1)
        return result
print(recur(5))  

print("this is another test line")



print("second dummy print")

print("this is dummy code")


num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")



num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")