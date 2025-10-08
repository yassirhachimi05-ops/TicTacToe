import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self,gamecorr):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, gamecorr):
        square = random.choice(gamecorr.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, gamecorr):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. input move (0-8):")
            try:
                val = int(square)
                if val not in gamecorr.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("invalid square. Try again")
        return val 
    
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, gamecorr):
        if len(gamecorr.available_moves()) == 9:
            square = random.choice(gamecorr.available_moves()) 
        
        else:
            square = self.minimax(gamecorr, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        if state.current_winner == other_player:
            return {'position': None, 'score': 1*(state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        
        elif not state.empty_squares(): # no empty squares
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = { 'position': None, 'score': -math.inf}
        else:
            best = { 'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # step1: make a move , try that spot
            state.make_move(possible_move, player)
            # step2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player) # now, we alternate players
            
            # step3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            # step4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
            
        return best


        

            