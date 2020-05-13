
import random





class Card(object):
    """
        A representation of card object
    """

    def __init__(self):
        """
            Parameters: None
        """
        pass

    def play(self, player, game):
        """ This is introduction of process in playing the cards.
            When player put out one card, it will take one new card in deck.
        """
        player.get_hand().get_cards().remove(self)
        card = game.pick_card()
        player.get_hand().add_cards(card)
        game.set_action("NO_ACTION")
               

    def action(self, player, game, slot):
        """
            Parameters: None
        """
        pass
        
    def __str__(self):
        return "Card()"


    def __repr__(self):
        return "Card()"
        


class NumberCard(Card):
    """
        A representation of NumberCard
    """   
    def __init__(self, number):
        """
            Funcation:
                       Transfer parameters
            Parameters:
                        Number
            Return:
                    None
        """
        self._number = number
        
    def get_number(self):
        """
            Function:
                     Return the card's number
            Parameter:
                     None
            Return:
                    The card's number
        """
            
        return self._number

    def play(self, player, game):
        """
            This is introduction of process in playing the cards.
            When player put out one card, it will take one new card in deck.
        """
        player.get_hand().get_cards().remove(self)
        card = game.pick_card()
        player.get_hand().add_cards(card)
        game.next_player()
        game.set_action("NO_ACTION")
    
    def __str__(self):
        return "NumberCard({})".format(self._number)


    def __repr__(self):
        return "NumberCard({})".format(self._number)
        

class TutorCard(Card):
    """
        A representation of TutorCard
    """
    def __init__(self, name):
        """
            Patameters:
                        name(str): The pattern's name.
        """
        self._pattern = name
        
    def get_name(self):
        """
            (str) Return the name
        """
        return self._pattern

    def play(self, player, game):
        """
            Move the next the player, and set action.
        """
        super().play(player, game)
        game.set_action("PICKUP_CODER")

    def action(self, player, game, slot):
        """
                The sleeping_card which the player chooses need be obtained
            And then, remove it from the card's deck put it into player's hand.
            At last, move to another player.
        """
        super().action(player, game, slot)
        card = game.get_sleeping_coder(slot)
        game.set_sleeping_coder(slot,None)
        player.get_coders().add_card(card)
        game.set_action("NO_ACTION")
        game.next_player()
               

    def __str__(self):
        return "TutorCard({})".format(self._pattern)

    def __repr__(self):
        return "TutorCard({})".format(self._pattern)

class CoderCard(Card):
    """This class has three arguements: Cards, Player, Sleeping coder.
    """
    def __init__(self, name):
        """
            Parameters:
                        The name
        """
        self._name = name

    def get_name(self):
        """
            (int) Return the name
        """
        return self._name

    def play(self, player, game):
        """
            Just set action
        """
        game.set_action("NO_ACTION")

    def action(self, player, game, slot):
        """
            Parameters: None
        """
        pass
    
    def __str__(self):
        return "CoderCard({})".format(self._name)

    def __repr__(self):
        return "CoderCard({})".format(self._name)
         
class KeyboardKidnapperCard(Card):
    """
        A representation of KeyboardKidnapperCard
    """
    def play(self, player, game):
        """
            This is introduction of process in playing the cards.
            When player put out one card, it will take one new card in deck.
        """
        super().play(player, game)
        game.set_action("STEAL_CODER")
        
    def action(self, player, game, slot):
        """
                The sleeping_card which the player chooses need be obtained
            And then, remove it from the card's deck put it into player's hand.
            At last, move to another player.
        """        
        super().action(player, game, slot)        
        card = player.get_coders().get_card(slot)
        player.get_coders().remove_card(slot)
        game.current_player().get_coders().add_card(card)
        game.set_action("NO_ACTION")
        game.next_player()
        
    def __str__(self):
        return "KeyboardKidnapperCard()"
    
    def __repr__(self):
        return "KeyboardKidnapperCard()"

