from fastapi import APIRouter
from pydantic import BaseModel 
from models.board import Board
from models.piece import AmbigPiece
from services.domain.analysis import mate_analyze
from models.virtual_board import VirtualBoard
from models.game_master import GameMaster

router = APIRouter(
    prefix="/mate",
    tags=["mate"],
    responses={404: {"description": "Not found!"}}, 
)

class PostedBoard(BaseModel):
    board: list

@router.post('/analyze')
def analyze(param: PostedBoard):
    boardObj = Board()

    boardObj.set_side('white')
    boardObj.set_board(param.board)
    gm = GameMaster()

    virtualBoard = VirtualBoard(param.board, 'white', gm)
    matingMoves = mate_analyze.search_mate(virtualBoard, param.board, 'white', gm, 0)

    print(matingMoves)

    return {"message": "checkmate analyze"}