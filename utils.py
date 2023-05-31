from random import randint as rand #Для вызова рандом - rand

def randbool(r, mxr):
    t = rand(0, mxr)
    return (t <= r)

def randcell(w, h):
    tw = rand(0, w -1)
    th = rand(0, h -1)
    return (th, tw)
#0-на верх: 1- направо: 2-вниз: 3-налево:
def randcell_2(x, y):
    noves = [(-1,0), (0,1), (1,0), (0,-1)] # первое число это столбец, второе строка
    t = rand(0,3)
    dx, dy = noves[t][0], noves[t][1]
    return(x + dx, y + dy)