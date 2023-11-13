print("Task Date: 11.10.2023")
print("Task 1:\n")

"""
Реалізуйте гру "Хрестики-Нулики" для двох гравців.
Використовуйте словник для представлення гри.
"""

class TicTacToe:
    def __init__(self):
        self.board = {
            '1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '
        }
        self.current_player = 'X'

    def print_board(self):
        print(f"{self.board['1']} | {self.board['2']} | {self.board['3']}")
        print("--+---+--")
        print(f"{self.board['4']} | {self.board['5']} | {self.board['6']}")
        print("--+---+--")
        print(f"{self.board['7']} | {self.board['8']} | {self.board['9']}")

    def make_move(self, position):
        if self.board.get(position) == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move! Please choose an empty position.")

    def check_winner(self):
        winning_combinations = [
            ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
            ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
            ['1', '5', '9'], ['3', '5', '7']
        ]

        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                return self.board[combination[0]]

        if ' ' not in self.board.values():
            return 'Draw'

        return None

game = TicTacToe()

while True:
    game.print_board()

    position = input(f"{game.current_player}, choose a position (1-9): ")
    game.make_move(position)

    winner = game.check_winner()
    if winner:
        game.print_board()
        if winner == 'Draw':
            print("It's a draw!")
        else:
            print(f"Player {winner} wins!")
        break

# main
game = TicTacToe()

while True:
    game.print_board()

    position = input(game.current_player, "choose a position (1-9): ")
    game.make_move(position)

    winner = game.check_winner()
    if winner:
        game.print_board()
        if winner == 'Draw':
            print("It's a draw!")
        else:
            print(f"Player {winner} wins!")
        break