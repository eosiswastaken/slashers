import Player

class Room:
    def __init__(self,id,name,contents,description,requirements,exits):
        self.id = id # (int) the room ID
        self.name = name# (str) the room name
        self.contents = contents# (dict) the contents of the room (NPCs nodes interactables gold items monsters etc)
        self.desc = description# (str) short description of the room
        self.exits = exits# (list) a list of the exits to get to anoter room
        self.reqs = requirements

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_contents(self):
        return self.contents

    def get_description(self):
        return self.desc

    def get_requirements(self):
        return self.reqs

    def get_exits(self):
        return self.exits

    def search_exits(self,id,pos=False):
        if id in self.exits and not pos:
            return True
        elif id in self.exits and pos:
            return True,self.exits.index(id)
        else:
            return False

    def search_npcs(self,key):
        if key in self.contents["npcs"]:
            return True
        else:
            return False


    def search_nodes(self,key,amount=False):
        if key in self.contents["nodes"] and not amount:
            return True
        elif key in self.contents["nodes"] and amount:
            return True,self.contents["nodes"][key]
        else:
            return False

    def search_interactables(self,key):
        if key in self.contents["interactables"]:
            return True
        else:
            return False

    def search_stations(self,key,amount=0):
        if key in self.contents["stations"]:
            return True
        else:
            return False

    def search_items(self,key,amount=False):
        if key in self.contents["items"] and not amount:
            return True
        elif key in self.contents["items"] and amount:
            return True,self.contents["items"][key]
        else:
            return False

    def search_monsters(self,key,amount=False):
        if key in self.contents["monsters"] and not amount:
            return True
        elif key in self.contents["monsters"] and amount:
            return True,self.contents["monsters"][key]
        else:
            return False

    def search_gold(self,amount=False):
        if self.contents["gold"] != 0 and not amount:
            return True
        elif self.contents["gold"] != 0 and amount:
            return True,self.contents["gold"]
        else:
            return False

    def search_requirements(self,key,details=False):
        if key in self.reqs and not details:
            return True
        elif key in self.reqs and details:
            return True,list(self.reqs.keys())[list(self.reqs.values()).index(self.reqs[key])],self.reqs[key]
        else:
            return False

    def store_item(self,item,quantity):
                if item.title() in Player.P.inv:
                    if item.title() in self.contents["items"]:
                        self.contents["items"][item.title()] += quantity
                        Player.P.remove_item(item.title(),quantity)
                        print("You stored " + str(quantity) + " " + str(item.title()) + " in your the room, there is now a total of " + str(self.contents["items"][item.title()]) + " " + str(item.title()) + " in the room")
                    else:
                        self.contents["items"][item.title()] = quantity
                        Player.P.remove_item(item,quantity)
                        print("You stored " + str(quantity) + " " + str(item.title()) + " in the room")

    def retrieve_item(self,item,quantity):
        if item.title() in self.contents["items"]:
            Player.P.give_item(item.title(),quantity)
            if quantity >= self.contents["items"][item.title()]:
                del self.contents["items"][item.title()]
                print("You took the last " + str(quantity) + " " + str(item.title()) + " in the room, there is no more " + str(item.title()) + " in the room.")
            else:
                self.contents["items"][item.title()] -= quantity
                print("You took " + str(quantity) + " " + str(item.title()) + " in the room, there is " + str(self.contents["items"][item.title()]) + " " + str(item.title()) + " left in the room")

    def check_item(self,item):
        if item.title() in self.contents["items"]:
            return self.contents["items"][item.title()]

exampleRoom = Room(1,"The Example Room",{
"npcs" : { # no caps
    "blacksmith" : True,
    "banker" : True
},
"nodes" : { # caps only for tier
    "T1tree" : 12,
    "T2tree" : 6,
    "T2iron" : 10
},
"interactables" : { # no caps
    "fountain" : True
},
"stations" : { # no caps
    "sewing" : True,
    "forge" : True
},
"items" : { # capitalize first letter of each word only
    "Torch" : 3,
    "Golden Key" : 1
},
"monsters" : { # capitalize first letter of each word only
    "Zombie" : 4,
    "Skeleton" : 1
},
"gold" : 123

},"You arrive in an old village with a few NPCs, some trees, some iron ore on the side of the mountain and a crypt with zombies and skeletons",
{"Golden Key" : 1},
[1,2,3,4,-1,-1]) # Nord , Sud , Ouest , Est , Haut , Bas 0/1/2/3/4/5





map = {
    0 : exampleRoom,
    1 : exampleRoom,
    2 : exampleRoom,
    3 : exampleRoom,
    4 : exampleRoom,
    5 : exampleRoom,
    6 : exampleRoom
}
