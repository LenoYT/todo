import json
import os

def move(fro, to, what, data):
    # Sprawdź, czy sekcja 'fro' i 'what' istnieją w danych
    if fro in data["TODO"] and what in data["TODO"][fro]:
        item = data["TODO"][fro][what]
        
        # Upewnij się, że sekcja 'to' istnieje
        if to not in data["TODO"]:
            data["TODO"][to] = {}
        
        # Dodaj dane do sekcji 'to'
        data["TODO"][to][what] = item
        
        # Usuń dane z sekcji 'fro' tylko jeśli sekcja 'fro' jest teraz pusta
        del data["TODO"][fro][what]
        if not data["TODO"][fro]:
            # Nie usuwaj sekcji 'fro' jeśli jest pusta, bo sekcja 'undo' powinna pozostać
            pass

        # Zapisz zmienione dane do pliku
        with open('db.json', 'w') as file:
            json.dump(data, file, indent=4)

        print("Dane zostały przeniesione i zapisane.")
    else:
        print(f"Brak danych do przeniesienia z {fro} lub {what} nie istnieje.")

def show(n, data):
    # Sprawdź, czy sekcja 'n' istnieje w danych
    if "TODO" in data and n in data["TODO"]:
        section = data["TODO"][n]
        
        # Iteruj przez wszystkie elementy w sekcji
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
    print("\n1. Move From A to B\n2. Show all elements in A")

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
    except ValueError:
        print("Wprowadź poprawny numer opcji.")
    
    wait = str(input("\n\n\nPress Enter to continue..."))
