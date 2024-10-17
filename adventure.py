# äventyret sparar vilken runda det är och du har 10 liv, du får 1 poäng för varje runda du klarar
# Du är en gullig liten äventyrare som är ute och promenerar i vildmarken.
# I din påse har du en karta över området och en kompass.
# inventory = ["karta", "kompass"]
# Du kan välja att titta i din påse, promenera vidare eller löka
# Om du tittar i din påse får du reda på vad du har med dig
# Om du promenerar vidare så fortsätter du din vandring
# Om du lökar så står du stilla och tittar dig omkring
# När du lökar finns det en 50% chans att du hittar något spännande 
# items = ["vättejos", "kantarell", "ekorre", "sten"]
# det finns även en 20% chans att du möter en person på din vandring
# Om du äter vättejos så blir du sjuk och förlorar 1 liv
# Om du äter kantarell så blir du mätt och får 1 liv
# Om du äter ekorre så är du moraliskt tvivelaktig och förlorar 1 poäng
# Om du äter sten så bryter du dina tänder och förlorar 1 liv
# Om du möter en person och är smittad av vätte så kan du bita personen och
# förvandla dem till en vätte, -10 poäng
# du landar i den mörka sidan och spelet är över
# Vad väljer du att göra?
# Det är en 50% chans att du möter en vätte på din vandring
# Plötsligt möter du en ondskefull vätte, de är väldigt fega, farliga och hemska
# Vätten närmar sig hotfull, vad väljer du att göra?
# Bekämpa vätten med pathos, logos och ethos alltså på svenska med känslor, logik och etik
# logik besegrar känslor, du trasslar in vätten i en logisk diskussion och kan smita förbi
# +1 poäng för att du klarade dig förbi vätten
# etik besegrar logik, vätte imponeras av din moral och ger dig en gåva
# +1 poäng för att du klarade dig förbi vätten
# du får en slumpad gåva från vätten, ["ostkant", "pepparkvarn", "fiskespö", "tandpetare"]
# känslor besegrar etik, känslorna tar över och vätten blir arg och biter dig, spring!
# Du har blivit biten av vätten, vättar är giftiga, du kommer att förvandlas till en vätte om 3 rundor
# Det är oavgjort, du tänker så hårt att du får huvudvärk
# -1 liv

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
