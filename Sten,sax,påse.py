import random as rand
lista = ["Sten", "Sax", "Påse"]
print(f"Nu ska vi spela Sten, Sax eller Påsen\nJag är Python311")

spelare = input("Ange ditt Spelarnamn --> ")
antal_omgangar = int(input("Ange antal omgångar vi ska spela --> "))

for i in range (antal_omgangar):
    bot_val = rand.choice(lista)
    val = input("Välj 'Sten', 'Sax' eller 'Påse'--> ")
    print(f"Spelomgång {i+1}\n", "-"*12)
    print(f"{spelare} spelar: {val.title()}")
    print(f"Python311 spelar: {bot_val}")
    
    #Oavgjort
    if bot_val.lower() == val.lower():
        print(f"Vinnare i spelomgång {i+1}: Oavgjort")
    #Spelaren vinner
    elif (val == "Sten" and bot_val == "Sax") or \
         (val == "Sax" and bot_val == "Påse") or \
         (val == "Påse" and bot_val == "Sten"):
        print(f"Vinnaren i spelomgång 1: {spelare}!")
    #Datorn vinner
    else:
        print("Vinnaren i spelomgång 1: Python311!")

    
        