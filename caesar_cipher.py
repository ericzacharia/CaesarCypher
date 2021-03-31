import sys


def character_shift(letter, shift):  # Shifts a single character
    letter_ascii = ord(letter)
    shift %= 26
    shifted_letter_ascii = letter_ascii + shift
    if ord('a') <= letter_ascii <= ord('z') and ord('z') < shifted_letter_ascii:
        shifted_letter_ascii -= 26
        shifted_letter = chr(shifted_letter_ascii)
    elif ord('A') <= letter_ascii <= ord('Z') and ord('Z') < shifted_letter_ascii:
        shifted_letter_ascii -= 26
        shifted_letter = chr(shifted_letter_ascii)
    elif ord('A') > letter_ascii > ord('Z') or ord('a') > letter_ascii > ord('z'):
        return letter
    elif ord('A') <= letter_ascii <= ord('Z') or ord('a') <= letter_ascii <= ord('z'):
        shifted_letter = chr(shifted_letter_ascii)
    else:
        return letter
    # print(f'The original letter {letter} was encrypted to {shifted_letter} using a shift of {shift}.')
    return shifted_letter


# key = 3
# print(character_shift(input('Enter a letter: '), key))
if sys.argv[2] == '-d':
    key = -int(sys.argv[1])
    input_file = sys.argv[3]
    output_file = sys.argv[4]
elif sys.argv[2] == '-e':
    key = int(sys.argv[1])
    input_file = sys.argv[2]
    output_file = sys.argv[3]
else:
    key = int(sys.argv[1])
    input_file = sys.argv[2]
    output_file = sys.argv[3]

with open(output_file, "w") as file:
    with open(input_file, 'r') as f:  # with automatically closes the .txt file at the end
        for line in f:
            for char in line:
                char = character_shift(char, key)
                file.write(char)
