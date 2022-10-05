import string
#to import the string module
alphabets = string.ascii_lowercase + string.ascii_lowercase
#allows us to accomodate for the lowercase letters (1 to 25) also i cant be bothered to write the alphabet
sentence = list(input('enter your text: ').lower())
#this is going to be responsibile for holding the text which needs to be encrypted or decrypted
instructions = input('enter encrypt to ENCRYPT, decrypt to DECRYPT: ').lower()
shift_number = int(input('enter your shift number from 1 to 25: ').lower())
end_program = False
#the program will continue to run until the program has the boolean value of True
while not end_program:
    #search through the enter text
    if instructions == 'encrypt':
        for i in range(len(sentence)):
        #this is going to tell us how long we need the for loop to run
        #next we need to get the position of each character within the sentence
            if sentence[i] == ' ':
            #to check if the spacebar was used
                sentence[i] = ' '
            #i want to replace it with a value of an empty string so i can keep it there
            else:
                new_letter = alphabets.index(sentence[i]) + shift_number
                sentence[i] = alphabets[new_letter]
        #convert the list back into a string
        print(''.join(map(str,sentence)))
        end_program = True
    elif instructions == 'decrypt':
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                sentence[i] = ' '
            #this is the same as encryption so just copy and paste
            else:
                new_letter = alphabets.index(sentence[i]) - shift_number
                #again copy and paste but minus instead of plus so we are moving backwards
                sentence[i] = alphabets[new_letter]
                #need to convert the list back to a string so copy and paste
        print(''.join(map(str,sentence)))
        end_program = True
    else:
        decide = input('invalid entry, try again. Y for YES, N for NO: ').lower()
        #this is incase the user inputs anything other than encrypt or decrypt then we display this message
        if decide == 'y':
            sentence = list(input('enter your text: ').lower())
            instructions = input('enter encrypt to ENCRYPT, decrypt to DECRYPT: ').lower()
            shift_number = int(input('enter your shift number from 1 to 25: ').lower())
        else:
            end_program = True