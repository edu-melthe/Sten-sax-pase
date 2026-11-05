print("Nu ska vi spela Sten, Sax eller Påse!")
print("Jag är Python311\n")
spelarnamn = input("Ange ditt Spelarnamn -->")
while True:
    try:
        omgångar = int(input("Ange antal omgångar vi ska spela -->"))
        break
    except ValueError:
        continue