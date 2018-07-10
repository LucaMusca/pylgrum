import unittest
from context import Player, Hand, Card, Suit, Rank, OverdealtHandError

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.p = Player()

    def test_initial_hand_size(self):
        self.assertEqual(self.p._hand.size(), 0)

    def test_receive_card(self):
        self.p.receive_card(Card(rank=Rank.TEN, suit=Suit.HEART))
        self.assertEqual(self.p._hand.size(), 1)

    def test_too_many_cards(self):
        self.p.receive_card(Card(rank=Rank.QUEEN, suit=Suit.HEART))    # 0 : QH
        self.p.receive_card(Card(rank=Rank.JACK, suit=Suit.DIAMOND))   # 1 : JD
        self.p.receive_card(Card(rank=Rank.ACE, suit=Suit.CLUB))       # 2 : AC
        self.p.receive_card(Card(rank=Rank.KING, suit=Suit.SPADE))     # 3 : KS
        self.p.receive_card(Card(rank=Rank.TWO, suit=Suit.HEART))      # 4 : 2H
        self.p.receive_card(Card(rank=Rank.THREE, suit=Suit.DIAMOND))  # 5 : 3D
        self.p.receive_card(Card(rank=Rank.FOUR, suit=Suit.CLUB))      # 6 : 4C
        self.p.receive_card(Card(rank=Rank.FIVE, suit=Suit.SPADE))     # 7 : 5S
        self.p.receive_card(Card(rank=Rank.TEN, suit=Suit.HEART))      # 8 : 10H
        self.p.receive_card(Card(rank=Rank.NINE, suit=Suit.DIAMOND))   # 9 : 9D
        self.p.receive_card(Card(rank=Rank.EIGHT, suit=Suit.CLUB))     # 10: 8C
        self.assertEqual(self.p._hand.size(), 11) ## a full hand

        with self.assertRaises(OverdealtHandError):
            self.p.receive_card(Card(rank=Rank.SEVEN, suit=Suit.SPADE)) 
        
if __name__ == '__main__':
    unittest.main()