from asyncio.events import BaseDefaultEventLoopPolicy
import time


def cooking_choices() :
    duration = 0
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
        min_sec_format = "{:02d}:{02d}". format(minutes, secondes)
        for i in range(10) :
            time.sleep(1)
            print(min_sec_format, end="", flush=True)
        print(min_sec_format, end='/r')
    print("Cuisson terminée")
            
            

cooking_time = cooking_choices()
timer(cooking_time)





    


