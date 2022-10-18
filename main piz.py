pizzas = ["4 fromages", "picante", "tuna", "reine"]
#pizzas =()

def add_piz() :
    new_pizz = input("ajouter une pizza : ") 
    if new_pizz.lower() in pizzas :
        print("la pizza existe déjà")
    else :
        pizzas.append(new_pizz)

def show_piz() :
    if not pizzas :
        print ("No Pizzas")
    else :
        print(f"--- Number of pizzas {len(pizzas)} ---")
        for i in pizzas :
            print(i)
        print()
        print("1st pizza", pizzas[0])
        print("last pizza", pizzas[-1])

show_piz()
add_piz()
show_piz()
