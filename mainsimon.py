#Jeu qui génère des chiffres aléatoires, 3s de mémorisation, a chaque bon résultat ajoute 1 chiffre.
#Erreur on arrete et donne le score.

from operator import add
import os
import time
import random

TIME = 3

def clear_screen() :
    if(os.name == "posix"):
        os.system("clear")
    else:
        os.system("cls")


def start() :
    return str(random.randint(0, 9))


def chain() :
    startnb = start()+start()
    score = 0 
    while True:
        print("Retenez la séquence")
        time.sleep(1)

        startnb += start()

        print (startnb)
        time.sleep(3)

        clear_screen()

        answer = input("Quelle est votre réponse ?")
        if answer == startnb :
            score += 1
            print(f"Votre score : {score}")

        else :
            print(f"mauvaise réponse, c'etait {startnb}")
            print(f"Votre score est {score}")
            exit()


start()
chain()