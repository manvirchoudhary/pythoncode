
print(" . . .rock. . . ")
print(" . . .paper. . . ")
print(". . .Scissor. . .")
print("      ")

player1 = input("Player 1, make your move : ")
print("No Cheating!\n\n" * 20)
player2 = input("Player 2, make your move: ")
print("      ")
print(" Shoot!")

if player1 == player2:
       print("It's Tie man!")
elif player1 == "rock":
       if player2 == "paper":
              print(" Booom Player 2 Wins ")
       elif player2 == "scissor":
              print(" Boom Player 1 wins")       
elif player1 == "paper":
       if player2 == "rock":
              print("Boom Player 1 wins") 
       elif player2 == "scissor":
              print("Boom Player 2 wins")              
elif player1 == "scissor":
       if player2 == "rock":
              print("Boom Player 2 wins")
       elif player2 == "paper":
              print("Boom Player 1 wins")           
else:
       print(" Something went wrong, Please restart Again")       

            


    