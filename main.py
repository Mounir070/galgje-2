if turns == 1:
        print("""     ____
      | \|
      o  |
     /|\ |
     / \ |
         |
    _____|""")
    #als je verloren hebt
        print("Schande!, Je hebt het woord", hetwoord, "niet kunnen raden")
        print("Je kan het nog een keer proberen, type ja of nee")
  
# de woorden die gebruikt gaan worden
  woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier",
  "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]
  
  # letters die zijn toegestaan
  validLetters = "a", "b", "c", "d", "", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
   
  # random woord word gekozen en door puntjes vervangen 
# random woord word gekozen en door puntjes vervangen 

  hetwoord= random.choice(woordenlijst)
  lengtewoord = len(hetwoord)
  puntjes = [" ~ "] *lengtewoord
  ja = "ja"
  nee = "nee"

# introductie
  naam = input("Vul hier je naam in: ")
  print()
  print("Welkom", naam,"bij ons galgje spel")
  game = True

  print("Raad de letters en als je het woord weet typ het dan in.")
  print()
  print("het woord heeft " + str(lengtewoord) + " letters")
   #als het woord geraden is
  while game == True:
    userGuess = input("raad een letter of het woord: ")
    if userGuess == hetwoord:
      print ("gefeliciteerd", naam, "je hebt het woord geraden")
      print()
      print("wil je nog een keer spelen? Type dan ja of nee?")
      print("Goed gedaan!!! je had alleen deze letters nodig om het woord te raden")
    #speler kan kiezen om opnieuw te spelen
    if userGuess == ja:
       spel()
       if userGuess == nee:
       quit()
    #letter verschijnt als ie geraden is
    else:
      if userGuess in hetwoord:
        for idx, letter in enumerate(hetwoord):
          
          if(letter == userGuess):
            puntjes[idx] = userGuess
      #als er een foute gok is      
      else:
        turns -= 1
        drawgalgjes()
    print(''.join(puntjes))

  if userGuess not in validLetters:
   turns -= 1
   
spel()