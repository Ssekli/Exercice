#réaliser un quizz



'''print("Quelle est la devise américaine  ? ")
print("a : Dollar")
print("b : Euro")
print("c : Livre")
print("d : Deutschmark")
answer = input("Votre réponse :")
if answer == "a" :
    print("Bonne réponse")
else :
    print("Mauvaise réponse")


print("Que signifie H2O ? ")
print("a : Eau")
print("b : Pastis")
print("c : Acide chloridrique")
print("d : Dunkerque")
answer = input("Votre réponse :")
if answer == "c" :
    print("Bonne réponse")
else :
    print("Mauvaise réponse")'''


def ask_questions(question, a1, a2, a3, a4, right_choice) :
    global score
    print("Question :", question)
    print("a :", a1)
    print("b :", a2)
    print("c :", a3)
    print("d :", a4)
    answer = input("Votre réponse :")
    right_answer = False
    if answer == right_choice :
        print("Bonne réponse")
        score += 1
    else :
        print("Mauvaise réponse")

    print() #reachable car pas de return avt
    


score = 0 
ask_questions("Quelle est la capitale de la France ? ","Marseille", "Lille","Paris", "Dunkerque", "c" )
ask_questions("Quelle est la capitale de l'Italie' ? ", "Vienne", "Rome", "Turin", "Dunkerque", "b")

print("Votre score est:", score)