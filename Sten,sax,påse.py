import random as rand
lista = ["Sten", "Sax", "Påse"]

spelarens_poäng = 0
datorns_poäng = 0

print(f"Nu ska vi spela Sten, Sax eller Påsen\nJag är Python311")

spelare = input("Ange ditt Spelarnamn --> ")


while True:
    try:
        antal_omgangar = int(input("Ange antal omgångar vi ska spela --> "))
        if antal_omgangar > 0:
            break
        print("Ogiltigt svar. Du måste ange ett tal större än 0")
    except ValueError:
        print("Ogiltigt svar. Du måste ange ett tal")


#Kör spelet ett valt antal omgångar
for i in range (antal_omgangar):
    bot_val = rand.choice(lista)
    print(f"\nSpelomgång {i+1}\n", "-"*13)
    
    
    #Ser till att du väljer Sten, Sax eller Påse
    while True:
        val = input("Välj 'Sten', 'Sax' eller 'Påse'--> ").capitalize()
        if val in lista:
            break
        print("Ogiltigt svar! Du måste välja Sten, Sax eller Påse.")
    
    print (f"{spelare} spelar: {val}\nPython311 spelar: {bot_val}")
    
    
    #Oavgjort
    if bot_val == val:
        print(f"\nVinnare i spelomgång {i+1}: Oavgjort")
    #Spelaren vinner
    elif (val == "Sten" and bot_val == "Sax") or \
         (val == "Sax" and bot_val == "Påse") or \
         (val == "Påse" and bot_val == "Sten"):
        spelarens_poäng += 1
        print(f"\nVinnaren i spelomgång {i+1}: {spelare}!")
    #Datorn vinner
    else:
        datorns_poäng += 1
        print(f"\nVinnaren i spelomgång {i+1}: Python311!\n")


#Skriver ut slutpoäng och vinnaren
print(f"\nSLUTRESULTAT\n", "="*13)
if datorns_poäng > spelarens_poäng:
    print(f"Python311: {datorns_poäng}p\n{spelare}: {spelarens_poäng}p")
    vinnare = "Python311"
elif datorns_poäng == spelarens_poäng:
    print(f"{spelare}: {spelarens_poäng}p\nPython311: {datorns_poäng}p")
    vinnare = "Oavgjort"
else:
    print(f"{spelare}: {spelarens_poäng}p\nPython311: {datorns_poäng}p")
    vinnare = spelare
print(f"Vinnare: {vinnare}!")
        