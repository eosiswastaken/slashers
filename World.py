import Room
import Player

class World:
    def __init__(self,map):
        self.map = map

    def can_move_to(self,room):
        if room in self.map[Player.P.pos].get_exits():
            return True
        else:
            return False

    def can_move_to_dir(self,dir):
        exits = self.map[Player.P.pos].get_exits()
        if exits[dir] != -1:
            return exits[dir]
        else:
            return False

    def move_to(self,room):
        Player.P.pos = room
        print(" Room desc. : " + str(W.map[Player.P.pos].get_description()))
        print(" You are at : " + str(Player.P.pos))
        print(" Exits of this room : " + str(W.map[Player.P.pos].get_exits()))
        print(W.map[Player.P.pos].contents["monsters"])





W = World(Room.map)

#print(W.map[0].search_npcs("blacksmith"))
#print(W.map[0].search_exits(4,True))
#print(W.map[0].search_exits(4,True)[1])
#print(W.map[0].search_exits(4))
#print("\n\n")
#print(W.map[0].search_nodes("T2iron"))
#print(W.map[0].search_nodes("T2iron",True))
#ptdr = W.map[0].search_requirements("Golden Key",True)[1]
#print(ptdr)
#print(W.map[0].search_items(ptdr))
W.map[0].store_item("UNITEM",3)
