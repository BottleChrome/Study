import Car 

print("Use Case 1 ")
sonata = Car.Sonata("new")
sonata.move(50)
sonata.show_dash()
sonata.ride(2)
sonata.move(450)
sonata.show_dash()
sonata.fill(35)
sonata.move(140)
sonata.ride(-1)
sonata.move(100)
sonata.show_dash()
print("\n\n")
print("Use Case 2 ")

bongo = Car.Bongo("old")
bongo.fill(20)
bongo.load(600)
bongo.move(120)
bongo.show_dash()
bongo.fill(30)
bongo.move(240)
bongo.show_dash()
bongo.load(-200)
bongo.move(30)
bongo.show_dash()