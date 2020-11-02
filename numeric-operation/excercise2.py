# first_value = int(input('First Number: '))
#second_value = int(input('Second number: '))
#sum = first_value + second_value
#print("Sum: " + str(sum))

first_value = input('first Number: ')
second_value = input('second Number: ')

if first_value.isnumeric() == False or second_value.isnumeric == False:
    print('Please input numbers alone')
    exit()

sum = int(first_value) + int(second_value)
print(str(sum))

