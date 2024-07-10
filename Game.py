# My card game

from getpass_asterisk.getpass_asterisk import getpass_asterisk
import random

def authorise(player, password):  # Function to compare many players easily.
    player_authorised = False
    #Searching for username and password in array.
    for (y, x) in authorised_players:
        if player == y and password == x: 
            player_authorised = True 
            retry = False # Will be used later to allow the user to re-enter details if incorrect.
    return player_authorised

def getCredentialsAndAuthorise(playerName,used_usernames):
    retry = True  #Gives the users an option to try entering their details again.
    # Keep track of already used usernames
    while retry == True:
        playerUserId = input(playerName + ", enter your username: ")
        usernameForLater = playerUserId
        # Check for duplicate usernames
        if playerUserId in used_usernames:
            print("This username is already taken. Please choose a different one.")
            continue  # Skip to the next iteration of the loop
        else:
            used_usernames.append(playerUserId)
        password = getpass_asterisk("Enter your password: ")
        player_authorised = authorise(playerUserId, password)
        if player_authorised == True: #Checks if the user has been authorised before continuing.
            print("Welcome", playerUserId)
            retry = False
        else:
            print("Username or password is incorrect.")
            retry1 = input("Would you like to retry: ").title()
            if retry1 == "Yes":
                retry = True
            else:
                retry = False
                print("Game has shut down.")
                exit(0)
    return usernameForLater



def shuffle():
    while len(deck) != 0:
        card = random.choice(deck)
        shuffled_deck.append(card)
        deck.remove(card)

def pickingOfCards(player1, player2, player1_cards, player2_cards):
    while len(shuffled_deck) > 0:
        player1Pick = input("Player 1, enter 'Pick' to pick a card: ").title()
        if player1Pick == "Pick":
            cardP1 = [shuffled_deck.pop(-1)]
        else:
            print("Player 1 has not picked a card\nA card has been picked.")
            cardP1 = [shuffled_deck.pop(-1)]
        player2Pick = input("Player 2, enter 'Pick' to pick a card: ").title()
        if player2Pick == "Pick":
            cardP2 = [shuffled_deck.pop(-1)]
        else:
            print("Player 2 has not picked a card\nA card has been picked.")
            cardP2 = [shuffled_deck.pop(-1)]
        print("Player 1 card:", cardP1, "\nPlayer 2 card:", cardP2)
        for (colour1, num1) in cardP1:
            for (colour2, num2) in cardP2:
                if colour1 == colour2:
                    if num1 > num2:
                        player1 += 1
                        player1_cards.append(cardP1)
                        player1_cards.append(cardP2)
                        print("Player 1 has won a point.")
                    else:
                        player2 += 1
                        player2_cards.append(cardP1)
                        player2_cards.append(cardP2)
                        print("Player 2 has won a point.")
                elif colour1 == "R" and colour2 == "B":
                    player1 += 1
                    player1_cards.append(cardP1)
                    player1_cards.append(cardP2)
                    print("Player 1 has won a point.")
                elif colour1 == "B" and colour2 == "R":
                    player2 += 1
                    player2_cards.append(cardP1)
                    player2_cards.append(cardP2)
                    print("Player 2 has won a point.")
                elif colour1 == "Y" and colour2 == "R":
                    player1 += 1
                    player1_cards.append(cardP1)
                    player1_cards.append(cardP2)
                    print("Player 1 has won a point.")
                elif colour1 == "R" and colour2 == "Y":
                    player2 += 1
                    player2_cards.append(cardP1)
                    player2_cards.append(cardP2)
                    print("Player 2 has won a point.")
                elif colour1 == "B" and colour2 == "Y":
                    player1 += 1
                    player1_cards.append(cardP1)
                    player1_cards.append(cardP2)
                    print("Player 1 has won a point.")
                elif colour1 == "Y" and colour2 == "B":
                    player2 += 1
                    player2_cards.append(cardP1)
                    player2_cards.append(cardP2)
                    print("Player 2 has won a point.")
        print(player1)
        print(player2)
    if player1 > player2:
        numCards = len(player1_cards)
    else:
        numCards = len(player2_cards)
    return numCards


def decidingwinner(player1N, player2N):
    if len(player1_cards) > len(player2_cards):
        print("End of game\nPlayer 1 has won the game\nPlayer 1 cards:",
              player1_cards)
        winner = player1N
    else:
        print("End of game\nPlayer 2 has won the game\nPlayer 2 cards:",
              player2_cards)
        winner = player2N
    return winner


#Game starts here
used_usernames = []
player1Name = getCredentialsAndAuthorise("Player 1",used_usernames)
player2Name = getCredentialsAndAuthorise("Player 2",used_usernames)

player1 = 0
player1_cards = []

player2 = 0
player2_cards = []
shuffle()
numberofcards = pickingOfCards(player1, player2, player1_cards, player2_cards)
winner = decidingwinner(player1Name, player2Name)
print(winner,"has won the game!!!!")

winnersFile = open("winners.txt", "a")
winnersFile.write(f"{winner},{numberofcards}\n")
winnersFile.close()

winners = []
winnersFile = open("winners.txt", "r")
for winnerAndCards in winnersFile:
    winners.append(str(winnerAndCards).removesuffix("\n").split(","))
winnersFile.close()

# winners.sort(key=sortKeyFunc)
sortedWinners = sorted(winners, key=lambda x: int(x[1]), reverse=True)

print("Top 5 Winners")
for [x,y] in sortedWinners[0:5]:
 print(f"Player:{x} Score:{y}")

