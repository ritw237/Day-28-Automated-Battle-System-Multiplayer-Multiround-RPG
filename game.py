import os
import time
import random
import unittest


def roll(sides):
  roll = random.randint(1, sides)
  return roll


def health():
  health_val = (((roll(6) * roll(12)) / 2) + 10)
  return health_val


def strength():
  strength_val = ((roll(6) * roll(12)) / 2 + 12)
  return strength_val


agility_val = ((roll(8) * roll(10)) / 2 + 12)
intelligence_val = ((roll(12) * roll(6)) / 2 + 12)
charisma_val = ((roll(10) * roll(8)) / 2 + 12)

# dictionary of epic quotes
epic_quotes = {
  "Human": [
    "I am the flame that will never be extinguished!",
    "I will not be broken by the hardships of this world!",
    "I will rise above adversity and conquer all!",
    "I am the future, and the future is bright!"
  ],
  "Elf": [
    "My magic is unmatched by any mortal!",
    "I am the guardian of the forest, and I will not be swayed!",
    "My arrows will find their mark, and my enemies will fall!",
    "I am the embodiment of grace and power!"
  ],
  "Wizard": [
    "My knowledge of the arcane arts is unrivaled!",
    "I am the master of the elements, and they bend to my will!",
    "My spells will shatter the earth and bring forth destruction!",
    "I am the bringer of light, and the keeper of the dark!"
  ],
  "Orc": [
    "I am the terror of the battlefield, and my enemies will tremble before me!",
    "My axe will split the earth and crush my foes!",
    "I will not be stopped, and I will not be defeated!",
    "I am the embodiment of strength and ferocity!"
  ]
}


def char_generator():

  name = str(input("Name Your Legend: \n"))
  print("Name input:", name)
  type = str(input("Character Type (Human, Elf, Wizard, Orc): \n"))
  print("Type input:", type)
  while type not in ['Human', 'Elf', 'Wizard', 'Orc']:
    type = str(input("Invalid character type. Please choose from (Human, Elf, Wizard, Orc): \n"))
  char_health = health()
  char_strength = strength()
  char_quote = random.choice(epic_quotes[type])

  # store the values in a dictionary
  char_dict = {
    "name": name,
    "type": type,
    "health": char_health,
    "strength": char_strength,
    "quote": char_quote
  }
  return char_dict
  # return name, type, char_health, char_strength,  char_quote


def simulate_battle():

  round = 1
  print("🤺⚔️  Epic Character Battlegrounds ⚔️🛡")
  print("\nWho are you? \n")
  char1 = char_generator()
  #print("-----")
  #print(char1)
  #print("-----")

  print()
  print("You are a", char1["type"], "named", char1["name"])
  print("Your health is", char1["health"], "and your strength is",
        char1["strength"])
  print("Your epic quote is:", char1["quote"])
  

  print("\nWho are you battling? ")
  char2 = char_generator()
  #print("-----")
  #print(char2)
  #print("-----")
  print()
  print("You are a", char2["type"], "named", char2["name"])
  print("Your health is", char2["health"], "and your strength is",
        char2["strength"])
  print("Your epic quote is:", char2["quote"])
  time.sleep(4)

  while True:
    time.sleep(4)
    #detects the operating system and clears the screen
    if os.name == 'nt':
      os.system("cls")
    else:
      os.system("clear")

    

    print("⚔️ ⚔️ ⚔️ ⚔️        ⚔️ ⚔️ ⚔️ ⚔️\nround", round, "starts now")
    time.sleep(1)

    roll1 = roll(6)
    roll2 = roll(6)
    # defining winner variable and loser variable so they can hold the character dictionary
    winner = {}
    loser = {}

    if roll1 > roll2:

      winner = char1
      loser = char2
    elif roll1 < roll2:

      winner = char2
      loser = char1
    else:
      print("round",round, "is a draw")
      round += 1
      print("-----")
      print("round", round, "will begin now")
      continue

    # display the winner and loser
    print(winner['name'], "wins round", round, "with a roll of", roll1, "and loser",loser["name"], "loses with a roll of", roll2)
    
    loser["health"] -= (winner["strength"] - loser["strength"]) + 1
    # display the health of the loser and winner
    print("\n",winner["name"], "has", winner["health"], "health left")
    print(loser["name"], "has", loser["health"], "health left")

    if loser["health"] <= 0:
      print(winner["name"], "wins the battle!")
      break
    else:
      print("\n",loser["name"], "has", loser["health"], "health left")
      print(loser["name"], "loses the round!")
      print(winner["name"], "has", winner["health"], "health left")
      print(winner["name"], "wins the round!")
      round += 1
      continue


print("⚔️ BATTLE TIME ⚔️\n")
print("-----\n")
simulate_battle()

try:
  ques = str(input("\nWanna play again? "))
  if ques == "yes" or ques == "Yes":
      simulate_battle()
  else:
      exit()
except SystemExit:
  pass

if __name__ == '__main__':
    import unittest
    import test_game
    unittest.main(module=test_game, exit=False, verbosity =2)




