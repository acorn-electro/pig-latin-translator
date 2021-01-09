# Pig Latin Translator
# Accept text from the user and translate it to Pig Latin
# Rules:
#    - If the word starts with a consonant, move the first letter to the end and add 'ay' (dog -> ogday)
#    - If the word starts with multiple consonants, move the cluster to the end and add 'ay' (string -> ingstray)
#    - If the word starts with a vowel, add 'yay' to the end (eat -> eatay)

import re, sys

vowels = "aeiouAEIOU"

while True:
    try:
        text = input("Enter the text to translate: ")
        # Split the text into a list of words and spaces/punctuation between them
        words = re.split(r'(\W+)', text)
        
        for i in range(len(words)):
            word = words[i]
            # Skip over spaces and punctuation
            if not word.isalnum():
                continue
            
            if len(word) <= 1 or word[0] in vowels:
                word = word + "yay"
            else:
                # Handle multiple consonants at beginning of word
                clusterEnd = 1
                for j in range(1, len(word)):
                    if word[j] in vowels:
                        clusterEnd = j
                        break
                word = word[clusterEnd:] + word[0:clusterEnd].lower() + "ay"
                
            # Handle capitalization
            if len(words[i]) > 1 and words[i].isupper():
                word = word.upper()
            elif words[i].istitle():
                word = word.title()
            words[i] = word
            
        print("".join(words))
        
        
    except KeyboardInterrupt or EOFError:
        sys.exit()
        