'''matrix = [1, 3, 2, 9, 5, 4, 3, 7, 9]
uniques = []

for i in matrix:
    if i not in uniques:
        uniques.append(i)
print(uniques)


digits = {
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine"
}
phone = input("Phone: ")
output = ""

for i in phone:
    output += digits.get(i, "!")+ " "
print(output)'''
