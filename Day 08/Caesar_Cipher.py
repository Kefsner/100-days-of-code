from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encrypted_list = []


def caesar(input_text, input_shift, input_direction):
    if input_direction == "encode":
        for n in input_text:
            if n in alphabet:
                encrypted_list.append(alphabet[alphabet.index(n) + input_shift])
            else:
                encrypted_list.append(n)
        print(f'The encoded text is {"".join(encrypted_list)}')

    elif input_direction == "decode":
        for n in input_text:
            if n in alphabet:
                encrypted_list.append(alphabet[alphabet.index(n) - input_shift])
            else:
                encrypted_list.append(n)
        print(f'The decoded text is {"".join(encrypted_list)}')


print(logo)

direction = ""
should_end = False
correct_direction_input = False

while not should_end:
    while not correct_direction_input:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction != "encode" and direction != "decode":
            print('Please type only "encode" or "decode".')
        else:
            correct_direction_input = True

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    caesar(input_text=text, input_shift=shift, input_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye!")
    else:
        correct_direction_input = False
        encrypted_list = []
