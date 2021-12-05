import random

names = ["Josh", "Maria", "Jasper", "Francois", "Saara"]
lastnames = ["Smith", "Sim", "Holland", "Macpherson"]

random_name = random.choice(names) + " " + random.choice(lastnames)
print(random_name)