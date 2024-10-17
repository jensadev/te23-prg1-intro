print("Välkommen till det bästa programmet, där du sparar mat")
run = True
while run:
    # lägga till ta bort maträtt
    choice = input("Vad vill du göra? \n[1] Skriv ut\n[2] Lägg till mat\n[3] Avsluta\n")
    if choice == "1":
        print("skriv ut")
        dishes = ["Kroppkakor", "Stroganoff", "Pizza"]
        for dish in dishes:
            print(dish)
    elif choice == "2":
        dish = input("Skriv in en ny maträtt: ")
        dishes.append(dish)
    elif choice == "3":
        run = False
    else:
        print("Jag fattar inte ditt kommando")
