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