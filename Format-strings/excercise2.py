message = str.capitalize('first message')
print(message)

message = 'second message'.capitalize()
print(message)

message = 'third message'
print(message.capitalize())

message = 'hello world'
print(message.lower())
print(message.upper())
message = message.title()
print(message)
print(message.swapcase())

message = 'The quick brown fox jumps over the lazy dog'
print(message.find('q'))

print(message.find('t'))
print(message.find('T'))

message = '    middle     '
print('.' + message.lstrip() + '.')
print('.' + message.rstrip() + '.')
print('.' + message.strip() + '.')

message = 'brevity is the essence of wit'
message = message.replace('essence', 'soul')
print(message)