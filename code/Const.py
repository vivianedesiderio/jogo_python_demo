# C
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'level1Bg0': 0,
    'level1Bg1': 1,
    'level1Bg2': 2,
    'level1Bg3': 3,
    'level1Bg4': 4,
    'level1Bg5': 5,
    'level1Bg6': 6,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1,
}

ENTITY_HEALTH = {
    'level1Bg0': 999,
    'level1Bg1': 999,
    'level1Bg2': 999,
    'level1Bg3': 999,
    'level1Bg4': 999,
    'level1Bg5': 999,
    'level1Bg6': 999,
    'level2Bg1': 999,
    'level2Bg2': 999,
    'level2Bg3': 999,
    'level2Bg4': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,


}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')


# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                  'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                   'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                   'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 40000


# W
WIN_WIDTH = 576
WIN_HEIGHT = 324