#🟩🌲🟦🏥🏪🔥🚁🟫 image.png

from utils import randbool
from utils import randcell
from utils import randcell_2
from clouds import Clouds

CELL_TYPES = '🟩🌲🟦🏥🏪🔥'
TREE_BONUS = 100
UPGRADE_COST = 5000
LIFE_COST = 1000
class Map:
    
    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5
            
    def update_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
        for i in range(10):     
            self.add_fire()   
            
    def generate_shop(self):                 
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4
        
    def generate_hospital(self):                 
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3    
        else:
            self.generate_hospital()
                    
    def generate_tree(self):    # Генератор дерева
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if(self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1
        
    def generate_river(self, l):# Генерация рек
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell_2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_bounds(rx2, ry2)):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1
    # Рандом - mxr        отсечка - r 
    def generate_forest(self, r, mxr): # Генерация леса
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1
        
    def print_map(self, helico, clouds):
        print('🟫' * (self.w + 2))
        for ri in range(self.h):
            print('🟫', end="")
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if (clouds.cells[ri][ci] == 1):
                    print('', end='')
                elif (clouds.cells[ri][ci] == 2):   
                    print('', end='')
                if(helico.x == ri and helico.y == ci):
                    print('🚁', end='')
                elif (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")
            print('🟫') # Перенос после каждого ряда
        print('🟫' * (self.w + 2))
    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True 
    
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range (w)] for j in range (h)]
        self.generate_forest(3, 10) # Лес
        self.generate_river(10) # река
        self.generate_river(10) # река
        self.generate_shop()
        self.generate_hospital()
        #self.clouds = Clouds(w, h)
        
        
    def process_helicopter(self, helico):
        c = self.cells[helico.x][helico.y]
        if (c == 2):
            helico.tank = helico.mxtank
        if (c == 5 and helico.tank > 0):
            helico.tank -= 1  
            helico.score += TREE_BONUS
            self.cells[helico.x][helico.y] = 1
        if (c == 4 and helico.score >= UPGRADE_COST):
            helico.mxtank += 1
            helico.score -= UPGRADE_COST
        if (c == 3 and helico.score >= LIFE_COST):
            helico.lives += 1
            helico.score -= LIFE_COST
            