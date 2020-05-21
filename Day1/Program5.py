# Take input of runs scored by 3 players on 60 balls each and print following scored cards:
#1.Strike rate of each.
#2.What will be the runs score if they played 60 balls more ?
#3.What is the maximum number of sixes each players could have hit?


player1 = int(input("Enter the runs for player 1 : "))
player2 = int(input("Enter the runs for player 2 : "))
player3 = int(input("Enter the runs for player 3 : "))
strikerate1 =player1 * 100 / 60
strikerate2 =player2 * 100 / 60
strikerate3 =player3 * 100 / 60
print("Strike rate of player 1 is :-",strikerate1)
print("Strike rate of player 2 is :-",strikerate2)
print("Strike rate of player 3 is :-",strikerate3)
print("Runs scored by player 1 if they played 60 more balls is :-",player1 * 2)
print("Runs scored by player 2 if they played 60 more balls is :-",player2 * 2)
print("Runs scored by player 3 if they played 60 more balls is :-",player3 * 2)
print("Maximum number of sixes player 1 could hit :-",player1 // 6)
print("Maximum number of sixes player 2 could hit :-",player2 // 6)
print("Maximum number of sixes player 3 could hit :-5",player3 // 6)
