# マス
START  = 0
GOAL   = 1
NORMAL = 2
WALL   = 3

DEFAULT = [
    [START, NORMAL, NORMAL],
    [NORMAL, WALL, GOAL],
    [NORMAL, NORMAL, NORMAL]
]

masToSTR = {
    START  : 'S',
    GOAL   : 'G',
    NORMAL : 'N',
    WALL   : 'W'
}

# 行動
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

ACTIONS = (UP, DOWN, RIGHT, LEFT)