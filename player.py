import random

class Player:
    health = 10
    max_health = 10
    position = [1, 0]

    def was_hit(self, hid):
        # self.health -= hid
        self.health -= 1 #+ random.choice(range(hid+1))
        #print("player's health from Player: ", self.health)

    def wait(self):
        if not self.health == self.max_health:
            self.health += 1
        print("player's health:", self.health)

