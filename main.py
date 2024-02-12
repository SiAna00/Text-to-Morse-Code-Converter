morse_code = {"a" : ".-", 
              "b" : "-...", 
              "c" : "-.-.", 
              "d" : "-..", 
              "e" : ".", 
              "f" : "..-.", 
              "g" : "--.", 
              "h" : "....", 
              "i" : "..", 
              "j" : ".---", 
              "k" : "-.-", 
              "l" : ".-..", 
              "m" : "--", 
              "n" : "-.",
              "o" : "---",
              "p" : ".--.",
              "q" : "--.-",
              "r" : ".-.",
              "s" : "...",
              "t" : "-",
              "u" : "..-",
              "v" : "...-",
              "w" : ".--",
              "x" : "-..-",
              "y" : "-.--",
              "z" : "--..",
              0 : "-----",
              1 : ".----",
              2 : "..---",
              3 : "...--",
              4 : "....-",
              5 : ".....",
              6 : "-....",
              7 : "--...",
              8 : "---..",
              9 : "----.",
              "." : ".-.-.-",
              "," : "--..--",
              "?" : "..--..",
              "!" : "-.-.--",
              " " : " "
              }

print("Welcome to 'Latin to Morse Code' Converter")

phrase = (input("Enter a word or a phrase you would like to convert to Morse code:\n")).lower()

phrase_morse = ""

for character in phrase:
    for key in morse_code:
        if character == key:
            phrase_morse += morse_code[key]

print(phrase_morse)