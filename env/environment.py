from config import (
        START, GOAL, NORMAL, WALL,
        DEFAULT,
        ACTIONS,
        masToSTR
    )

"""
    TODO: 迷路環境を定義
        5 times 5 マス
        マスの種類
            S : スタート地点
            G : 報酬1 で行動終了
            N : 報酬0 で到達可能マス
            W : 到達不可能マス(要するに壁)
"""

class MazeEnv:
    def __init__(self, env=DEFAULT):
        length = len(env[0])

        if not all([len(e) == length for e in env]):
            raise Exception("与えられた環境が不正です")

        self.env = env
        self.shape = (len(env), length)
        self.states = list(range(self.shape[0] * self.shape[1]))
        self.map = self.transSTR(env)
    
    def transSTR(self, env):
        def _trs(e):
            res = ''
            for mas in e:
                res += masToSTR[mas]
            return res

        return '\n'.join([
            _trs(e) for e in env
        ])
    
    def __getitem__(self, key):
        if type(key) is tuple:
            first, second = key
            return self.env[first][second]

class Maze:
    def __init__(
        self,
        env=DEFAULT
    ):
        self.env = MazeEnv(env)
        self.shape = self.env.shape
        self.states = self.env.states
        self.actions = ACTIONS

        # game info
        self.nowGame = False
        self.now = None
        self.step = None
    
    def initialize(self):
        self.nowGame = False
        self.now = self.findStart()
        self.step = 0

    def action(self, act):
        if self.nowGame is False:
            raise Exception("ゲームをスタートしてください")
        
        nstate, reward, done = self.move(act)
        info = ''
        self.now = nstate
        self.step += 1
        
        if done:
            self.nowGame = False

        return nstate, reward, done, info

    def findStart(self):
        heig, widt = self.shape

        for i in range(heig):
            for j in range(widt):
                if self.env[i, j] == START:
                    return i * heig + j
        
        return -1

    def move(self, act):
        return self.now, 0, False

if __name__ == "__main__":
    env = MazeEnv()
    print(env.map)
    print(env.shape)
    print(env.states)
    
    game = Maze()
    print(
        game.env,
        game.states,
        game.actions
    )