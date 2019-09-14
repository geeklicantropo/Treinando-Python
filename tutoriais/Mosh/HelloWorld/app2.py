#prices = [10, 20, 30, 40]
#sum = 0
#for i in prices:
#    sum += i
#print(sum)

#numbers = [1,1,1,1,5]
#for x_count in numbers:
#    output = ''
#    for count in range(x_count):
#        output += 'x'
#    print(output)

'''word = input().lower()
is_palindrome = False

for i in range(0,len(word)):
    if word[i] == word[len(word)-i-1]:
        is_palindrome = True
    else:
        print("It's not palindrome")
        break
if is_palindrome:
    print(f"The {word} is palindrome.")'''

numbers = [10, 15, 7, 90, 5]
max_number = numbers[0]

for i in numbers:
    if i > max_number:
        max_number = i
print(max_number)