from random import randint
player_wins = 0
computer_wins = 0
winning_score = 2

while player_wins < winning_score and computer_wins < winning_score:
       print(f"Player Wins :  {player_wins} Computer Wins : {computer_wins}")
       print(" . . .rock. . . ")
       print(" . . .paper. . . ")
       print(". . .Scissor. . .")
       print("      ")
                            
       player = input("Player, make your move : ").lower()
       if player == "quit" or player == "q":
              break

       print("      \n")

       rand_num = randint(0,2)
       if rand_num == 0:
              computer = "rock"
       elif rand_num == 1:
              computer = "paper"
       else:
              computer= "scissor"

       print(f"Computer plays :  {computer}" )

       if player == computer:
              print("It's Tie man!")
       elif player == "rock":
              if computer == "paper":
                     print(" Booom computer Wins ")
                     computer_wins += 1
              else:
                     print(" Boom Player wins")       
                     player_wins += 1
       elif player == "paper":
              if computer == "rock":
                     print("Boom Player  wins") 
                     player_wins += 1
              else:
                     print("Boom computer wins")              
                     computer_wins += 1
       elif player == "scissor":
              if computer == "rock":
                     print("Boom computer wins")
                     computer_wins += 1
              else:
                     print("Boom Player wins")           
                     computer_wins += 1
       else:
              print(" Something went wrong, Please restart Again")       

if player_wins > computer_wins:
       print("CONGRATS, You Won!")

elif player_wins == computer_wins:
       print("IT'S A TIE")        
else:
       print("OH NO :( THE COMPUTER WON ...")                     


              


       