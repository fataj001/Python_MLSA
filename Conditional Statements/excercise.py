#print(type(7))
#print(type('hello world'))
#print(type(True))
#print(type('false'))


#print(bool('True'))
#print(bool('False'))
#print(bool(''))
#print(bool(' '))
#print(bool('Hello world!'))
#Comparing Numbers
num1 = 5
num2 = 0
true_value = True
false_value = False
if num1 > 1 and num2 < 10:
    print('The value is between 1 and 10')
if num1 > 1 or num2 > 1:
    print('atleast one value is greater than 1')

print(not true_value)
print(not false_value)

if not num1 > 1 and num2 < 10:
    print('Both values pass the test')
else:
    print('Both values do not pass the test')