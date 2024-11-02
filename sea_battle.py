# морской бой
import random

board=[]
ships = 16
coordinates = []
for i in range(ships):
    x = random.randint(0,7)
    y = random.randint(0,7)
    coordinates.append([x, y])

for i in range(8): #создаем поле
    board.append([0,0,0,0,0,0,0,0])
    for i in range (8):
        print(board[i])

def board_print():
    for i in range(8):
            print(board [i])
###################
#print(coordinates)
###################
while ships>0:
    x, y = map(int, input().split())
    if [x,y] in coordinates:
        print("Попал!")
        board[y][x] = "X"
        ships-=1
        board_print()
    else:
        print("Мимо!")
        board_print()