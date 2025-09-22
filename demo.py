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

<<<<<<< HEAD
print("this is another test line")
=======

print("this is testing")
>>>>>>> b4a92a9b21454f54b3249449a61d132067bfdb1e
