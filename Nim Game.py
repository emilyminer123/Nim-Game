"""
@author: Emily Miner
"""

piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, equal to the length of piles


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:
            print("You won this time, but it won't happen again.")
            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:
            print("I won, but are we really suprised?")
            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles
    
    print("We're going to play Nim.  You'd better play optimally or I'll win.")
    num_piles = int(input("How many piles do you want to play with?"))
    for i in range(num_piles):
        piles += [int(input("How many in pile "+str(i)+"? "))]
    
        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles

    for i in range(num_piles):
        print("pile ",i," = ",piles[i]) 


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] += -amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles

    a = int(input("Which pile? "))
    while a < 0 or a >= num_piles:
        a = int(input("Not a valid pile. Try again."))
    return a
    

def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles
    
    a = int(input("How many? "))
    while a < 1 or a >(piles[pnum]):
        a = int(input("Not a valid amount to remove. Try again."))
    return a


def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles 
    
    nim_sum = piles[0]
    L = []
    for i in range(1,num_piles):
        nim_sum = nim_sum^(piles[i])
    return nim_sum


def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles 
    pile_sums = []
    
    nim_sum = game_nim_sum()
    for i in range(num_piles):
        pile_sums += [(piles[i])^nim_sum]
    for i in range(num_piles):
        if pile_sums[i] < piles[i]:
            return i, piles[i]-pile_sums[i]
    for i in range(num_piles):
        if piles[i] != 0:
            return i,1

def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles

    print("It's now my turn, hmmmm...")
    p,n = opt_play()
    piles[p] = piles[p] - n
    print("I remove ",n," from pile ",p)


#   start playing automatically
if __name__ == "__main__" : play_nim()
