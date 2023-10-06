from base_game import Game
from base_board import Board
from base_card import Card

if __name__ == '__main__':
    card1 = {'attack': 1, 'health': 5, 'is_poison': True, 'is_reborn': True}
    card2 = {'attack': 10, 'health': 20}
    card3 = {'attack': 4, 'health': 4}

    board_top = [Card(**card1), Card(**card3)]
    board_bottom = [Card(**card2), Card(**card2)]

    board = Board(top=board_top, bottom=board_bottom)
    game = Game(board=board)
    game.run()

    '''
    # Simple run
    game = Game()
    game.run()
    '''
