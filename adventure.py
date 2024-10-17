# Äventyret sparar vilken runda det är och du har 10 liv,
# du får 1 poäng för varje runda du klarar
# Du är en gullig liten äventyrare som är ute och promenerar i vildmarken.
# I din påse har du en karta över området och en kompass.
# inventory = ["karta", "kompass"]
# Du kan välja att titta i din påse, promenera vidare eller löka
# Om du tittar i din påse får du reda på vad du har med dig
# Om du promenerar vidare så fortsätter du din vandring
# Om du lökar så står du stilla och tittar dig omkring
# När du lökar finns det en 50% chans att du hittar något spännande
# items = ["vättejos", "kantarell", "ekorre", "sten"]
# random.choice(items)
# det finns även en 20% chans att du möter en person på din vandring
  # Stinkande socka - En socka som luktar så illa att den kan skrämma bort en vätte.
  # Effekt: Skrämmer bort en vätte, +1 poäng.
  # Mystisk svamp - En svamp som kan ha oväntade effekter.
  # Effekt: 50% chans att bli mätt och få 1 liv, 50% chans att bli sjuk och förlora 1 liv.
  # Gammal ostbit - En ostbit som har legat ute alldeles för länge.
  # Effekt: Om du äter den, blir du sjuk och förlorar 1 liv.
  # Trasig trollstav - En trollstav som inte fungerar längre.
  # Effekt: Ingen direkt effekt, men kan användas för att imponera på en person du möter, +1 poäng.
  # Borttappad strumpa - En ensam strumpa som någon har tappat.
  # Effekt: Ingen direkt effekt, men kan användas för att byta till sig något från en person du möter.
# Om du möter en person och är smittad av vätte så kan du bita personen och
# förvandla dem till en vätte, -10 poäng
# du landar i den mörka sidan och spelet är över
# Vad väljer du att göra?
# Det är en 50% chans att du möter en vätte på din vandring
# Plötsligt möter du en ondskefull vätte, de är väldigt fega, farliga och hemska
# Vätten närmar sig hotfull, vad väljer du att göra?
# Du kan här använda ett föremål om du har det i din påse
# Se föremål i påsen
# Du kan också försöka att kommunicera med vätten
# Bekämpa vätten med pathos, logos och ethos alltså på svenska med känslor, logik och etik
# logik besegrar känslor, du trasslar in vätten i en logisk diskussion och kan smita förbi
  # +1 poäng för att du klarade dig förbi vätten
# etik besegrar logik, vätte imponeras av din moral och ger dig en gåva
  # +1 poäng för att du klarade dig förbi vätten
  # du får en slumpad gåva från vätten
    # [ Magisk svamp - En svamp som kan få dig att se världen i olika färger eller ge
    # dig tillfälliga krafter.
    # Osynlighetsmantel - En mantel som gör dig osynlig för en kort stund,
    # perfekt för att smyga förbi faror.
    # sten - En mystisk sten som du kan prata med och berätta dina hemligheter för.
    # Den svarar aldrig, men det känns ändå som att den lyssnar. Kanske är det bara
    # du som är lite konstig, men det är ändå skönt att ha någon att prata med i vildmarken. ]
# Känslor besegrar etik, känslorna tar över och vätten blir arg och biter dig, spring!
  # Du har blivit biten av vätten, vättar är giftiga, du kommer att förvandlas
  # till en vätte om 3 rundor
# Det är oavgjort, du tänker så hårt att du får huvudvärk
  # -1 liv
  # Du tycker verkligen inte om oförskämda vättar

# Du har klarat dig förbi vätten och kan fortsätta din vandring

import random

def random_choice():
    choice = random.randint(0, 100)
    if choice <= 50:
        return 0
    elif choice <= 70:
        return 1
    else:
        return 2

# The patos logos and ethos function is a rock paper scissors game where logic
# beats emotions, ethics beats logic and emotions beats ethics

def patos_logos_ethos():
    choice = random.randint(0, 2)
    if choice == 0:
        return "logik"
    elif choice == 1:
        return "etik"
    else:
        return "känslor"

# Vi kan introducera dict för att spara information om föremål
items = {
    "vättejos": "blir du sjuk och förlorar 1 liv",
    "kantarell": "blir du mätt och får 1 liv",
    "ekorre": "är du moraliskt tvivelaktig och förlorar 1 poäng",
    "sten": "bryter du dina tänder och förlorar 1 liv",
    "stinkande socka": "skrämmer bort en vätte, +1 poäng"
}

# Exempel på hur man kan använda dictionaries
for item, effect in items.items():
    print(f"Om du äter {item} så {effect}")


items = [
    ("vättejos", "blir du sjuk och förlorar 1 liv", "test"),
    ("kantarell", "blir du mätt och får 1 liv"),
    ("ekorre", "är du moraliskt tvivelaktig och förlorar 1 poäng"),
    ("sten", "bryter du dina tänder och förlorar 1 liv"),
    ("stinkande socka", "skrämmer bort en vätte, +1 poäng")
]

# Exempel på hur man kan använda tuples
for item in items:
    print(f"Om du äter {item[0]} så {item[1]}")


items = [
    ["vättejos", "blir du sjuk och förlorar 1 liv"],
    ["kantarell", "blir du mätt och får 1 liv"],
    ["ekorre", "är du moraliskt tvivelaktig och förlorar 1 poäng"],
    ["sten", "bryter du dina tänder och förlorar 1 liv"],
    ["stinkande socka", "skrämmer bort en vätte, +1 poäng"]
]

# Exempel på hur man kan använda listor
for item in items:
    name = item[0]
    effect = item[1]
    print(f"Om du äter {name} så {effect}")


items = [
    {"name": "vättejos", "effect": "blir du sjuk och förlorar 1 liv"},
    {"name": "kantarell", "effect": "blir du mätt och får 1 liv"},
    {"name": "ekorre", "effect": "är du moraliskt tvivelaktig och förlorar 1 poäng"},
    {"name": "sten", "effect": "bryter du dina tänder och förlorar 1 liv"},
    {"name": "stinkande socka", "effect": "skrämmer bort en vätte, +1 poäng"}
]


  
items.append({"name": "mystisk svamp", "effect": "50% chans att bli mätt och få 1 liv, 50% chans att bli sjuk och förlora 1 liv"})

# Exempel på hur man kan använda listor av dictionaries
for item in items:
    print(f"Om du äter {item['name']} så {item['effect']}")

found = random.choice(items)
print(found)