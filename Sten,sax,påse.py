print("Nu ska vi spela Sten, Sax eller Påse!")
print("Jag är Python311\n")
spelare = input("Ange ditt Spelarnamn -->")
while True:
    try:
        antal_omgangar = int(input("Ange antal omgångar vi ska spela -->"))
        break
    except ValueError:
        continue