# Programmers: Aidan, Nicol
# Course: CS151, Dr. Rajeev
# Date: 12/02/2021
# Lab Number: 10
# Program Inputs: Morse code file
# Program Outputs: Translated morse code

# Problem The file morsecode.txt (accompanying this handout) contains the Morse code translation for letters A to Z,
# digits 0 to 9, and some punctuation symbols. Write a program that loads this file into a dictionary obect that maps
# Morse code symbols to their corresponding letter, digit, or punctuation symbol. The program should then ask the user
# for the name of a file containing Morse code and, using the dictionary, decode its contents to the console. Use the
# files morse1.txt, morse2.txt, and morse3.txt (accopanying this handout) to test your program.

# A function load_morse_dictionary which loads the data from the file morsecode.txt, builds a dictionary (mapping morse
# code to letters, numbers, and punctuation), and returns it.

# A function decode_file which, given the morse dictionary and a filename containing morse code lines, decodes the
# contents of the file to the console. Note: You can use the optional parameter end=”” with your print statement so
# that it will not include line breaks after each call. When you're ready to print a new line, use print().

# A main function to drive the program. Submission One submission per team including all member names.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this function reads the morsecode.txt and creates a dictionary
def load_morse_dictionary():
    morse_dict = {}
    file = open("morsecode.txt", "r")
    for line in file:
        key, value = line.split()
        morse_dict[key] = value
    return morse_dict

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function to decode the coded string
def decode_file(filename, morse_code_dict):
    coded = ""
    # reverse the key and value pairs of dict
    morse_code_dict = dict(map(reversed, morse_code_dict.items()))
    # read the file of morse coded string
    file = open(filename, "r")
    for line in file:
        # merges characters
        coded += line.rstrip() + "  "
    decipher = ''
    text = ''
    for letter in coded:
        # checks for space
        if (letter != ' '):
            i = 0
            text += letter
        else:
            # new character
            i += 1
            # new word
            if i == 2:
                # adding space to separate words
                decipher += ' '
            else:
                # accessing the keys using their values
                decipher += morse_code_dict[text]
                text = ''
    return decipher

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# main function to run the program
def main():
    morse = load_morse_dictionary()
    print("a. 'morse1.txt'")
    print("b. 'morse2.txt'")
    print("c. 'morse3.txt'")
    filename = input("What file would you like to be decoded")
    if filename == 'a'.strip().lower():
        filename = 'morse1.txt'
    elif filename == 'b'.strip().lower():
        filename = 'morse2.txt'
    elif filename == 'c'.strip().lower():
        filename = 'morse3.txt'
    else:
        print("Invalid option")

    result = decode_file(filename, morse)
    print(result)

main()