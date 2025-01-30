class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

class Board:
    def __init__(self, n):
        self.size = n
        self.rows = {}
        self.cols = {}
        for i in range(n):
            self.rows[i] = {}
            self.cols[i] = {}
        self.diag = {}
        self.revdiag = {}
        self.set_board()
    def set_board(self):
        self.board = [[' ' for i in range(self.size)] for i in range(self.size)]
        return

    def set_markers(self, marker1, marker2):
        for i in range(n):
            self.rows[i][marker1] = 0
            self.cols[i][marker1] = 0
            self.rows[i][marker2] = 0
            self.cols[i][marker2] = 0
        self.diag[marker1] = 0
        self.revdiag[marker1] = 0
        self.diag[marker2] = 0
        self.revdiag[marker2] = 0
    def __repr__(self):
        s = ''
        for i in self.board:
            s+= '\n' +'| '.join(i) +'\n'
            s+= '-'*5
        return s
    def is_turn_valid(self, x, y):
        if x<0 or x==self.size or y<0 or y==self.size:
            return False
        if self.board[x][y] != ' ':
            return False
        return True
    def check_win(self, player, x, y):
        if not self.is_turn_valid(x, y):
            raise ValueError
        else:
            self.board[x][y] = player.marker
            self.rows[x][player.marker] += 1
            self.cols[y][player.marker] += 1
            if x==y:
                self.diag[player.marker] += 1
            if x+y == self.size-1:
                self.revdiag[player.marker] += 1
            if self.rows[x][player.marker] == self.size or self.cols[y][player.marker] == self.size or self.diag[player.marker] == self.size or self.revdiag[player.marker] == self.size:
                return True
            return False

class Game:
    def __init__(self, player1, player2, n):
        self.player1 = player1
        self.player2 = player2
        self.board = Board(n)
        self.board.set_markers(self.player1.marker, self.player2.marker)
    def play(self):
        win = False
        currturn = 1
        while not win:
            if currturn:
                player = self.player1
            else:
                player = self.player2
            place = input('Enter x,y: ')
            x, y = place.split(' ')
            x, y = int(x), int(y)
            try:
                win = self.board.check_win(player, x,y)
                currturn ^= 1
            except:
                print('Invalid Move')

                continue
            print(self.board)
        print(f'{player.name} Wins!')


player1 = Player('Gigachad Devanshu', 'x')
player2 = Player('Chut Bittu', 'o')
n = 3
game = Game(player1, player2, n)
game.play()
