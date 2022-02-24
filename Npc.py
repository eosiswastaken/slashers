import Player
import Tools


class Banker:
    def __init__(self,name):
        self.gold = 6008
        self.name = name
        self.maxInvSize = 1000
        self.bank = {
                "item1" : 64,
                "item2" : 16,
                "item3" : 48,
                "item4" : 32
        }


    def store_item(self,item,quantity):
            if self.get_weight() + quantity < self.maxInvSize:
                if item in self.bank:
                    self.bank[item] += quantity
                    Player.P.remove_item(item,quantity)
                    print("You stored " + str(quantity) + " " + str(item) + " in your bank, there is now a total of " + str(self.bank[item]) + " " + str(item) + " in your bank")
                else:
                    self.bank[item] = quantity
                    Player.P.remove_item(item,quantity)
                    print("You stored " + str(quantity) + " " + str(item) + " in your bank.")

    def retrieve_item(self,item,quantity):
        if item in self.bank:
            Player.P.add_item(item,quantity)
            print("alr existing updating qt")##
            if quantity >= self.bank[item]:
                del self.bank[item]
                print("You took all the " + str(quantity) + " " + str(item) + " in your bank, there is no more " + str(item) + " in your bank.")
            else:
                self.bank[item] -= quantity
                print("You took " + str(quantity) + " more " + str(item) + " in your bank, there is now a total of " + str(self.bank[item]) + " " + str(item))



    def query_store_item(self):
        item = str(input("Quel item veux-tu stocker dans la banque?"))
        if item in Player.P.inv:
            print("You have " + str(Player.P.inv[item]) + " " + str(item) + " in your inventory.")
            quantity = int(input("Combien?"))
            if quantity <= Player.P.inv[item] and type(quantity) == int:
                self.store_item(item,quantity)

    def query_retrieve_item(self):
            item = str(input("Quel item veux-tu sortir de la banque?"))
            if item in self.bank:
                print("You have " + str(self.bank[item]) + " " + str(item) + " in your bank.")
                quantity = int(input("Combien?"))
                if quantity <= self.bank[item] and type(quantity) == int:
                    self.retrieve_item(item,quantity)

    def deposit_gold(self):
        try:
             amount = int(input("Combien de gold veux tu déposer ?"))
        except ValueError:
            print("You must input an integer !")
            amount = 0
        if amount <= Player.P.gold and amount != 0:
            self.gold += amount
            Player.P.gold -= amount
            print("Tu as déposé " + str(amount) + " gold dans ton inventaire")
            B.print_gold()


    def retrieve_gold(self):
        try:
             amount = int(input("Combien de gold veux tu prendre ?"))
        except ValueError:
            print("You must input an integer !")
            amount = 0
        if amount <= self.gold and amount != 0:
            Player.P.gold += amount
            self.gold -= amount
            print("Tu as déposé " + str(amount) + " gold dans ta banque")
            B.print_gold()

    def print_gold(self):
        print("Tu as actuellement " + str(self.gold) + " gold en banque, et " + str(Player.P.gold) + " sur toi")

    def get_weight(self):
        totalWeight = 0
        for i in self.bank.values():
            totalWeight += i
        return totalWeight

    def print_bank(self):
        count = 0
        for i in self.bank:
            print(" | Bank : " + str(self.bank[i]) + " " + str(i), end=' ')
            count += 1
            if count == 3:
                print("")
                count = 0
        print("")
        print(" --> You have [" + str(self.get_weight()) + " / " + str(self.maxInvSize) + "] items")



B = Banker("Thierry")
#B.store_item("UNITEM",1)
#B.query_store_item()
#B.query_store_item()
#B.query_store_item()
#B.query_store_item()
#B.query_store_item()
#B.query_retrieve_item()
#B.deposit_gold()
#B.retrieve_gold()
#B.print_gold()
#B.print_bank()
