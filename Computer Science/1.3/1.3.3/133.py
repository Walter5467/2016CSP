from __future__ import print_function # use Python 3.0 printing

def age_limit_output(age):
    '''Step 6a if-else example'''
    AGE_LIMIT = 13   #Caps for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough')
    print('Minimum age is ', AGE_LIMIT)
    
def report_grade(perc):
    if  perc >= 80:
        print('A grade of', perc, 'is great work! Keep it up!')
    else:
        print('A grade of', perc, 'is not good work. Maybe try studying more!')
        
def vowel(letter):
    vowels = 'aeiouAIOU'
    if letter in vowels:
        return True
    else:
        return False
        
def letter_in_word(guess, word):
    if guess in word:
        return True
    else:
        return False
        
def hint(color, secret):
    if color in secret:
        print (color, 'is in the code.')
    else:
        print ('The color', color, 'is not in the code.')
