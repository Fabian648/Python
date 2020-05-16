import random


class Character:
    def __init__(self, hp, ad, name, de):
        self.hp = hp
        self.ad = ad
        self.name = name
        self.de = de

    def get_hit(self, ad):

        self.hp = self.hp - ad / self.de

        if self.hp <= 0:
            self.die()

    def is_dead(self):
        return self.hp <= 0

    def die(self):
        print(self.name + " is dead")


class Enemie(Character):
    pass

class Ork(Enemie):
    def __init__(self):
        Character.__init__(self, 200, 40, "ork", 1.25)

class Archer(Enemie):
    def __init__(self):
        Character.__init__(self, 75, 50, "archer", 1)

class Field:
    def __init__(self, enemies):
        self.enemies = enemies
    
    def print_state(self):
        print("You look around and see ")

        for i in self.enemies:
            print(i.name)
    
    @staticmethod
    def gen_random():
        en = random.randint(0,2)
        if en == 0:
            return Field([])
        elif en == 1:
            return Field([Archer()])
        elif en == 2:
            return Field([Ork()])

class Map:
    def __init__(self, width, height):
        self.state = []
        self.x = 0
        self.y = 0

        for i in range(width):
            fields = []
            for j in range(height):
                fields.append(Field.gen_random())
            self.state.append(fields)

    def print_state(self):
        self.state[self.x][self.y].print_state()

    def get_enemies(self):
        return self.state[self.x][self.y].enemies

    def forward(self):
        if self.x == len(self.state) - 1:
            print("You see huge mountains which you can't pass")
        else:
            self.x += 1

    def backwards(self):
        if self.x == 0:
            print("You see cliffs but you can't jump safely")
        else:
            self.x -= 1

    def right(self):
        if self.y == len(self.state[self.x]) - 1:
            print("You see huge mountains which you can't pass")
        else:
            self.y += 1

    def left(self):
        if self.y == 0:
            print("You see cliffs but you can't jump safely")
        else:
            self.y -= 1

class Player(Character):
    def __init__(self, name, hp, ad, de):
        Character.__init__(self, hp, ad, name, de)
        self.max_hp = hp

    def die(self):
        exit("Wasted. Try again.")

    def game_rest(self):
        self.hp = self.max_hp
        print("You were healed\nNow you have " + str(int(p.hp)) + " hp")

def game_help(p, m):
    print(commands.keys())

def game_quit(p, m):
    exit("You commit suicide and leave this world.")

def rest(p, m):
    p.game_rest()

def forward(p, m):
    m.forward()

def backwards(p, m):
    m.backwards()

def right(p, m):
    m.right()

def left(p, m):
    m.left()

def fight(p, m):
    enemies = m.get_enemies()
    while len(enemies) > 0:
        enemies[0].get_hit(p.ad)
        if enemies[0].is_dead():
            enemies.remove(enemies[0])
        for i in enemies:
            p.get_hit(i.ad)
        print("You are wounded and have " + str(int(p.hp)) + " hp left")

commands = {
    "help": game_help,
    "quit": game_quit,
    "fight": fight,
    "rest": rest,
    "forward": forward,
    "backwards": backwards,
    "right": right,
    "left": left
}
if __name__ == "__main__":
    name = input("Enter your name: ")
    p = Player(name, 500, 100, 2)
    map = Map(10, 10)
    run = True
    print("type help to list the commands available \n")
    while run:
        
        command = input("> ").lower().split(" ")
        if command[0] in commands:
            commands[command[0]](p , map)
        else:
            print("You run around in circles and don't know what to do.")
        map.print_state()