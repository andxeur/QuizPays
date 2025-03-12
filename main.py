import json
import random


# Charger le fichier JSON
with open("pays.json", "r", encoding="utf-8") as file:
    data = json.load(file)

unique_numbers = random.sample(range(0, len(data["pays"])), 5)

victoire = 0

for i in unique_numbers:
    reponse = input(f"Quelle est la capitale de ce pays ? {data['pays'][i]['nom']} : ")
    if reponse == data["pays"][i]["capitale"]:
        victoire += 1
        print("Bravo !")
    else:
        print("Dommage ! La bonne reponse est : ", data["pays"][i]["capitale"])

print(f"Votre score est de {victoire}/5")