from termcolor import colored, cprint
import os
import platform


class Model:
    matrix: list
    winner: str
    board_is_full: bool
    player: int
    error: str

class Controller:
    def __init__(self, model: Model):
        self.model = model

    def start_game(self):
        self.model.winner = ''
        self.model.player = 'X'
        self.model.board_is_full = False
        self.model.matrix =  [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]
        self.model.error = ''

    def _matrix_is_full(self, matrix: list) -> bool:
        self.model.board_is_full = not('-' in matrix[0] or '-' in matrix[1] or '-' in matrix[2])
        
    
    def _valid_win(self, matrix: list) -> bool:
        if matrix[0][0] == matrix[0][1] == matrix[0][2] != '-' or \
        matrix[1][0] == matrix[1][1] == matrix[1][2] != '-' or \
        matrix[2][0] == matrix[2][1] == matrix[2][2] != '-' or \
        matrix[0][0] == matrix[1][0] == matrix[2][0] != '-' or \
        matrix[0][1] == matrix[1][1] == matrix[2][1] != '-' or \
        matrix[0][2] == matrix[1][2] == matrix[2][2] != '-' or \
        matrix[0][0] == matrix[1][1] == matrix[2][2] != '-' or \
        matrix[0][2] == matrix[1][1] == matrix[2][0] != '-':
            return True

    def move(self, move: list):
        try:
            if self.model.matrix[move[0] - 1][move[1] - 1] != "-":
                cprint('\nPlace is occupied. Please take another. \n', 'red')
                return
            else:
                self.model.matrix[move[0] - 1][move[1] - 1] = colored('X', 'blue') if self.model.player == 'X' else colored('O', 'red')
        except:
            self.model.error = 'IndexError'
            return 
        if self._valid_win(self.model.matrix):
            self.model.winner = self.model.player
            return
        if self._matrix_is_full(self.model.matrix):
            self.model.board_is_full = 1
            return 
        self.model.player = 'X' if self.model.player == 'O' else 'O'
    

class View:
    def __init__(self, model: Model, controller: Controller):
        self.model = model
        self.controller = controller
        
    def start(self):
        self.controller.start_game()
        os.system("cls") if platform.system() == 'Windows' else os.system('clear')
        cprint('\n' + 'Game start!', 'green')
        self._update()
        while self.model.winner == '' and self.model.board_is_full == 0:
            move = list(map(int, input().split()))
            controller.move(move)
            self._update()
        cprint('Do you want play one more game? (y/any another key)', 'green')
        if input().strip().lower() == 'y': 
            self.start()
        else:
            cprint('Thanks for game!', 'green')
    def _update(self):
        if self.model.error == 'IndexError':
            cprint('\nError. Input is wrong. Try again', 'red')
            self.model.error = ''
        print('\n' + '\n'.join('\t'.join(map(str, row)) for row in self.model.matrix) + '\n')
        if self.model.winner != '':
            print(f'Game over. Player {colored(self.model.player, "blue" if self.model.player == "X" else "red")} is winner!' '\n')
        elif self.model.board_is_full == 1:
            cprint('Draw!', 'yellow')
        else:
            cprint(f'Current player: {colored(self.model.player, "blue" if self.model.player == "X" else "red")} \n', 'green')
        

model = Model()
controller = Controller(model)
view = View(model, controller)

view.start()
