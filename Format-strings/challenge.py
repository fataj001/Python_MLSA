first_value = '  FIRST challenge         '.capitalize()
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'.capitalize()

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge



# Second challenge


# Third challenge


print(first_value.rjust(20))
print(second_value.lstrip())
print(third_value)


print(fourth_value, fifth_value, sixth_value, sep='#', end='!')

# Fourth challenge - use only the print() function (no f-strings)
print( '\n'+fourth_value.rjust(14))

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(' \t' + fifth_value)
print('\t' + sixth_value)