from dataclasses import dataclass
from typing import List, Optional, Tuple

@dataclass
class Move:
    from_pos: Tuple[int, int]  # (riga, colonna)
    to_pos: Tuple[int, int]
    captured_piece: Optional[object] = None
    promotion_piece: Optional[str] = None

class BoardStandard2Players:

    BOARD_SIZE = 8
    COLORS = ("WHITE", "BLACK")

    def __init__(self):
        self.current_player = BoardStandard2Players.COLORS [0]
        # mat 8x8

    def getLegalMoves(self, color: str) -> list:
        x : int
        y : int
        z : int
        w : int

        legal_moves = [Move(x,y), Move(z,w)]

        # Controlla per ogni cella le mosse legali rispetto al pezzo presente
        # Modifica la lista legal_moves di conseguenza

        return legal_moves

    def nextPlayer(self):
        self.current_player = BoardStandard2Players.COLORS[1 if self.current_player == "white" else 0]

class Piece:
    def __init__(self, color: str, name: str):
        self.color = color
        self.name = name

    def getLegalMoves(self, color: str):

class Rook(Piece):
    # Si può muovere o in orizzontale o in verticale, di qualunque distanza

    def __init__(self, color: str):
        super().__init__(color, "Rook")

    def getLegalMoves(self, color: str):

