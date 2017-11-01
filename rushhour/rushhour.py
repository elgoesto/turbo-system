
import numpy as np
import cs50


#constants
BSIZE = 6

# make board of zeros
board = np.zeros((6,6))

# make cars, horizontal and verical, niet meer nodig
# car2h = np.array([1,1])
# car2v = np.array([[1],[1]])


# make function to place cars on the board
# set coordinate and orintation
# orientation 1 = vertical, 2 = horizontal
def place(y, x, orient, size, car_id):

    # Place car vertical
    if orient == 1:
        board[y:size+y,x] = car_id

    # Place car horizontal
    elif orient == 2:
        board[y,x:size+x] = car_id

    else:
        print(error)

# examples how to place cars
place(2, 3, 1, 2, 12)
place(0, 3, 2, 3, 6)


print(board)

