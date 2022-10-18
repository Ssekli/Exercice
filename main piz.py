pizzas = ["4 fromages", "picante", "tuna", "reine"]
#pizzas =()

def add_piz() :
    new_pizz = input("ajouter une pizza : ") 
    if new_pizz.lower() in pizzas :
        print("la pizza existe déjà")
    else :
        pizzas.append(new_pizz)

def show_piz(n_1st=-1) :
    pizzas.sort(key=sorting_order)
   # if n_1st != -1 :
    #    pizzas[0 : n_1st]
    if not pizzas :
        print ("No Pizzas")
    else :
        print(f"--- Number of pizzas {len(pizzas)} ---")
        for i in pizzas :
            print(i)
        print()
        print("1st pizza", pizzas[0])
        print("last pizza", pizzas[-1])

def sorting_order(e) :
    return len(e)

add_piz()
show_piz(2)
