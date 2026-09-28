from dataclasses import dataclass
from typing import List, Optional, Tuple, Any

@dataclass
class Move:
    from_pos: Tuple[int, int]  # (riga, colonna)
    to_pos: Tuple[int, int]
    captured_piece: Optional[object] = None
    promotion_piece: Optional[str] = None

class BoardStandard2Players:

    BOARD_SIZE = 8
    COLORS = ("WHITE", "BLACK")
    WHITE_IN_CHECK = False
    BLACK_IN_CHECK = False

    def __init__(self):
        self.current_player = BoardStandard2Players.COLORS [0]
        self.move_history: list[object] = []
        self.pieces: list[object] = []

        # Generazione board 8x8
        rook_w_1 = Rook("white", [0,0])
        horse_w_1 = Horse("white", [0,1])
        bishop_w_1 = Bishop("white", [0,2])
        queen_w_1 = Queen("white", [0,3])
        king_w_1 = King("white", [0,4])
        bishop_w_2 = Bishop("white", [0,5])
        horse_w_2 = Horse("white", [0,6])
        rook_w_2 = Rook("white", [0,7])
        pawn_w_1 = Pawn("white", [1,0])
        pawn_w_2 = Pawn("white", [1,1])
        pawn_w_3 = Pawn("white", [1,2])
        pawn_w_4 = Pawn("white", [1,3])
        pawn_w_5 = Pawn("white", [1,4])
        pawn_w_6 = Pawn("white", [1,5])
        pawn_w_7 = Pawn("white", [1,6])
        pawn_w_8 = Pawn("white", [1,7])
        self.pieces.append(rook_w_1, horse_w_1, bishop_w_1, queen_w_1, king_w_1, bishop_w_2, horse_w_2, rook_w_2, pawn_w_1, pawn_w_2, pawn_w_3,
                           pawn_w_4, pawn_w_5, pawn_w_6, pawn_w_7, pawn_w_8)

        rook_b_1 = Rook("black", [7, 0])
        horse_b_1 = Horse("black", [7, 1])
        bishop_b_1 = Bishop("black", [7, 2])
        queen_b_1 = Queen("black", [7, 3])
        king_b_1 = King("black", [7, 4])
        bishop_b_2 = Bishop("black", [7, 5])
        horse_b_2 = Horse("black", [7, 6])
        rook_b_2 = Rook("black", [7, 7])
        pawn_b_1 = Pawn("black", [6, 0])
        pawn_b_2 = Pawn("black", [6, 1])
        pawn_b_3 = Pawn("black", [6, 2])
        pawn_b_4 = Pawn("black", [6, 3])
        pawn_b_5 = Pawn("black", [6, 4])
        pawn_b_6 = Pawn("black", [6, 5])
        pawn_b_7 = Pawn("black", [6, 6])
        pawn_b_8 = Pawn("black", [6, 7])
        self.pieces.append(rook_b_1, horse_b_1, bishop_b_1, queen_b_1, king_b_1, bishop_b_2, horse_b_2, rook_b_2, pawn_b_1, pawn_b_2, pawn_b_3,
                           pawn_b_4, pawn_b_5, pawn_b_6, pawn_b_7, pawn_b_8)

    def getAllLegalMoves(self, piece: object, ) -> list:

        all_legal_moves: List[Tuple[Any, Tuple[Tuple[int, int], ...]]] = []

        for piece in self.pieces:
            all_legal_moves.append(piece, piece.getLegalMoves(self))

        return all_legal_moves

    def nextPlayer(self):
        self.current_player = BoardStandard2Players.COLORS[1 if self.current_player == "white" else 0]

class Piece:
    def __init__(self, color: str, name: str, location: Tuple[int, int]):
        self.color = color
        self.name = name
        self.location = location

class Rook(Piece):
    # Si può muovere o in orizzontale o in verticale, di qualunque distanza

    def __init__(self, color: str, location: Tuple[int, int]):
        super().__init__(color, "Rook", location)

    def getLegalMoves(self, board: object) -> tuple:


class Bishop(Piece):
    def __init__(self, color: str, location: Tuple[int, int]):
        super().__init__(color, "Bishop", location)

    def getLegalMoves(self, board: object) -> tuple:

class King(Piece):
    def __init__(self, color: str, location: Tuple[int, int]):
        super().__init__(color, "King", location)

    def getLegalMoves(self, board: object) -> tuple:

class Queen(Piece):
    def __init__(self, color: str, location: Tuple[int, int]):
        super().__init__(color, "Queen", location)

    def getLegalMoves(self, board: object) -> tuple:

class Pawn(Piece):
    def __init__(self, color: str, location: Tuple[int, int]):
        super().__init__(color, "Pawn", location)

    def getLegalMoves(self, board: object) -> tuple:

class Horse(Piece):
    def __init__(self, color: str, location: Tuple[int, int]):
        super().__init__(color, "Horse", location)

    def getLegalMoves(self, board: object) -> tuple:
