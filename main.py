from map import Map
import time
import os
from hellcopter import Hellcopter as Helico
from pynput import keyboard
from clouds import Clouds
TICK_SLEEP = 0.1
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10
CLOUDS_UPDATE = 30

tmp = Map(MAP_W, MAP_H) # размер карты 
clouds = Clouds(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)

#
MOVES = {'w': (-1,0), 'd': (0,1), 's': (1,0), 'a': (0,-1)}
def process_key(key):
    global helico
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
        
    
Listener = keyboard.Listener(
    on_press = None,
    on_release = process_key,)
Listener.start()
#
    
tick = 1

while True:
    os.system('cls') # для MAC OS "clear"
    tmp.process_helicopter(helico)
    helico.print_menu()
    tmp.print_map(helico, clouds)
    print("TICK", tick)
    
    tick += 1
    time.sleep(TICK_SLEEP) #Передаёт задержку кадра
    if (tick % TREE_UPDATE == 0):
        tmp.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        tmp.update_fires()
    if (tick % CLOUDS_UPDATE == 0):
         clouds.update()