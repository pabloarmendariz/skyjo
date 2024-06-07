import numpy as np
import random

class Pack:
    def __init__(self, nb_players) -> None:
        self.pack = self.get_pack()
        self.nb_players = nb_players
        self.cards_per_player = 12

    @classmethod
    def create_set(self):
        minus_twos = np.full(5, -2)
        minus_ones = np.full(10, -1)
        zeros = np.full(15, 0)
        other_cards = np.concatenate([np.full(10,x) for x in range(1,13)])
        final_set = np.concatenate((minus_twos,minus_ones,zeros,other_cards))
        return final_set
    
    def get_pack(self):
        set = self.create_set()
        random.shuffle(set)
        return set
    
    def distribute_cards(self):
        total_cards_to_distribute = self.cards_per_player * self.nb_players
        self.hands = [[] for _ in range(self.nb_players)]

        for i in range(total_cards_to_distribute):
            player_index = i % self.nb_players
            card_index = i
            self.hands[player_index].append(self.pack[card_index])
        
        self.pack = self.pack[total_cards_to_distribute:]
        #TODO remove those cards from the pack

        #if you need numpy arrays, add this
        # self.hands = [np.array(player) for player in hands]

        #if you want to print the hands, add this
        # for i, player in enumerate(self.hands):
        #     print(f"Player {i+1}'s cards: {player}")


if __name__ == "__main__":
    pack = Pack(2)
    print(pack.pack)
    pack.distribute_cards()
    print(pack.hands)
    print(pack.pack)



