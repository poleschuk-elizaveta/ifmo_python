#coding: utf-8
from random import shuffle


class Cards():
    deckOfCards = [x for x in range(2, 54)]
    shuffled_cards = []
    def __init__(self):
        pass

    def shuffle_cards(self):
        d = self.deckOfCards
        shuffle(d)
        for i in d:
           self.shuffled_cards.append(i)
        return self.shuffled_cards

    def give_cards(self, player): #раздать карты
        for i in range(0, 6):
            player.my_cards.append(self.shuffled_cards.pop(i))
            if len(player.my_cards) == 6:
                break
        return player.my_cards

    def trump_card(self): #определить козырь
        pass


class Player():
    my_cards = []
    score = 0

    def make_a_move(self): #сделать ход
        pass

    def take_cards(self): #добрать карты
        pass


class Card(Cards):
    my_cards = []

deck = Cards()
player_1 = Player()
player_2 = Player()

deck.shuffle_cards()
player_1_cards = deck.give_cards(player_1)
print deck.shuffle_cards()
print player_1_cards