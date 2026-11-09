import random
lista = ["Sten", "Sax", "Påse"]

print("Nu ska vi spela Sten, Sax eller Påse!")
print("Jag är Python311\n")
spelare = input("Ange ditt Spelarnamn -->")
while True:
    try:
        antal_omgangar = int(input("Ange antal omgångar vi ska spela -->"))
        break
    except ValueError:
        continue
for i in range (antal_omgangar):
    botval = random.choice(lista)
    print(f"Spelomgång {i+1}\n", "-"*12)
    val = input("Välj 'Sten', 'Sax' eller 'Påse'-->")
    print(f"{spelare} spelar: {val.title()}")
    print(f"Python311 spelar: {botval}")
    if botval.lower() == val.lower():
        print(f"Vinnare i spelomgång {i+1}: Oavgjort")
    elif ((botval == "Sten" and val.lower() == "sax") or (botval == "Sax" and val.lower() == "påse") or (botval == "Påse" and val.lower() == "sten")):
        print(f"Vinnare i spelomgång {i+1}: Python311")
    elif ((botval == "Sax" and val.lower() == "sten") or (botval == "Påse" and val.lower() == "sax") or (botval == "Sten" and val.lower() == "påse")):
        print(f"Vinnare i spelomgång {i+1}: {spelare}")
    
        