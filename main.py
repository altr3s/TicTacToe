class Model:
    matrix: list
    winner: str
    board_is_full: bool
    player: int

class Controller:
    def __init__(self, model: Model):
        self.model = model

    def start_game(self):
        self.model.winner = ''
        self.model.player = 1
        self.model.board_is_full = False
        self.model.matrix =  [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]

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

    def move(self, move):
        if self.model.matrix[move[0] - 1][move[1] - 1] != "-":
            print("Place is occupied. Please take another.")
            return
        else:
            self.model.matrix[move[0] - 1][move[1] - 1] = "X" if self.model.player == 1 else "O"
        if self._valid_win(self.model.matrix):
            self.model.winner = str(self.model.player)
            return
        if self._matrix_is_full(self.model.matrix):
            self.model.board_is_full = 1
            return
        self.model.player = 1 if self.model.player == 2 else 2
    

class View:
    def __init__(self, model: Model, controller: Controller):
        self.model = model
        self.controller = controller
        
    def start(self):
        self.controller.start_game()
        print("Game start")
        self._update()
        while self.model.winner == '' and self.model.board_is_full == 0:
            move = list(map(int, input().split()))
            controller.move(move)
            self._update()
        print('Do you want play one more game? (y/n)?')
        if input() == 'y': 
            self.start()
        else:
            print('Thanks!')
    def _update(self):
        print('\n'.join('\t'.join(map(str, row)) for row in self.model.matrix))
        if self.model.winner != '':
            print(f'Game over. Player {self.model.winner} is winner!')
        elif self.model.board_is_full == 1:
            print('Draw!')
        else:
            print(f'Current player: {self.model.player}')
        


model = Model()
controller = Controller(model)
view = View(model, controller)

view.start()
