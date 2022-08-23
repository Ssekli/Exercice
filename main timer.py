from asyncio.events import BaseDefaultEventLoopPolicy
import time


def cooking_choices() :
    duration = 0
    while duration == 0 :
        cook = input("Quelle cuisson voulez vous ? (coque, mollets ou durs)")
        if cook == "coque" :
            duration = 3
        elif cook == "mollets" :
            duration = 6
        elif cook == "durs" :
            duration = 9
    
    cooking_time = duration * 60
    return cooking_time


def timer(cooking_time) :
    while cooking_time :
        
        minutes = cooking_time//60
        secondes = cooking_time-minutes*60
        cooking_time -= 10
        print(f"{minutes:02d}:{secondes:02d}")
        for i in range(10) :
            time.sleep(1)
            print(".", end="", flush=True)
        
        

    print("Cuisson terminée")
            
            

cooking_time = cooking_choices()
timer(cooking_time)





    


