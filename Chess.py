#with pandas or not?
import pandas as pd
class chess:
    def __init__(self):#initilaising the board
        board = pd.DataFrame([['0000']*8]*8, columns=[chr(97+i) for i in range(8)])
        #simplify this later
        board.loc[1,:] = 'b_pn'
        board.loc[6,:] = 'w_pn'

        board.loc[0,'a'] ='b_rk'
        board.loc[0,'h'] ='b_rk'
        board.loc[7,'a'] ='w_rk'
        board.loc[7,'h'] = 'w_rk'

        board.loc[0,'b'] ='b_kt'
        board.loc[0,'g'] ='b_kt'
        board.loc[7,'b'] ='w_kt'
        board.loc[7,'g'] = 'w_kt'

        board.loc[0,'c'] ='b_bp'
        board.loc[0,'f'] ='b_bp'
        board.loc[7,'c'] ='w_bp'
        board.loc[7,'f'] = 'w_bp'

        board.loc[0,'d'] ='b_qn'
        board.loc[0,'e'] ='b_kg'
        board.loc[7,'d'] ='w_qn'
        board.loc[7,'e'] = 'w_kg'

        print(board)
    #need to create a method for the pieces to move limitations
    '''
    should there be an indication of forward?

    pn - pwan - first move 2 or 1 then rest of game 1 forwards (1diag for atk) - promotes to another piece except king at the end of the board
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

chess()
