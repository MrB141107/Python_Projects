import random
from base_card import Card
import config as cfg


class Board:
    def __init__(self, top: list[Card] = [], bottom: list[Card] = []):
        self.top = top  # top board
        self.bottom = bottom  # bottom board
        self.max_space = (cfg.CARD_TXT_SPACE * 2 + 5) * cfg.BOARD_LENGTH

    def populate_with_random_cards(self) -> None:
        self.top = []
        self.bottom = []

        for i in range(cfg.BOARD_LENGTH * 2):
            new_card = Card()

            # generating random bubble and poison probabilities
            poison = random.randint(1, 100)
            bubble = random.randint(1, 100)
            if poison <= cfg.POISON_PROB * 100:
                new_card.is_poison = True
            if bubble <= cfg.BUBBLE_PROB * 100:
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
