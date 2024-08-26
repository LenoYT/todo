import json
import os

def create(n, name, desc, data):
    if n not in data["TODO"]:
        data["TODO"][n] = {}
    
    data["TODO"][n][name] = {
        "name": name,
        "description": desc
    }
    
    with open('db.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"Element '{name}' został dodany do sekcji '{n}'.")

def move(fro, to, what, data):
    if fro in data["TODO"] and what in data["TODO"][fro]:
        item = data["TODO"][fro][what]

        if to not in data["TODO"]:
            data["TODO"][to] = {}
        
        data["TODO"][to][what] = item
        
        del data["TODO"][fro][what]
        if not data["TODO"][fro]:
            pass

        with open('db.json', 'w') as file:
            json.dump(data, file, indent=4)

        print("Dane zostały przeniesione i zapisane.")
    else:
        print(f"Brak danych do przeniesienia z {fro} lub {what} nie istnieje.")

def show(n, data):
    if "TODO" in data and n in data["TODO"]:
        section = data["TODO"][n]
        
        for key, value in section.items():
            print(f"\n\nElement: {key}")
            print(f"Name: {value.get('name', 'Brak danych')}")
            print(f"Description: {value.get('description', 'Brak danych')}")
    else:
        print(f"Brak sekcji '{n}' w danych.")


while True:
    os.system("cls")
    with open('db.json', 'r') as file:
        data = json.load(file)
    print("\n1. Move From A to B\n2. Show all elements in A\n3. Create TODO")

    try:
        option = int(input("\nOPT > "))

        if option == 1:
            fro = str(input("\nFROM > "))
            to = str(input("\nTO > "))
            what = str(input("\nWHAT > "))
            move(fro, to, what, data)
        elif option == 2:
            n = str(input("\nun/do > "))
            show(n, data)
        elif option == 3:
            n = str(input("\nun/do > "))
            name = str(input("\nNAME > "))
            desc = str(input("\nDESC > "))
            create(n, name, desc, data)
    except ValueError:
        print("Wprowadź poprawny numer opcji.")
    
    wait = str(input("\n\n\nPress Enter to continue..."))