class Deck(object):
    """
            A representation of the card's deck
            It can show the player's hand cards, coder cards, remove_card,
        sleeping coder.
    """
    def __init__(self, starting_cards=None):
        """
            Parameters: judge the starting card whether none
        """
        if starting_cards == None:
            self._starting_card = []
        else:
            self._starting_card = starting_cards

    def get_cards(self):
        """
            (int) Return the card
        """
        card = self._starting_card
        return card
    
    def get_card(self, slot):
        """
            (int) Return the starting card
        """
        return self._starting_card[slot]

    def top(self):
        """
            It return the last one card in starting_card
            (int) Return get_cards
        """
        return self.get_cards()[-1]

    def remove_card(self, slot):
        """
            remove the starting card in the list
        """
        del self._starting_card[slot] 
    
    def get_amount(self):
        """
            (int) Return the total card
        """            
        return len(self.get_cards())

    def shuffle(self):
        """
            This function can rearrange the card's deck
        """
        random.shuffle(self.get_cards())

    def pick(self, amount = 1):
        """
            (int) Return the picking card
        """
        pick_card = self._starting_card[-1:-amount -1 :-1]
        self._starting_card = self._starting_card[0:-amount:1] 
        return pick_card            

    def add_card(self, card):
        """
            This function can put the card into the starting_cards
        """
        self.get_cards().append(card)

    def add_cards(self, cards):
        """
                This function is that make the cards become the list, and then
            put them into the starting_cards.
        """
        self.get_cards().extend(cards)

    def copy(self, deck):
        """
            This function copy all cards in other deck into this deck
        """
        self.add_cards(deck.get_cards())

    def __str__(self):
        string="Deck({})".format(self._starting_card)
        string=string.replace("[", "")
        string=string.replace("]", "")
        return string
       
    def __repr__(self):
        string="Deck({})".format(self._starting_card)
        string=string.replace("[", "")
        string=string.replace("]", "")
        return string

class Player(object):
    """
        A representation of Player
    """

    def __init__(self, player_name):
        """
            Transfer the cards in the hand and coder's hand
            Parameters: The player's name, hand card and coder card            
        """
        self._player_name = player_name
        self._hand = Deck()   
        self._coder = Deck() 

    def get_name(self):
        """
            (int) Return the player name
        """
        return self._player_name

    def get_hand(self):
        """
            (int) Return the hand card
        """
        return self._hand

    def get_coders(self):
        """
            (int) Return the coder card
        """
        return self._coder

    def has_won(self):
        """
            If player has more than three cards
        the player will win and game over.
            Function:
                    judge who is a wineer.
            Parameter:
                    coders cards
            Return:
                    If player has more than three cards, it will become the winner
                
        """
        coders_card = self.get_coders().get_amount()
        if coders_card > 3:
            return True
        else:
            return False

    def __str__(self):

        return "Player({})".format(self._player_name + ", " + str(self._hand) + ", " + str(self._coder)) 
    def __repr__(self):
        return "Player({})".format(self._player_name + ", " + str(self._hand) + ", " + str(self._coder))

class AllNighterCard(Card):
    """
        A representation of AllNighterCard
    """        
    def __init__(self):
        """
            Parameters: None
        """
        pass

    def play(self, player, game):
        """
            This is introduction of process in playing the cards.
            When player put out one card, it will take one new card in deck.
        """        
        super().play(player, game)
        game.set_action("SLEEP_CODER")

    def action(self, player, game, slot):
        """
                The sleeping_card which the player chooses need be obtained
            And then, remove it from the card's deck put it into player's hand.
            At last, move to another player.
        """
        card = player.get_coders().get_card(slot)
        player.get_coders().remove_card(slot)
        index = game.get_sleeping_coders().index(None)
        game.set_sleeping_coder(index,card)
        game.set_action("NO_ACTION")
        game.next_player()
        
    def __str__(self):
        return "AllNighterCard()"

    def __repr__(self):
        return "AllNighterCard()"
            
            
def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
