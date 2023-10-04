import random
from time import sleep

CARD_TXT_SPACE = 3
BOARD_LENGTH = 7
POISON_PROB = 0.15
BUBBLE_PROB = 0.25
DELAY = 2

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


class Card:
    def __init__(self, attack: int = None, health: int = None,
                 is_bubbled: bool = False, is_poison: bool = False):
        self.attack = attack if attack is not None else random.randint(1, 50)
        self.health = health if health is not None else random.randint(1, 50)

        # if a card is bubbled, it ignores the first time it takes damage
        self.is_bubbled = is_bubbled

        # if a card has poison, it kills any card to which it does damage
        self.is_poison = is_poison

        self.is_dead = False
        self.has_attacked = False

    def __str__(self):
        '''This function allows us to easily print instances of Card class.
        If the card is bubbled, it adds 'b' after health. If the card has
        poison, it adds 'p' after attack'''

        atk_info = f"{str(self.attack) + 'p' * self.is_poison}"
        hlt_info = f"{str(self.health) + 'b' * self.is_bubbled}"
        return f"({atk_info: <{CARD_TXT_SPACE}}|{hlt_info: >{CARD_TXT_SPACE}})"

    def __repr__(self):
        '''Does the same as __str__'''

        return self.__str__()

    def takes_damage(self, other) -> None:
        '''This function changes the stats of the card based on the other
        card attack'''

        if self.is_bubbled:
            self.is_bubbled = False
            return

        if other.is_poison:
            self.health = 0
            self.is_dead = True
            return

        self.health -= other.attack
        if self.health <= 0:
            self.is_dead = True

    def do_attack(self, other) -> None:
        other.takes_damage(self)
        self.takes_damage(other)


class Board:
    def __init__(self, top: list[Card] = [], bottom: list[Card] = []):
        self.top = top  # top board
        self.bottom = bottom  # bottom board
        self.max_space = (CARD_TXT_SPACE * 2 + 5) * BOARD_LENGTH

    def populate_with_random_cards(self) -> None:
        self.top = []
        self.bottom = []

        for i in range(BOARD_LENGTH * 2):
            new_card = Card()

            # generating random bubble and poison probabilities
            poison = random.randint(1, 100)
            bubble = random.randint(1, 100)
            if poison <= POISON_PROB * 100:
                new_card.is_poison = True
            if bubble <= BUBBLE_PROB * 100:
                new_card.is_bubbled = True

            # populating top and bottom board
            if i % 2 == 0:
                self.top.append(new_card)
            else:
                self.bottom.append(new_card)

    def show(self, iter_num: int) -> None:
        '''Prints board (top board and bottom one) with some formatting'''

        if iter_num > 0:
            heading = f"Current Board on {iter_num} iteration"
        else:
            heading = "Starting Board"
        heading = f"{heading:-^{self.max_space}}"

        print(heading)
        print(self.top)
        print(self.bottom)
        print('-' * self.max_space)


class Game:
    def __init__(self, board: Board = None, verbalize: bool = True):
        self.is_top_move = True  # is it top-board's turn
        self.verbalize = verbalize  # if set to True then we print game text

        if board is None:
            new_board = Board()
            new_board.populate_with_random_cards()
            self.board = new_board
        else:
            self.board = board

    def run(self) -> None:
        '''Game loop with DELAY in seconds'''

        iter_num = 0
        self.board.show(iter_num)

        while self.board.top and self.board.bottom:
            iter_num += 1
            text = ""
            sleep(DELAY)

            attacker, attacked, brd, opp_brd = self.next_cards()
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
                brd.pop(atkr_idx)
            if attacked.is_dead:
                opp_brd.pop(atkd_idx)

            self.board.show(iter_num)

    def next_cards(self) -> (Card, Card, list[Card], list[Card]):
        '''Returns the card that attacks, the card that is being attacked by
        the first card and pointers to their boards respectively'''

        # Selecting correct boards based on 'is_top_move' attribute
        brd = self.board.top if self.is_top_move else self.board.bottom
        opp_brd = self.board.bottom if self.is_top_move else self.board.top

        # Selecting the first in order card that has not attacked yet
        # Then randomly selecting the attacked card
        for card in brd:
            if not card.has_attacked:
                card.has_attacked = True
                self.is_top_move = not self.is_top_move
                return (card, random.choice(opp_brd), brd, opp_brd)

        '''If all cards have attacked then set all card's properties
        'has_attacked' to false and try again to call this funciton'''
        for card in brd:
            card.has_attacked = False
        return self.next_cards()


if __name__ == '__main__':
    game = Game()
    game.run()
