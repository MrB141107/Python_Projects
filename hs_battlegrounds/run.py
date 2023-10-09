from base_game import Game
from base_board import Board
from base_card import Card
from hs_cards import get_cards

if __name__ == '__main__':
    cards = get_cards()  # dict of classes

    board_top = [cards['Annoy-o-Tron'](),
                 cards['Dozy Whelp'](),
                 cards['Micro Mummy']()]

    board_btm = [cards['Annoy-o-Tron'](),
                 cards['Dozy Whelp'](),
                 cards['Micro Mummy']()]

    board = Board(top=board_top, bottom=board_btm)
    game = Game(board=board)
    game.run()

    '''
    # Simple run
    game = Game()
    game.run()
    '''
