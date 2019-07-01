from!!!!!!! random import randint, choice

class Hamster:
    def __init__(self, hid,  map, map_size):
        self.id = hid
        self.health = 2
        self.position = self.get_clear_position(map, map_size)

    def get_clear_position(self, map, map_size):

        while True:
            coords = [randint(0, map_size['width']), randint(0, map_size['height'])]
            if map.split("\n")[coords[1]][coords[0]] == "*":
                return coords

    def walk(self, map, map_size, position):    # Метод двигает крыс
        direction = randint(0, 3)               #0 - right  1 - left 2 -up 3  -bottom
        coords = position

        if direction == 0 and (position[0] + 1) <= map_size['width']:
            coords = [position[0] + 1, position[1]]
        if direction == 1 and (position[0] - 1) >= 0:
            coords = [position[0] - 1, position[1]]
        if direction == 2 and (position[1] - 1) >= 0:
            coords = [position[0], position[1] - 1]
        if direction == 3 and (position[1] + 1) <= map_size['height']:
            coords = [position[0], position[1] + 1]

        if map.split("\n")[coords[1]][coords[0]] == "*":
            return coords
        else:
            return position

    def on_shot(self):
        self.health -= 1
        if self.health == 0:
            print(self.id, "was kiled")
            return True
        else:
            print(f'Мышку {self.id} пнули, осталось жить ей {self.health}')
            return False
