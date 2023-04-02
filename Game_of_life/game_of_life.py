import numpy as np
from random import randint
from Game import Game
from datetime import datetime
SIZE = 16 ** 2

SIZE += 2
np_field = np.zeros(SIZE * SIZE, dtype = int).reshape(SIZE,SIZE)
for i in range(1, (SIZE - 1)):
    for j in range(1, (SIZE - 1)):
        np_field[i][j] = randint(0,1) 
np_tmp = np.zeros(SIZE * SIZE, dtype = int).reshape(SIZE,SIZE)
ls_field = [list(x) for x in np_field]
ls_tmp = [list(x) for x in np_tmp]
print('Done field') 
g_np = Game(np_field, np_tmp, SIZE, SIZE, cycles = 128)
g_ls = Game(ls_field, ls_tmp, SIZE, SIZE, cycles = 128)

start_time = datetime.now()
g_np.game()
print(datetime.now() - start_time)
start_time = datetime.now()
g_ls.game()
print(datetime.now() - start_time)
