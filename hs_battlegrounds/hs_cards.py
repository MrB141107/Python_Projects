from base_card import Card

if_base_card = True
inherited_class = Card


class Annoy_o_Tron(inherited_class):
    name = 'Annoy-o-Tron'

    def __init__(self):
        super().__init__(attack=1, health=2)
        self.is_bubbled = True
        self.is_taunt = True


class Dozy_Whelp(inherited_class):
    name = 'Dozy Whelp'

    def __init__(self):
        super().__init__(attack=0, health=3)
        self.is_taunt = True

    def before_attacked(self, other):
        self.attack += 1


class Micro_Mummy(inherited_class):
    name = 'Micro Mummy'

    def __init__(self):
        super().__init__(attack=1, health=2)
        self.is_reborn = True


def get_cards() -> dict:
    cards = dict()
    def_classes = [Card, inherited_class]  # excluding this classes from list
    global_objs = list(globals().items())

    for name, obj in global_objs:
        if obj not in def_classes and isinstance(obj, type):
            cards[obj.name] = obj

    return cards
