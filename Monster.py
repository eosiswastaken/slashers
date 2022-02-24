import Tools
import random

class Monster:
    def __init__(self,hp,atk,defense,cc,cd,name,loot,lvl):
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.cc = cc
        self.cd = cd
        self.name = name
        self.loot = loot
        self.lvl = lvl






Monsters = {
    "Zombie" : Monster(100,10,5,5,200,"Zombie",[["Rottn flesh",[1,3],50,"Gold",[20,200],100,"Fabric",[2,7],25]],4),
    "Skeleton" : Monster(100,10,5,5,200,"Skeleton",[["Bone",[1,3],50,"Gold",[20,200],100]],4)
    
    }
#print(Monsters["Zombie"].loot)
#print(Monsters["Zombie"].attack())
#print(Monsters["Zombie"].defend())
print("allo")
