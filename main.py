
# Text Characters with corresponding Morse Characters
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}
# Initialisation
print("-----Hello To the Text to Morse Code Converter--------")
program_on = True

# Program
while program_on:
    # Getting the user text input
    user_input = input("\nPlease enter the text that you want to convert here: ").upper()
    output = ""

    # Looping on Text Characters to transform them into Morse Characters
    for character in user_input:
        if character in morse_code_dict:
            output += morse_code_dict[character]

    # Showing the Morse Code
    print(f"The corresponding morse Code for your text is: \n{output}")

    # Letting the user decide whether he wants to reuse the program or not
    decision = input("Do you want to convert anything else (YES/NO): ").upper()
    if not decision == "YES":
        program_on = False
