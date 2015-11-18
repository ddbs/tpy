#!/usr/bin/env python3

class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()


class Bassist(Musician):
    def __init__(self):
        super().__init__(["Twang", "Thrumb", "Bling"])


class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boink", "Bow", "Boom"])


class Drummer(Musician):
    def __init__(self):
        super().__init__(["Rataplan", "Badum", "Pah"])

    def count(self):
        c = ['One', 'Two', 'Three', 'Four']
        for i in c:
            print(i)

    def combust(self):
        print("Drummer combusting!")

#dario = Drummer()
#dario.solo(6)
#dario.count()
#dario.combust()


class Band(Musician):
    def __init__(self):
        self.members = []
        self.drummer = Drummer()

    def hire(self):
        musician_hire = input("Want to hire a [b]assist, a [g]uitarist, or a [d]rummer? ").lower()

        if musician_hire in 'bgd':
            if musician_hire == 'b':
                print("You have hired a bassist!")
                self.members.append(Bassist())
            elif musician_hire == 'g':
                print("You have hired a guitarist!")
                self.members.append(Guitarist())
            elif musician_hire == 'd':
                print("You have hired a drummer!")
                self.members.append(Drummer())
        else:
            self.hire()

    def fire(self):
        print(self.members)
        musician_fire = input("Want to fire a [b]assist, a [g]uitarist, or a [d]rummer? ").lower()

        if musician_fire in 'bgd':
            if musician_fire == 'b':
                for m in self.members:
                    if isinstance(m, Bassist):
                        self.members.remove(m)
            elif musician_fire == 'g':
                for m in self.members:
                    if isinstance(m, Guitarist):
                        self.members.remove(m)
            elif musician_fire == 'd':
                for m in self.members:
                    if isinstance(m, Drummer):
                        self.members.remove(m)
        else:
            self.fire()

#Q how to remove objects from a list?

    def members_count(self):
        print("The band has {} musicians:".format(len(self.members)))
        for musician in self.members:
            print(musician.__class__.__name__)

    def play(self, length):
        self.drummer.count()
        for musician in self.members:
            musician.solo(length)


u3 = Band()
u3.hire()
u3.hire()
u3.hire()
u3.play(6)
u3.fire()
#u3.members_count()
