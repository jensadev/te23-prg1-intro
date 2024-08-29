print("Hej och välkommen till mitt program!")
user_name = input("Skriv ditt namn: ")
print(f"Hej {user_name}! Vad kul att du är här!")

print("Jag undrar hur gammal du är?")
user_age = input("Skriv din ålder i år: ")
print(f"Tack, vad fint att du är {user_age} år ung.")

# konvertera user_age till int innan matte
user_age_converted = int(user_age)
if user_age_converted >= 15: # > =
    print("Du får köra moppen.")
else:
    print("😡")