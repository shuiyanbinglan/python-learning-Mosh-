ord("b")
# asscii码

temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")


age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

# message = "Eligible" if age >= 18 else "Not eligible"
print(message)


high_income = False
good_credit = True
student = True

if not student:
    print("Eligible")
if high_income and good_credit:
    # if high_income == True and good_credit == True :    布尔值没必要
    print("Eligible")
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

# age should be between 18 and 65
age = 22
if age >= 18 and age < 65:
    # if 8 <= age <65
    print("Eligible")


if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    # 比较首字母的ascii码的大小，如果相等，再比第二个，以此类推
    print("b")
else:
    print("c")


for number in range(3):
    print("Sending a message")
    print("Attempt", number)
    print("Attempt", number+1, (number+1) * ".")


successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# for else 语句


for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

# f转为字符，否则xy就是变量


print(type(5))
print(type(range(5)))

# Iterable
for x in "Python":
    print(x)
for y in [1, 2, 3, 4]:
    print(y)

for item in "shopping_cart":
    print(item)


number = 100
while number > 0:
    print(number)
    number //= 2


command = ""
while command != "quit" and command != "QUIT":
    command = input(">")
    print("ECHO", command)

# while command.lower() !="quit":
