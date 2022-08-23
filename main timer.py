from asyncio.events import BaseDefaultEventLoopPolicy
import time


def cooking_choices() :
    cook = False
    while cook == False :
        cook = input("Quelle cuisson voulez vous ? Tapez 1 pour à la coque, 2 pour mollets et 3 pour durs")
        if cook == 1 :
            duration = 3
            cook = True
        elif cook == 2 :
            duration = 6
            cook = True
        elif cook == 3 :
            duration = 9
            cook = True
        else :
            print("Erreur, entrez 1, 2 ou 3 selon votre cuisson(respectivement coque, mollets et durs")
    
    cooking_time = duration * 60
    return cooking_time


def timer(cooking_time) :
    while cooking_time :
        for i in range(10) :
            time.sleep(1)
            print(".", end="", flush=True)
        minutes = cooking_time//60
        secondes = cooking_time-minutes*60
        cooking_time -= 10
        print(f"{minutes:02d}:{secondes:02d}")

    
        
        
    print("Cuisson terminée")
            
            

cooking_time = cooking_choices()
timer(cooking_time)