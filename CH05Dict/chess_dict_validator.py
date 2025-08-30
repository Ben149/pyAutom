def isValidChessBoard(board):
    valid_positions = [str(n) + l for n in range(1, 9) for l in "abcdefgh"]
    valid_pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    # Counters
    piece_count = {'w': 0, 'b': 0}
    pawns_count = {'w': 0, 'b': 0}
    kings_count = {'w': 0, 'b': 0}

    for position, piece in board.items():
        # 1. Position must be valid
        if position not in valid_positions:
            return False

        # 2. Piece must be valid
        if len(piece) < 2:
            return False
        color, name = piece[0], piece[1:]
        if color not in ['w', 'b'] or name not in valid_pieces:
            return False

        # 3. Count pieces
        piece_count[color] += 1
        if name == 'pawn':
            pawns_count[color] += 1
        if name == 'king':
            kings_count[color] += 1

    # 4. Constraints
    if piece_count['w'] > 16 or piece_count['b'] > 16:
        return False
    if pawns_count['w'] > 8 or pawns_count['b'] > 8:
        return False
    if kings_count['w'] != 1 or kings_count['b'] != 1:
        return False

    return True

board = {
    '1h': 'bking',
    '6c': 'wqueen',
    '2g': 'bbishop',
    '5h': 'bqueen',
    '3e': 'wking'
}

print(isValidChessBoard(board))  # Should return True