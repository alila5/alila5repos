from player import Player
from hamsters import Hamster
import time
import random

class Game:
    hamsters_count = 3
    happy_message = "WOW!!!!! You won!!!"
    map = """**\n**"""    # Это поле по умолчанию   #"""****\n****\n****"""
    gameon = True
    round = 1  # Счетчик ходов
    directions = {"w": "s", "s": "w", "a": "d", "d": "a"}

    def __init__(self, map_W, map_H):
        self.player = Player()
        self.hamsters = []
        self.map =  (('*'*map_W)+'\n')*(map_H-1)+('*'*map_W)    # Генератор карты
        self.map_size = {'width': map_W-1,'height': map_H-1}    # Один раз считаем размер карты

        for i in range(self.hamsters_count):
            self.hamsters.append(Hamster(i+1, self.get_full_map(True),self.map_size))

    def add_point(self, position, name, s):
        li = s.split("\n")
        row = li[position[1]]
        row = row[:position[0]] + name + row[position[0]+1:]
        li[position[1]] = row
        return "\n".join(li)

    def render_map(self, f_print):
        s = self.map
        s = self.add_point(self.player.position, "x", s)
        for h in self.hamsters:
            if h.health > 0:
                s = self.add_point(h.position, str(h.id), s)
        if f_print == True:
            print(s)
            print('-'*40)

    def move_player(self, destination):
        """ destination = w,a,s,d """
        if destination == "s":
            if self.player.position[1] == self.map_size['height'] :
                return False
            self.player.position[1] += 1  # bottom
        if destination == "w":
            if self.player.position[1] == 0:
                return False
            self.player.position[1] -= 1  # top
        if destination == "a":
            if self.player.position[0] == 0:
                return False
            self.player.position[0] -= 1  # left
        if destination == "d":
            if self.player.position[0] == self.map_size['width'] :
                return False
            self.player.position[0] += 1  # right
        self.on_move(destination)

    def get_full_map(self, start_game=False):
        s = self.map
        for h in self.hamsters :
            if h.health > 0:                 # !!!!!!!!!!!!!!!!!!!!!!!!!  Это злой косяк был. Без этого if-а мыши виртуально жили    !!!!!!!
                s = self.add_point(h.position, str(h.id), s)
        if start_game:
            s = self.add_point(self.player.position, "x", s)
        return s

    def get_hamster_on_position(self, coords):
        s = self.get_full_map()
        return s.split("\n")[coords[1]][coords[0]]



    def on_move(self, direction):
        hamster = self.get_hamster_on_position(self.player.position)
        if not hamster == "*":
            print('Player Х  атаковал крысу ',hamster )
            self.player.was_hit(int(hamster))
            if self.player.health <= 0:
                self.gameon = False
                print("game over... sorry!")
                return False
            #print("player's health: ", self.player.health)
            killed = self.hamsters[int(hamster)-1].on_shot()
            if not killed:
                self.move_player(self.directions[direction])



    def Move_Fast(self, sleep_time):  # функция ускоренной ловли крыс
        x = 0
        y = 0
        time.sleep(sleep_time)
        for h in self.hamsters:
            if h.health > 0:
                y = y + h.position[1]
                x = x + h.position[0]
        x = x / len(self.hamsters)
        y = y / len(self.hamsters)
        dx = abs(self.player.position[0] - x)
        dy = abs(self.player.position[1] - y)
        if dx >= dy:
            if x >= self.player.position[0]:
                command = 'd'
            else:
                command = 'a'
        else:
            if y >= self.player.position[1]:
                command = 's'
            else:
                command = 'w'
        return command

    def start(self):
        game.render_map(True)   # в рендер добавил обработчик отображать поле или нет
        while self.gameon:
            self.round += 1
            print('Шаг игры ', self.round)
            sleep_time = 0                                      # Время задержки 0 - ...
            command = self.Move_Fast(sleep_time)
            # command = random.choice(["a", "s", "d", "w"])     # Вариант со случайной охотой
            #command = input("Insert command: ")               # Классика
            if command in ["a", "s", "d", "w", 'e']:
                self.move_player(command)
                self.render_map(False)
                print('-'*8, 'Список живых','-'*8)
                print('Name, Health, X/Y')
                print('  Х   ', self.player.health, '   ',self.player.position)
                print('-' * 30)
                if len([h for h in self.hamsters if h.health > 0]) == 0:
                    print(self.happy_message)
                    self.render_map(True)
                    print('-END-' * 7)
                    return True
                for h in self.hamsters:                         # Это заставляет крыс бегать
                    if h.health > 0:
                        h.position = h.walk(self.get_full_map(True), self.map_size, h.position)
                        print(' ',h.id,'  ', h.health,'   ', h.position)
                        print('-' * 30)
                self.render_map(True)
            if command == "e":
                self.player.wait()
            if command == "q":
                self.gameon = False





game = Game(200,200)
game.s =30

game.start()
