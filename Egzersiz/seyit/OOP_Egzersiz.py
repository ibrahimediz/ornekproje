class Hero:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health


class Arena:
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2

    def fight(self):
        person1 = int(self.person1.health)
        person2 = int(self.person2.health)
        while person1 > 0 and person2 > 0:
            person1 -= int(self.person2.power)
            person2 -= int(self.person1.power)

        if person1 > person2:
            winner = self.person1.name
        elif person1 == person2:
            winner = "no one!"
        else:
            winner = self.person2.name
        return winner


batman = Hero("Batman", "88", "1000")
naruto = Hero("Naruto", "88", "1000")

fight1 = Arena(naruto, batman).fight()
print("The winner is %s" % fight1)


