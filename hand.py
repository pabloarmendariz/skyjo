from typing import Literal

class Card:
    def __init__(self, value:int, hidden:bool=True):
        self.value  = value
        self.hidden = hidden
    
    def flip_card(self) -> None:
        self.hidden = True

class Column:
    def __init__(self, removed:bool=False):
        self.removed = removed
        self.values = [None, None, None]
    
    def verify_removal(self) -> None:
        all_cards_are_flipped = all([~card.hidden for card in self.values])
        all_cards_are_the_same = all(self.values)
        self.removed = all_cards_are_the_same and all_cards_are_flipped
    
    def update_value(self, value:Card, position:Literal[1,2,3]):
        self.values[position-1] = value
    
    def remove_column(self):
        """
        Before removing the cards from the column, 
        """
        cards_to_discards = self.values
        self.values = None
        return cards_to_discards

class Hand:
    def __init__(self):
        self.column_1 = Column()
        self.column_2 = Column()
        self.column_3 = Column()
        self.column_4 = Column()
    
    def fill_hand(self, cards:list):
        # TODO find a way to place cards in the hand.
        """
        columns = [self.column_1, self.column_2]
        for i, card in enumerate(cards):
        """
        pass
    

    

