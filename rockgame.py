
print(" . . .rock. . . ")
print(" . . .paper. . . ")
print(". . .Scissor. . .")
print("      ")

player1 = input("Player 1, make your move : ")
player2 = input("Player 2, make your move: ")

print("      ")
print(" Shoot!")


if  "rock" == player1 and "paper" == player2 : 
       print(" Booom Player 2 Wins ")
elif "rock" == player2 and "paper" == player1:
       print(" Boom Player 1 Wins")
elif "paper" == player1 and "scissor" == player2:
       print(" Boom Player 2 Wins")  
elif "paper" == player2 and "scissor" == player1:
       print(" Boom Player 1 Wins")
elif "rock" == player1 and "scissor" == player2:
       print(" Boom Player 1 Wins")
elif "rock" == player2 and "scissor" == player1:       
       print(" Boom Player 1 Wins")           
else:
       print(" Don't Cheat , Please restart Again")       

            


    