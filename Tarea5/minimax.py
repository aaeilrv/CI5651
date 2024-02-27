from math import inf

FIRST_PLAYER = "|"
SECOND_PLAYER = "-"
CROSS = "+"

def first(state, n, alpha, beta):
    if n == 0 or state.sucessors(FIRST_PLAYER) == []:
        return state.evaluate(FIRST_PLAYER)
    else:
        best = -inf
        for x in state.sucessors(FIRST_PLAYER):
            best = max(best, second(x, n - 1, alpha, beta))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    
def second(state, n, alpha, beta):
    if n == 0 or state.sucessors(SECOND_PLAYER) == []:
        return state.evaluate(SECOND_PLAYER)
    else:
        best = inf
        for x in state.sucessors(SECOND_PLAYER):
            best = min(best, first(x, n - 1, alpha, beta))
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
    
class config:
    def __init__(self):
        self.board = [''] * 9
        self.last_move = None

    def __repr__(self):
        return f"{self.board}"
    
    def get_board(self):
        for i in range(0, 9, 3):
            print(self.board[i], self.board[i + 1], self.board[i + 2])
    
    def winning_pos(self):
        if self.board[0] == self.board[1] == self.board[2] and self.board[0] == CROSS or \
            self.board[3] == self.board[4] == self.board[5] and self.board[3] == CROSS or \
            self.board[6] == self.board[7] == self.board[8] and self.board[6] == CROSS:
            return True
        
        if self.board[0] == self.board[3] == self.board[6] and self.board[0] == CROSS or \
            self.board[1] == self.board[4] == self.board[7] and self.board[1] == CROSS or \
            self.board[2] == self.board[5] == self.board[8] and self.board[2] == CROSS:
            return True
        
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] == CROSS or \
            self.board[2] == self.board[4] == self.board[6] and self.board[2] == CROSS:
            return True
        
        return False
    
    def available_positions(self, current_player):
        available = []
        for i, pos in enumerate(self.board):
            if pos == '':
                available.append(i)
            if pos == SECOND_PLAYER and current_player == FIRST_PLAYER and self.last_move != i:
                available.append(i)
            if pos == FIRST_PLAYER and current_player == SECOND_PLAYER and self.last_move != i:
                available.append(i)

        return available
    
    def sucessors(self, current_player):
        succ = []
        for i in self.available_positions(current_player):
            new_config = config()
            new_config.board = self.board[:]
            new_config.last_move = i

            if new_config.board[i] == '':
                new_config.board[i] = current_player

            elif new_config.board[i] == SECOND_PLAYER and current_player == FIRST_PLAYER:
                new_config.board[i] = CROSS
                
            elif new_config.board[i] == FIRST_PLAYER and current_player == SECOND_PLAYER:
                new_config.board[i] = CROSS
            
            succ.append(new_config)
        return succ        

    def evaluate(self, current_player):
        if self.winning_pos():
            if current_player == FIRST_PLAYER:
                return -1
            elif current_player == SECOND_PLAYER:
                return 1
        else:
            return 0
        
c = config()
print(second(c, 100, -inf, inf))
