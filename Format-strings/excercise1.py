first_string = 'A literal string'
second_string = "A literal string"
print(second_string == first_string)


third_string = 'A single quoted literal string with a " double quote'
fourth_string = "A double quoted literal string with a ' single quote"
print(third_string)
print(fourth_string)

fifth_string = 'A single quoted literal string with an \' escaped single quote'
sixth_string = "A double quoted literal string with a \" double quote"
seventh_string = 'A literal string with a \n new line character'
eighth_string = 'A literal string with a \t tab character'

print(fifth_string)
print(sixth_string)
print(seventh_string)
print(eighth_string)

nineth_string = r"A literal string with a \n new line character printed raw"

print(nineth_string)