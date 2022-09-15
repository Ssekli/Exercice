#pizzas = ("4 fromages", "picante", "tuna", "reine")
pizzas =()
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