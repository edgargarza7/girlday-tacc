from microbit import *

# Define a function that can perform the 'shift' of letters in the alphabet
def shift_letter_encrypt(letter, shift_amount):
    letter_num = ord(letter) - ord('A')
    shifted_letter_num = (letter_num + shift_amount) % 26
    return chr(ord('A') + shifted_letter_num)

# Define a function that encrypts all the letters in a message
def shift_message_encrypt(message, shift_amount):
    shifted_message = " "
    for letter in message:
        shifted_message = shifted_message + shift_letter_encrypt(letter, shift_amount)
    return shifted_message

# Define a function that can perform the 'shift' of letters in the alphabet
def shift_letter_decrypt(letter, shift_amount):
    letter_num = ord(letter) - ord('A')
    shifted_letter_num = (letter_num - shift_amount) % 26
    return chr(ord('A') + shifted_letter_num)

# Define a function that decrypts all the letters in a message
def shift_message_decrypt(message, shift_amount):
    shifted_message = " "
    for letter in message:
        shifted_message = shifted_message + shift_letter_decrypt(letter, shift_amount)
    return shifted_message

# Insert message between the " " below and the number of letters for the shift: 
plaintext = "SECRET"
ciphertext = "VHFUHW"
shift_key = 3
    
# The message will scroll once before the while True loop starts
display.scroll("Press A to encrypt, Press B to decrypt", wait=False, delay=150)
    
while True:
    # press button A to display the shifted message
    if button_a.is_pressed(): 
        display.scroll(str(shift_key), delay=150)
        display.clear()
        sleep(200) 
        display.scroll(shift_message_encrypt(plaintext, shift_key), wait=False, delay=150)
    elif button_b.is_pressed(): 
        display.scroll(str(shift_key), delay=150)
        display.clear()
        sleep(200) 
        display.scroll(shift_message_decrypt(ciphertext, shift_key), wait=False, delay=150)
