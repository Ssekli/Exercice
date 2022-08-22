# faire un convertisseur livre / pouce avec question d'entrée.

from ast import While
from re import A


def cm_to_inch() :
   answer_str = input("Quelle est votre valeur à convertir de cm vers inch ?")
   answer_int = int(answer_str)
   conversion = answer_int * 0.394

   print(f"{conversion} inch")

def inch_to_cm() :
    answer_str = input("Quelle est votre valeur à convertir de inch vers cm ? ")
    answer_int = int(answer_str)
    conversion = answer_int * 2.54

    print(f"{conversion} cm")



def Question() :
    conv = 0
    while conv == 0 :
        conv_str = input("Que voulez vous faire ? Convertir cm en inch (taper 1) Convertir inch en cm (Taper 2)")
        try :
            conv = int(conv_str)
        except ValueError :
            print("Entrez 1 ou 2")
    
        if conv ==1 :
                cm_to_inch()
        elif conv ==2 :
                inch_to_cm()

    


Question()
continuer = True   
while continuer:
    choix = input("Voulez-vous continuer ? (Taper Oui pour continuer)")
    if choix not in ("Oui", "oui" ):
        continuer = False
    if continuer == True:
        Question()
