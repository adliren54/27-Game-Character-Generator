import random
import os, time

def chara():
  name = input("Name your Legend: \n")
  type = input("Character Type (human, elf, wizard, orc, imp, etc): \n")
  return name

def chara_health():
  health1 = random.randint(1, 6)
  health2 = random.randint(1,12)
  health = ((health1 * health2) / 2) + 10
  return health

def chara_strength():
  strength1 = random.randint(1,6)
  strength2 = random.randint(1,12)
  strength = ((strength1 * strength2) / 2) + 10
  return strength

while True:
  print("⚔️ CHARACTER BUILDER ⚔️")
  char = chara()
  charHealth = chara_health()
  charStrength = chara_strength()
  print(char)
  print("HEALTH: ", charHealth)
  print("STRENGTH", charStrength)

  print("May your name go down in Legend...")

  terus = input("Again? (yes/no): ")
  if terus == "yes":
    time.sleep(1)
    os.system("clear")
    continue
  elif terus == "no":
    break