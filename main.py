import random
import time
from rich.prompt import Prompt
from rich import print
from words import Words
from leaderboard import lb
from termcolor import cprint


class Wordle:

    def __init__(self,mode):

        self.word_six = random.choice(Words.Words_Six())
        self.word_five = random.choice(Words.Words_Five())
        self.word_four = random.choice(Words.Words_Four())
        self.start_time = time.time()
        self.mode = mode
        if self.mode == "2":
            self.time = 120

    def out_of_time(self):
        # timer for hard mode
        end_time = time.time()
        if end_time - self.start_time >= 120:
            print("You are out of time!")
            self.game_over()
            quit()

    def user_guess(self, remaining, diff):
        # gets proper input from user
        if diff == '4':
            user_input = Prompt.ask(f"\nEnter your first guess({remaining} guesses remaining)")
            self.choice = user_input.upper()
            self.remaining = remaining
            if len(user_input) != 4:
                print("Enter a 4-lettered word.")
                self.user_guess(remaining, diff)
            elif user_input.upper() not in Words.Words_Four():
                print("Enter a valid word.")
                self.user_guess(remaining, diff)
            if self.choice == self.word_four:
                print("You have won! The word was:")
                cprint(f"     {self.word_four}    ", 'green')
                end_time = time.time()
                score = self.rating(end_time - self.start_time)
                lb(0, score, self.word_four, 6 - remaining, self.mode)
                print("Your rating for this wordle is: {:.2f}".format(score))
                quit()
            return self.choice

        if diff == '5':
            user_input = Prompt.ask(f"\nEnter your first guess({remaining} guesses remaining)")
            self.choice = user_input.upper()
            self.remaining = remaining
            if len(user_input) != 5:
                print("Enter a 5-lettered word.")
                self.user_guess(remaining,diff)
            elif user_input.upper() not in Words.Words_Five():
                print("Enter a valid word.")
                self.user_guess(remaining,diff)
            if self.choice == self.word_five:
                print("You have won! The word was:")
                cprint(f"     {self.word_five}    ",'green' )
                end_time = time.time()
                score = self.rating(end_time - self.start_time)
                lb(0, score, self.word_five, 6-remaining,self.mode)
                print("Your rating for this wordle is: {:.2f}".format(score))
                quit()
            return self.choice
        elif diff == '6':
            user_input = Prompt.ask(f"\nEnter your first guess({remaining} guesses remaining)")
            self.choice = user_input.upper()
            self.remaining = remaining
            if len(user_input) != 6:
                print("Enter a 6-lettered word.")
                self.user_guess(remaining,diff)
            elif user_input.upper() not in Words.Words_Six():
                print("Enter a valid word.")
                self.user_guess(remaining,diff)
            if self.choice == self.word_six:
                print("You have won! The word was)")
                cprint(f"     {self.word_six}     ","green")
                end_time = time.time()
                score = self.rating(end_time - self.start_time)
                lb(0, score, self.word_six, 6-remaining,self.mode)
                print("Your rating for this wordle is: {:.2f}".format(score))
                quit()
            return self.choice

    def color(self,us_input):
        #coloring of the matching letters. green for same place, yellow for wrong place but is in word.
        lst = []
        if len(us_input) == 6:
            for i in range(len(us_input)):
                if us_input[i] == self.word_six[i]:
                    lst.append(f'\033[32m{us_input[i]}\033[39m')
                elif us_input[i] in self.word_six:
                    if us_input.count(us_input[i]) > 1:
                        lst.append(f'{us_input[i]}')
                    else:
                        lst.append(f'\033[33m{us_input[i]}\033[39m')
                else:
                    lst.append(f'{us_input[i]}')
            self.lst = lst
            if self.mode == "2":
                b_time = time.time()
                print("{:.2f} seconds remaining".format(self.time - (b_time - self.start_time)))
            return lst
        elif len(us_input) == 5:
            for i in range(len(us_input)):
                if us_input[i] == self.word_five[i]:
                    lst.append(f'\033[32m{us_input[i]}\033[39m')
                elif us_input[i] in self.word_five:
                    if us_input.count(us_input[i]) > 1:
                        lst.append(f'{us_input[i]}')
                    else:
                        lst.append(f'\033[33m{us_input[i]}\033[39m')

                else:
                    lst.append(f'{us_input[i]}')
            self.lst = lst
            if self.mode == "2":
                b_time = time.time()
                if (self.time - (b_time - self.start_time)) <= 0:
                    print("{:.2f} seconds remaining".format(0))
                else:
                    print("{:.2f} seconds remaining".format(self.time - (b_time - self.start_time)))
            return lst

        elif len(us_input) == 4:
            for i in range(len(us_input)):
                if us_input[i] == self.word_four[i]:
                    lst.append(f'\033[32m{us_input[i]}\033[39m')
                elif us_input[i] in self.word_four:
                    if us_input.count(us_input[i]) > 1:
                        lst.append(f'{us_input[i]}')
                    else:
                        lst.append(f'\033[33m{us_input[i]}\033[39m')

                else:
                    lst.append(f'{us_input[i]}')
            self.lst = lst
            if self.mode == "2":
                b_time = time.time()
                print("{:.2f} seconds remaining".format(self.time - (b_time - self.start_time)))
            return lst



    def game_over(self):
        if len(self.choice) == 5:
            print('\nGame is over! The word was:')
            cprint(f"    {self.word_five}","red")
        elif len(self.choice) == 6:
            print('\nGame is over! The word was:')
            cprint(f"    {self.word_six}","red")
        elif len(self.choice) == 4:
            print('\nGame is over! The word was:')
            cprint(f"    {self.word_four}","red")
        exit()

    def rating(self, time):
        # magical numbers for rating calculation. bigger means better.
        chance_spent = 6 - (self.remaining-1)
        return (((1/(chance_spent*time))**(1/2))*(2**int(self.mode)))*10


