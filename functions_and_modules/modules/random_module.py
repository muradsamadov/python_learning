import random

value = random.random()  #random ededleri print edir
value = random.uniform(1,6)  #1-6 arasindaki random ededleri print edir burda yalniz kesr ededler daxildir
value = random.randint(1,6)  #randint ile 1-6 araligindaki yalniz tam ededleri print edir

print(value)

#####
import random

greetings = ["Hello", "Hi", "Hey"]
value = random.choice(greetings)  #choice ile greetings-in daxilindekiler random olaraq secir

print(value + ", Murad!")

#####
import random

deck = list(range(1,53))  #1-53 e kimi olan butun edeleri ardicil olaraq print edir

print(deck)

#####
import random

deck = list(range(1,53))

random.shuffle(deck)  #shuffle ile 1-53 arasi butun ededleri qarisiq sekilde print edir

print(deck)

#####
import random

deck = list(range(1,53))

hand = random.sample(deck, k=5)  #sample ile 1-53 arasi ededleri qarisiq sekilde amma ki, 5 ededini print edir

print(hand)