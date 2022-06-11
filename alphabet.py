from termcolor import colored

global alph
global lst
global lst_new
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lst = list(alph)
lst_new = list(alph)

def alphabet(choice):
    lst_word = list(choice)
    for v in lst_word:
        ind = (lst_new.index(v))
        lst[ind] = colored(str(v),'blue')
    return "".join(lst)