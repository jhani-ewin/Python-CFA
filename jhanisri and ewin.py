#!/usr/bin/env python

import random

def main():
    """Start a music guessing game."""
    print("Welcome to the music instrument guessing game!")
    answer=input('Are you ready to play the Quiz? (YES/NO) :')
    score =0
    total_questions=5

    if answer.lower()=='yes':

           answer =input('Question 1: which music instrument is louder? ~ PIPE ORGAN OR VIOLIN =')
    if answer.lower()=='pipe organ':
            score += 1
            print('wow...its correct')
    else:
            print('oops...its wrong')
           
        
    answer =input('Question 2: From this both which music instrument is big and have keyboard to play? ~ GUITAR OR PIANO =')
    if answer.lower()=='piano':
            score += 1
            print('wow...its correct')
    else:
            print('oops...its wrong')


    answer =input('Question 3: Guess the music instrument? [DR_M] =')
    if answer.lower()=='drum':
            score += 1
            print('wow...its correct')
    else:
           print('oops...its wrong')


    answer =input('Question 4: Guess the music instrument? [FL_TE] =')
    if answer.lower()=='flute':
            score += 1
            print('wow its correct')
    else:
           print('oops...its wrong')


    answer =input('Question 5: Guess the music instrument? [G_IT_R] =')
    if answer.lower()=='guitar':
            score += 1
            print('perfect..you got it right')
    else:
           print('oops...sorry,you got it wrong')  

    print('Thank you for playing this small game, hope you enjoyed.You attempted',score,"questions correctly!")
    mark=(score/total_questions)*100
    print('marks obtained:',mark)
    print('Thats all!...bye,see you again!')
main()


