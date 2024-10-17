print("Välkommen till det bästa programmet, där du sparar mat")
run = True
dishes = ["Tryffelsvin", "Gurksuffle", "Panikalladåb", "Saftsås"] # skapa listan utanför loopen
while run:
    # lägga till ta bort maträtt
    choice = input("Vad vill du göra? \n[1] Skriv ut\n[2] Lägg till mat\n[3] Sortera\n[4] Avsluta\n")
    if choice == "1":
        print("Maträtterna är: ")
        for dish in dishes:
            print(dish)
    elif choice == "2":
        dish = input("Skriv in en ny maträtt: ")
        dishes.append(dish)
    elif choice == "3":
        dishes.sort()
    elif choice == "4":
        run = False
    else:
        print("Jag fattar inte ditt kommando")
