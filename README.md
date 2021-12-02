Lab 10


Problem
The file morsecode.txt (accompanying this handout) contains the Morse code translation for letters A to Z, digits 0 to 9, and some punctuation symbols. Write a program that loads this file into a dictionary obect that maps Morse code symbols to their corresponding letter, digit, or punctuation symbol. The program should then ask the user for the name of a file containing Morse code and, using the dictionary, decode its contents to the console. Use the files morse1.txt, morse2.txt, and morse3.txt (accopanying this handout) to test your program.

Instructions
Create a new Python file and place intro comments using the template below.
Use comments to write the algorithm your program will follow, including functions.
Write the Python code corresponding to each of your algorithm's steps.
Commit and push changes and check your repository on github.com to confirm your updates before leaving lab (even if not finished).

Note: This lab does not require a flowchart or test cases.

Intro comments template
# Programmers: [your names]
# Course: CS151, Dr. Rajeev 
# Date:
# Lab Number:
# Program Inputs: [What information do you request from the user?]
# Program Outputs: [What information do you display for the user?]
Function decomposition
Your program should have a function for each of the following tasks. Practice iterative development: implement each item according to the instructions section below and then test that your code still works before proceeding onto the next item.

A function load_morse_dictionary which loads the data from the file morsecode.txt, builds a dictionary (mapping morse code to letters, numbers, and punctuation), and returns it.
A function decode_file which, given the morse dictionary and a filename containing morse code lines, decodes the contents of the file to the console. Note: You can use the optional parameter end=”” with your print statement so that it will not include line breaks after each call. When you're ready to print a new line, use print().
A main function to drive the program.
Submission
One submission per team including all member names.

GitHub: Completed .py file (including intro and algorithm comments).
