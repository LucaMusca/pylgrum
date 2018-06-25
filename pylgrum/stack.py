"""CardStack class implementation."""
import random

from pylgrum import Card
from .errors import CardNotFoundError

class CardStack():
    """A base class for collections of cards (e.g. deck, hand, discard pile).

    CardStack supports basic operations on collections of cards. In order to
    maintain generality, CardStack allows duplicates of a given card.

    The "top" of the stack is the end of the list.

    Public methods:
     add(c)      : adds c to the top of stack
     size()      : number of cards in the stack
     remove(i)   : removes and returns the card a given index
     find(c)     : searches the stack for c
     draw(c)     : removes and returns the "top" card in the stack
     shuffle()   : re-orders cards in the stack
     __eq__()    : stacks are equal iff they have the same cards
                   in the same order
     __str__()

    """

    def __init__(self) -> None:
        self.cards = [] # List[Card]

    def size(self) -> int:
        """Number of cards in the stack."""
        return len(self.cards)

    def add(self, newcard: Card) -> None:
        """Add a card to the top of the stack."""
        self.cards.append(newcard)

    def remove(self, i: int) -> Card:
        """Remove and return the card at the given index.

        Raises: CardNotFoundError
        """
        try:
            target_card = self.cards[i]
        except IndexError:
            raise CardNotFoundError("Index value {} out of range".format(i))

        before_the_card = self.cards[0:i]
        after_the_card = self.cards[i+1:]
        self.cards = before_the_card + after_the_card
        return target_card

    def find(self, targetcard: Card) -> int:
        """find() searches the stack for a specified card and returns it.

        Args:
         c (Card): the card to search for.

        Returns:
         int : index in the stack to the card.

        Raises:
         CardNotFoundError: if specified card is not in the stack.
        """
        for (position, checked_card) in enumerate(self.cards):
            if checked_card.is_same_card(targetcard):
                return position
        raise CardNotFoundError("{} not found in stack".format(
            targetcard.__str__()))

    def draw(self) -> Card:
        """Remove and return the top card on the stack."""
        return self.cards.pop()

    def shuffle(self) -> None:
        """Randomly re-order the stack."""
        random.shuffle(self.cards)

    def __eq__(self, other) -> bool:
        """Stacks are equal iff they have the same cards in the same order."""
        return self.cards == other.cards

    def __str__(self) -> str:
        """Printing a stack returns its cards in top-to-bottom order.

        Note: this will be the opposite of the list order - i.e. index 0
        is the last card listed. This way the visible order corresponds to the
        human notion of the "top" of the stack.
        """
        cards_to_print = self.cards.copy()
        cards_to_print.reverse()
        r_str = ", ".join([c.__str__() for c in cards_to_print])
        return r_str