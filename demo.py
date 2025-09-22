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
