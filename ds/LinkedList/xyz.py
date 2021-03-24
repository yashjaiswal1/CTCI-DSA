# Approach
# (1) Create an 8x8 array to represent the chessboard with value "O" for all squares initially
# (2) Populate the position of white king and ninja on the board
# (3) Mark all the squares adjacent to white king as "NA" --> not to be considered
# (4) Mark all positions in which the ninja can kill as "X"
# (5) For all kill squares, check if there is any adjacent safe square
# (i) if adjacent safe square is available then update current position as "+"
# (ii) else, do nothing
# (6) Check if an "O" exists which is surrounded by all "+" or "X" --> stalemate (rep. by "S")
# K --> King # Q --> Queen
def ninjaChess2021(king, ninja):
    chessboard = [["O", "O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O", "O"], [
        "O", "O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O", "O"], ["O", "O", "O", "O", "O", "O", "O", "O"]]
    chessboard[ord(king[0]) - 97][king[1] - 1] = "K"
    chessboard[ord(ninja[0]) - 97][ninja[1] - 1] = "N"

    king_i = ord(king[0]) - 97
    king_j = king[1] - 1

    if(king_i + 1 >= 0 and king_i + 1 <= 7):
        chessboard[king_i + 1][king_j] = "NA"

    if(king_i - 1 >= 0 and king_i - 1 <= 7):
        chessboard[king_i - 1][king_j] = "NA"

    if(king_j - 1 >= 0 and king_j - 1 <= 7):
        chessboard[king_i][king_j - 1] = "NA"

    if(king_j + 1 >= 0 and king_j + 1 <= 7):
        chessboard[king_i][king_j + 1] = "NA"

    if(king_i + 1 >= 0 and king_i + 1 <= 7 and king_j + 1 >= 0 and king_j + 1 <= 7):
        chessboard[king_i + 1][king_j + 1] = "NA"

    if(king_i - 1 >= 0 and king_i - 1 <= 7 and king_j - 1 >= 0 and king_j - 1 <= 7):
        chessboard[king_i - 1][king_j - 1] = "NA"

    if(king_i + 1 >= 0 and king_i + 1 <= 7 and king_j - 1 >= 0 and king_j - 1 <= 7):
        chessboard[king_i + 1][king_j - 1] = "NA"

    if(king_i - 1 >= 0 and king_i - 1 <= 7 and king_j + 1 >= 0 and king_j + 1 <= 7):
        chessboard[king_i - 1][king_j + 1] = "NA"
