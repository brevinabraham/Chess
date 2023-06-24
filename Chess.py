import pandas as pd


class Chess:
    def gameinit(self):
        self.outcomestatus = False
        while self.outcomestatus == False:
            for player in ['w','b']:
                self.gamestart(player)


    def gamestart(self, player):
        print(self.board)
        self.updatedboard = False
        while self.updatedboard == False:
            self.playermove = input(player + " input move: \n")
            self.update(player, self.playermove[0:3],self.playermove[3:5], self.playermove[5:7])

    def update(self, player, piece, movefrom, moveto):
        if player == piece[0]:
            validity = self.is_valid(piece[1:3],player,movefrom,moveto)
            if validity:
                deletestatus = self.delete(piece, movefrom)
                if deletestatus == True:
                    addstatus = self.add(piece, moveto)
                    self.updatedboard = True
            else:
                print("Invalid piece move")
        else:
            print("check input")

    def is_valid(self,piece,colour,start,end):
        if piece == 'pn':
            validity = Pawn.valid_move(self,colour,start,end)
        elif piece == 'rk':
            validity = Rook.valid_move(self,colour,start,end)
        elif piece == 'kt':
            validity = Knight.valid_move(self,colour,start,end)

        
        return validity
        

    def add(self, piece, moveto):#need to add conditions on the pieces to see if it can be added
        self.board.loc[int(moveto[1]),moveto[0]] = piece
        return True
        
    def delete(self, piece, movefrom):
        if self.board.loc[int(movefrom[1]),movefrom[0]] == piece:
            self.board.loc[int(movefrom[1]),movefrom[0]] = '0000'
            return True

    def __init__(self):#initilaising the self.board
        self.board = pd.DataFrame([['0000']*8]*8, columns=[chr(97+i) for i in range(8)])
        #simplify this later
        self.board.loc[1,:] = 'bpn'
        self.board.loc[6,:] = 'wpn'

        self.board.loc[0,'a'] ='brk'
        self.board.loc[0,'h'] ='brk'
        self.board.loc[7,'a'] ='wrk'
        self.board.loc[7,'h'] = 'wrk'

        self.board.loc[0,'b'] ='bkt'
        self.board.loc[0,'g'] ='bkt'
        self.board.loc[7,'b'] ='wkt'
        self.board.loc[7,'g'] = 'wkt'

        self.board.loc[0,'c'] ='bbp'
        self.board.loc[0,'f'] ='bbp'
        self.board.loc[7,'c'] ='wbp'
        self.board.loc[7,'f'] = 'wbp'

        self.board.loc[0,'d'] ='bqn'
        self.board.loc[0,'e'] ='bkg'
        self.board.loc[7,'d'] ='wqn'
        self.board.loc[7,'e'] = 'wkg'

        self.gameinit()

    #need to create a method for the pieces to move limitations
    '''
    should there be an indication of forward?

    pn - pwan - first move 2 or 1 then rest of game 1 forwards (1diag for atk) - promotes to another piece except king at the end of the self.board
    rk - rock - horizontal or vertical
    kt - kinght - L shape: 3 hori or vert
    bp - bishop - diagonal
    qn - queen - hori or vert or diag
    kg - king - one hori or vert or diag


    how to move the pieces, moving by +number of spaces in row or col
        can also check diagonal
            e.g. pn from d6 to d4(6-2) moving 2 spaces up
            e.g. pn from d6 to e5 (ord(d)+1)(6-1) moving 1 diag to the right 

    let the player make the move and check if inside or outside constrants first then check if anyhting blobking the way

    always check if check is inplace then player must move such that king is outof harm
    '''
    #need to create the pieces themselves

class Pawn(Chess):
    def valid_move(self,colour,start,end):
        direction = -1 if colour == 'w' else 1

        rankchange = ord(end[0]) - ord(start[0])
        filechange = int(end[1]) - int(start[1])

        if filechange == direction and rankchange == 0 and self.board.loc[int(end[1]),end[0]] == '0000':
            return True
        elif filechange == 2*direction and rankchange == 0 and self.board.loc[int(end[1]),end[0]] == '0000':
            if (direction == -1 and int(start[1]) == 6) or (direction == 1 and int(start[1]) == 1):
                return True
        elif abs(rankchange) == 1 and abs(filechange) == 1 and self.board.loc[int(end[1]),end[0]] != '0000' \
         and self.board.loc[int(end[1]),end[0]][0] != colour:
            if (direction == -1 and filechange < 0) or \
                 (direction == 1 and filechange > 0):
                return True
        
        return False
    
class Rook(Chess):
    def valid_move(self,colour,start,end):
        if start[0] == end[0] or start[1] == end[1]:

            rankchange = ord(end[0]) - ord(start[0])
            filechange = int(end[1]) - int(start[1])
            
            step_rank = 0 if rankchange == 0 else int(rankchange / abs(rankchange))
            step_file = 0 if filechange == 0 else int(filechange / abs(filechange))

            rank = ord(start[0]) + step_rank
            file = int(start[1]) + step_file
            move = chr(rank)+str(file)
            while move != end:
                if self.board.loc[file,chr(rank)] != '0000':
                    return False
                rank += step_rank
                file += step_file
                move = chr(rank)+str(file)
            
            if self.board.loc[int(end[1]),end[0]] == '0000' or self.board.loc[int(end[1]),end[0]][0] != colour:
                return True

        return False

class Knight(Chess):
    def valid_move(self,colour,start,end):
        rankchange = abs(ord(end[0]) - ord(start[0]))
        filechange = abs(int(end[1]) - int(start[1]))

        if (rankchange == 2 and filechange == 1) or (rankchange == 1 and filechange == 2):
            if self.board.loc[int(end[1]),end[0]] == '0000' or self.board.loc[int(end[1]),end[0]][0] != colour:
                return True
        return False


Chess()


