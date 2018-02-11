alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''

message = str(raw_input('Please enter a message: '))

key = input('Enter a key (1-26): ')
key = int(key)

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        #moving each alphabet by key. e.g. a, key:3, new char: a+3 = d
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character

print('Your new message is: ', newMessage)