# Reverse Guessing - makes the computer guess the number user input
#momor

from tkinter import *
import random  # to generate random numbers

# max and min that will change
Max = 100
Min = 1

global secret_number
global guess
# GUI
root = Tk()


# functions
def g_entry():
    global secret_number, guess
    secret_number = int(guessE.get())
    guess = random.randint(Min, Max)
    guess_l = Label(root, text='Is ' + str(guess) + ' your number?')
    guess_l.pack()


def g_lower():
    global guess, Max, Min
    Max = guess
    guess = int((guess + Min) / 2)
    guess_l = Label(root, text='Is ' + str(guess) + ' your number?')
    guess_l.pack()


def g_higher():
    global guess, Max, Min
    Min = guess
    guess = int((guess + Max) / 2)
    guess_l = Label(root, text='Is ' + str(guess) + ' your number?')
    guess_l.pack()


def g_yes():
    yes_l = Label(root, text='Hooray, I won!')
    yes_l.pack()


# input box
guessE = Entry(root, width=50)
guessE.pack()
guessE.insert(0, 'Enter a number between 1 and 100')

# buttons
guessButton = Button(root, text='Guess', command=g_entry).pack()
exitButton = Button(root, text='Exit', command=exit).pack()

yesButton = Button(root, text='Yes', command=g_yes).pack()
hButton = Button(root, text='Higher', command=g_higher).pack()
lButton = Button(root, text='Lower', command=g_lower).pack()

#launch
root.mainloop()