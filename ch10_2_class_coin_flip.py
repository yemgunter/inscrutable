# Ch 10.2 Classes Coin Flip

import coin

def main():
    # create an object from the Coin class

    call_the_toss()

def call_the_toss():
    # Get prediction from two players
    player1_guess = input("heads or tails? ")
    player2_guess = input("heads or tails? ")

    # toss the coin
    a_coin = Coin()
    a_coin.toss()

    # decide who got it right and display result
    if player1_guess == a_coin.get_sideup():
        print("Player 1 is correct")
    else:
        print("Payer 1 is not correct")

    if player2_guess == a_coin.get_sideup():
        print("Player 2 is correct")
    else:
        print("Payer 2 is not correct")
  

main()
    
