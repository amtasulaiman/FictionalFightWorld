import Proj2

p = Proj2.Person("Amta", 20, 10)
f1 = Proj2.Fighter("Henry", 22, 20)
f2 = Proj2.Fighter("Robin", 17, 30)
f3 = Proj2.Fighter("Chris", 24, 50)
f4 = Proj2.Fighter("Bella", 27)

print(p.str())
print(f1.str())
print(f2.str())
print(f3.str())
print(f4.str())

print("*****************************************************")
f1.challenge(f2, "spear")
f3.challenge(f3, "mace")
f4.challenge(f1, "broadsword")
print("*****************************************************")
w1 = Proj2.Warrior("Jacob", 24, 45)
w2 = Proj2.Warrior("Caleb", 33, 50)
w3 = Proj2.Warrior("Spencer", 40, 60)
print(w1.str())
print(w2.str())
print(w3.str())
print("*****************************************************")
w2.challenge(w1, "spear")
f1.challenge(w1, "spear")
f1.challenge(w1, "mace")
f3.challenge(w1, "broadsword")
f2.challenge(w1, "mace")

print(w1.str() + "\n" + w1.str_challenges())
print("*****************************************************")
w1.accept_random()
print(w1.str() + "\n" + w1.str_challenges())
w1.decline_random()
print(w1.str() + "\n" + w1.str_challenges())
w1.accept_first()
print(w1.str() + "\n" + w1.str_challenges())
w1.decline_first()
print(w1.str() + "\n" + w1.str_challenges())
print("*******************************************************")
k1 = Proj2.KnightErrant("Cory", 38, 70)
k2 = Proj2.KnightErrant('William', 39, 120)

print(k1.str())
print(k2.str())
print("*******************************************************")

w2.challenge(k1, 'unarmed combat')
f3.challenge(k1, 'broadsword')
k2.challenge(k1, 'spear')
f1.challenge(k1, 'mace')

k1.travel()

k1.challenge(k2, 'mace')
k2.challenge(k1, 'mace')
print("******************************************************")
print(k1.str() + "\n" + k1.str_challenges() + "\n")

k1.return_from_travel()

k1.accept_first()
print(k1.str() + "\n" + k1.str_challenges())
k1.decline_random()
print(k1.str() + "\n" + k1.str_challenges())
k1.accept_random()
print(k1.str() + "\n" + k1.str_challenges())
k1.decline_first()
print(k1.str() + "\n" + k1.str_challenges())

# Test case for withdraw
print("************************************************")
f3.challenge(w3, 'mace')
print(w3.str() + "\n" + w3.str_challenges())
f3.challenge(f1, 'spear')
f3.withdraw(w3)
print(w3.str() + "\n" + w3.str_challenges())





