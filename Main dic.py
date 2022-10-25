"""personne = {"name" : "Bob", "age": 25, "height": 1.60}

personne["poste"] = "dev"

print(personne)

personnes = [
    ("melanie", 35, 1.56 ),
    ("paul", 23, 1.78),
    ("Jacques", 35, 1.98)
]

def iteration (name, list) :
    for i in list:
        if i[0] == name:
            return i
    return None

infos = iteration("Jacques", personnes)
print(infos)"""

# diction associer clé aux valeurs

persons_dictionary = {
    "melanie" (35, 1.56 ),
    "paul" (23, 1.78),
    "Jacques" (35, 1.98)
}

infos = persons_dictionary.get("Jacques") #.get permet de pas sortir erreur si clé existe pas
print(infos)

#  dictionnaire plus efficca car clé moins de cpu