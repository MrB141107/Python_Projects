import random
from time import sleep
from termcolor import colored
from copy import deepcopy
import config as cfg
from base_card import Card
from base_board import Board

'''
A rough and simple text-based OOP implementation of Hearthstone Battlegrounds
game; not the whole game but rather card's fight simulation of the game. The
code is well extensible, so we can add new features. For example, it woudn't
be so hard to add 'is_reborn' property to Card and accordingly change the
game's logic.

By default, the code creates Board, populate it with random Cards, and runs
Game.

You can create you own Board and populate with any Cards.
Example:
    my_board = Board()
    my_board.top = [Card(attack=40, health=65, is_bubbled=True),
                    Card(attack=7, health=4, is_bubbled=True, is_poison=True),
                    Card(attack=2, health=2),
                    Card(attack=2, health=2)]

    my_board.bottom = [Card(attack=7, health=4, is_bubbled=True,
                            is_poison=True),
                       Card(attack=7, health=4, is_bubbled=True,
                            is_poison=True),
                       Card(attack=8, health=10)]

    game = Game(board=my_board)
    game.run()

All cards must be unique instances of the class. It means we cannot do this:
    card = Card(attack=4, health=6)
    board = Board()
    for i in range(7):
        board.top.append(card)
        board.bottom.append(card)

But we can do this:
    card_stats = {'attack': 4, 'health': 6}
    board = Board()
    for i in range(7):
        board.top.append(Card(**card_stats))
        board.bottom.append(Card(**card_stats))
    game = Game(board=board)
    game.run()
'''


class Game:
    def __init__(self, board: Board = None, verbalize: bool = True):
        self.is_top_move = True  # is it top-board's turn
        self.verbalize = verbalize  # if set to True then we print game text
        self.pre_calculate = True

        if board is None:
            new_board = Board()
            new_board.populate_with_random_cards()
            self.board = new_board
        else:
            self.board = board

    def calculate_chances(self):
        self.verbalize = False

        top_wins = 0
        btm_wins = 0
        tie = 0

        starting_board = deepcopy(self.board)
        self.board.show(0)

        for i in range(1000):
            self.board = deepcopy(starting_board)
            result = self.run(is_delay=False, is_print_board=False,
                              calculate=False)

            if result == 'Top Wins':
                top_wins += 1
            elif result == 'Bottom Wins':
                btm_wins += 1
            else:
                tie += 1

        result = f"Top Wins: {top_wins / 10}%, Tie: {tie / 10}%, " \
                 f"Bottom Wins: {btm_wins / 10}%"
        print(result)
        print()
        self.board = deepcopy(starting_board)
        self.verbalize = True
        self.is_top_move = True

    def run(self, is_delay=True, is_print_board=True, calculate=True) -> None:
        '''Game loop with DELAY in seconds'''

        if calculate:
            self.calculate_chances()

        iter_num = 0
        if is_print_board:
            self.board.show(iter_num)

        while self.board.top and self.board.bottom:
            iter_num += 1
            text = ""
            if is_delay:
                sleep(cfg.DELAY)

            try:
                attacker, attacked, brd, opp_brd = self.next_cards()
            except TypeError:
                game_result = "It's a tie"
                if self.verbalize:
                    print('\n' + game_result + '!\n')
                return game_result

            atkr_idx = brd.index(attacker)
            atkd_idx = opp_brd.index(attacked)

            # Generating the text for printing -------------------------------
            text = text + f"Card {str(attacker)} at position {atkr_idx}" \
                          f" attacks {str(attacked)} at position {atkd_idx}."
            # ----------------------------------------------------------------

            attacker.do_attack(attacked)

            # Generating the text for printing -------------------------------
            attacker_death_str = " Attacker dies." * attacker.is_dead
            attacked_death_str = " Attacked card dies." * attacked.is_dead
            text = text + attacker_death_str + attacked_death_str

            if attacker_death_str == '':
                text = text + f" Now the attacker stats is {attacker}."
            if attacked_death_str == '':
                text = text + f" Now the attacked card stats is {attacked}."

            if len(text) > self.board.max_space:
                text = (text[:self.board.max_space] + '\n'
                        + text[self.board.max_space:])
            # ----------------------------------------------------------------

            if self.verbalize:
                print('\n' + text + '\n')

            if attacker.is_dead:
                summon = attacker.after_death()
                brd.pop(atkr_idx)
                if summon is not None:
                    brd.insert(atkr_idx, summon)

            if attacked.is_dead:
                summon = attacked.after_death()
                opp_brd.pop(atkd_idx)
                if summon is not None:
                    opp_brd.insert(atkd_idx, summon)

            if is_print_board:
                self.board.show(iter_num)

        game_result = ''
        if self.board.top:
            game_result = 'Top Wins'
        elif self.board.bottom:
            game_result = 'Bottom Wins'
        else:
            game_result = "It's a tie"

        if self.verbalize:
            print('\n' + game_result + '!\n')

        return game_result

    def next_cards(self) -> (Card, Card, list[Card], list[Card]):
        '''Returns the card that attacks, the card that is being attacked by
        the first card and pointers to their boards respectively'''

        # Selecting correct boards based on 'is_top_move' attribute
        brd = self.board.top if self.is_top_move else self.board.bottom
        opp_brd = self.board.bottom if self.is_top_move else self.board.top

        is_brd_cant_attack = all([card.attack <= 0 for card in brd])
        is_opp_brd_cant_attack = all([card.attack <= 0 for card in brd])

        if is_brd_cant_attack and not is_opp_brd_cant_attack:
            self.is_top_move = not self.is_top_move
            return self.next_cards()
        elif is_brd_cant_attack and is_opp_brd_cant_attack:
            return None

        taunts = [i for i in range(len(opp_brd)) if opp_brd[i].is_taunt]

        # Selecting the first in order card that has not attacked yet
        # Then randomly selecting the attacked card
        for card in brd:
            if not card.has_attacked and card.attack > 0:
                card.has_attacked = True
                self.is_top_move = not self.is_top_move

                if not taunts:
                    attacked_card = random.choice(opp_brd)
                else:
                    attacked_card = opp_brd[random.choice(taunts)]

                return (card, attacked_card, brd, opp_brd)

        '''If all cards have attacked then set all card's properties
        'has_attacked' to false and try again to call this funciton'''
        for card in brd:
            card.has_attacked = False
        return self.next_cards()
