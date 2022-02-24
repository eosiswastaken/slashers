import Tools
import random

class Player:
    def __init__(self,name):
        self.hp = 20
        self.mp = 8
        self.atk = 10
        self.defense = 3
        self.gold = 100
        self.name = name
        self.inv = {}
        self.maxInvSize = 50
        self.faction = None
        self.race = None
        self.classe = None
        self.maxInvSize = 50
        self.xpToNextLevel = 10
        self.xpCurve = 1.4
        self.xp = 0
        self.lvl = 0
        self.pos = 0
        self.quickCmd = "look"
        self.adminStatus = False

    def create_player(name):
        return Player(name)

    def give_xp(self,amount):
        self.xp += amount
        if self.xp >= self.xpToNextLevel:
            self.lvl += 1
            self.xp = 0
            self.xpToNextLevel = round(self.xpToNextLevel * self.xpCurve,1)
            print(self.xpToNextLevel)
            self.level_up()

    def level_up(self):
        print("You leveled up to level " + str(self.lvl) + " ! You will need " + str(self.xpToNextLevel) + " XP to get to the next level !")
        if (self.lvl - 1) % 5 == 0:
            print("multiple de 5 omg")


    def print_inventory(self):
        for i in self.inv:
            print(" | You have " + str(self.inv[i]) + " " + str(i))
        print(" --> You have [" + str(self.get_weight()) + " / " + str(self.maxInvSize) + "] items")

    def print_gold(self):
        print(" --> Tu as " + str(self.gold) + " Gold")

    def give_item(self,item,quantity):
        if not self.is_inventory_full():
            if self.get_weight() + quantity < self.maxInvSize:
                if item.title() in self.inv:
                    self.inv[item.title()] += quantity
                else:
                    self.inv[item.title()] = quantity

    def check_item(self,item):
        if item.title() in self.inv:
            return self.inv[item.title()]

    def remove_item(self,item,quantity):
        if item.title() in self.inv:
            if quantity >= self.inv[item.title()]:
                del self.inv[item.title()]
            else:
                self.inv[item.title()] -= quantity

    def get_weight(self):
        totalWeight = 0
        for i in self.inv.values():
            totalWeight += i
        return totalWeight

    def is_inventory_full(self):
        totalWeight = 0
        for i in self.inv.values():
            totalWeight += i
        if totalWeight >= self.maxInvSize:
            return True
        else:
            return False

    def give_loot(self,pool):
        for i in range(0,len(pool), 3):
            item = pool[i]
            quantity = pool[i+1]
            chance = pool[i+2]
            if item == "Gold":
                self.gold += random.randint(quantity[0],quantity[1])
            elif Tools.Dice(100).roll() >= chance:
                finalQuantity = random.randint(quantity[0],quantity[1])
                self.give_item(item,finalQuantity)
            elif chance == 100:
                finalQuantity = random.randint(quantity[0],quantity[1])
                self.give_item(item,finalQuantity)

    def attack(self):
        pass


P = Player("Eosis")
#P.give_item("Ethan",1)
#P.give_item("ITEM",10)
#P.give_item("MOREITEMS",7)
#P.give_item("This item should not be added",300)
#P.print_inventory()

#pool = ["Sword",[1,1],50,"Gold",[20,200],100]
#P.give_loot(pool)
#P.print_inventory()
#P.print_gold()

#P.give_xp(80)
#P.give_xp(14)

#print(P.defend())
#print(P.attack())