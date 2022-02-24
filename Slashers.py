###########################################
#           ~  PLAINS OF WYN  ~           #
###########################################
# A game by Antoine.c | Project started November 1st of 2020 | Genre: Text-based RPG (with interestings mechanics) #
# Made as my first python beginner project | Coded with <3 with VSCode  | AMA: Eosis#6008 on discord #



#VARIABLES ET IMPORTS
import sys,os
import Npc,Player,World,Tools,Monster,Combat

title = ("""

 $$$$$$\  $$\                     $$\
$$  __$$\ $$ |                    $$ |
$$ /  \__|$$ | $$$$$$\   $$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$\
\$$$$$$\  $$ | \____$$\ $$  _____|$$  __$$\ $$  __$$\ $$  __$$\ $$  _____|
 \____$$\ $$ | $$$$$$$ |\$$$$$$\  $$ |  $$ |$$$$$$$$ |$$ |  \__|\$$$$$$\
$$\   $$ |$$ |$$  __$$ | \____$$\ $$ |  $$ |$$   ____|$$ |       \____$$\
\$$$$$$  |$$ |\$$$$$$$ |$$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |      $$$$$$$  |
 \______/ \__| \_______|\_______/ \__|  \__| \_______|\__|      \_______/

""")
favoriteCommand = "look"
is_admin = False
MOVE_VERBS = ["go","move","walk"]
N_DIRS = ["north","nord","z","n"]
S_DIRS = ["south","sud","s"]
O_DIRS = ["west","ouest","q","w","o"]
E_DIRS = ["east","est","d","e"]
H_DIRS = ["up","haut","u","h"]
B_DIRS = ["down","bas","b"]
PICK_VERBS = ["take","pick","pickup"]
DROP_VERBS = ["drop"]
INVENTORY_VERBS = ["inv","inventory","inventaire"]
ATTACK_VERBS = ["attack","atk","fight"]
TALK_VERBS = ["interact","talk","chat"]
LOOK_VERBS = ["look","examine"]
QUIT_VERBS = ["disconnect","quit","goodbye","quitter","partir"]
FAVORITE_VERBS = ["favorite","fav"]
FAVORITE_TRIGGER = ["a"]
ADMIN_TRIGGER = ["27"]
GIVE_VERBS = ["give"]


class Game:
    def __init__(self):
        pass

    def start_game(self):
        #Tools.Text.line_spacer_print("=")
        #os wait
        print(title)
        #os wait
        #Tools.Text.line_spacer_print("=")
        self.main_loop()

    def main_loop(self):
        while True:
            oui = Slashers.user_input("What do you want to do ?")
            Slashers.parse_string(oui)

    def print_info(self,box,message):
        return str(box).capitalize() + " >> " + str(message)

    def user_input(self,message):
        return input(str(message) + " >>> ").lower()

    def parse_string(self,string):
        cmd = string.split()
        if len(cmd) >= 1:
            if cmd[0] in MOVE_VERBS:
                if len(cmd) >= 2 and cmd[1] in N_DIRS:
                    move = World.W.can_move_to_dir(0)
                    if World.W.can_move_to_dir(0) != False:
                        World.W.move_to(move)
                elif len(cmd) >= 2 and  cmd[1] in S_DIRS:
                    move = World.W.can_move_to_dir(1)
                    if World.W.can_move_to_dir(1) != False:
                        World.W.move_to(move)
                elif len(cmd) >= 2 and  cmd[1] in O_DIRS:
                    move = World.W.can_move_to_dir(2)
                    if World.W.can_move_to_dir(2) != False:
                        World.W.move_to(move)
                elif len(cmd) >= 2 and  cmd[1] in E_DIRS:
                    move = World.W.can_move_to_dir(3)
                    if World.W.can_move_to_dir(3) != False:
                        World.W.move_to(move)
                elif len(cmd) >= 2 and  cmd[1] in H_DIRS:
                    move = World.W.can_move_to_dir(4)
                    if World.W.can_move_to_dir(4) != False:
                        World.W.move_to(move)
                elif len(cmd) >= 2 and  cmd[1] in B_DIRS:
                    move = World.W.can_move_to_dir(5)
                    if World.W.can_move_to_dir(5) != False:
                        World.W.move_to(move)
                else:
                    print("Please enter a valid direction !")
            elif cmd[0] in PICK_VERBS:
                prompt = self.user_input("What do you want to take ?")
                if World.W.map[Player.P.pos].check_item(prompt):
                    World.W.map[Player.P.pos].retrieve_item(prompt,1)
                    print(World.W.map[Player.P.pos].contents["items"])
                else:
                    print("Please enter a valid item !")
            elif cmd[0] in DROP_VERBS:
                prompt = self.user_input("What do you want to drop ?")
                if Player.P.check_item(prompt):
                    World.W.map[Player.P.pos].store_item(prompt,1)
                    print(World.W.map[Player.P.pos].contents["items"])
                else:
                    print("Please enter a valid item !")
            elif cmd[0] in ATTACK_VERBS:
                if len(cmd) > 1 and World.W.map[Player.P.pos].search_monsters(cmd[1].capitalize()):
                    print("Start fight")
                    Combat.F.pve_fight(Player.P,Monster.Monsters[cmd[1].capitalize()])
                else:
                    print("Please enter a valid target to attack !")
                print("allo oui j'attaque'")
            elif cmd[0] in INVENTORY_VERBS:
                print("allo oui je regarde mon inventaire")
                Player.P.print_inventory()
                Player.P.print_gold()
            elif cmd[0] in TALK_VERBS:
                print("allo oui je parle a un PNJ la ! - Bonsoir !")
            elif cmd[0] in QUIT_VERBS:
                quit()
            elif cmd[0] in FAVORITE_VERBS:
                newFav = str(self.user_input("Enter your new favorite command! ('quit' to cancel)"))
                if newFav in QUIT_VERBS:
                    print("Cancelled !")
                else:
                    Player.P.quickCmd = newFav
                    print(newFav)
            elif cmd[0] in FAVORITE_TRIGGER:
                self.parse_string(Player.P.quickCmd)
            elif cmd[0] in ADMIN_TRIGGER:
                print("Please enter a valid command!")
                if Player.P.adminStatus: 
                    Player.P.adminStatus = False
                else:
                    Player.P.adminStatus = True
            elif cmd[0] in GIVE_VERBS and Player.P.adminStatus:
                if len(cmd) > 2:
                    Player.P.give_item(str(cmd[1]),int(cmd[2]))
            elif cmd[0] in LOOK_VERBS:
                print("You look around and you see ",end='')
                for i in World.W.map[Player.P.pos].contents["items"]:
                    print(World.W.map[Player.P.pos].contents["items"][i],end=' ')
                    print(i,end='')
                    print(", ",end='')
                print("in the room.")



            else:
                print("Please enter a valid command !")
            return True





Slashers = Game()
Slashers.start_game()
