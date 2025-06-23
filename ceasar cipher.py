alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("type  'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("tpye your message:\n").lower()

shift = int(input("type the shift number:\n"))
#first create a function  called 'encrypt' that takes the "text" and "shift" as inputs.

#combine the encrypt and decrypt funtions into a single function called ceasar


#if a user type a number that is higher than the alphabet

shift = shift % 26

def ceasar(start_text , shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f" the {cipher_direction}d text is {end_text}")

ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)











