import random

def rockpaperscissors(user_input, computer):
    if ((user_input == "rock") & (computer == "rock")):
        print("The computer threw rock. Rock and rock ends in a draw.")
    elif((user_input == "scissor") & (computer == "scissor")):
        print("The computer threw scissor. scissor and scissor ends in a draw.")
    elif((user_input == "paper") & (computer == "paper")):
        print("The computer threw paper. paper and paper ends in a draw.")
  
    elif((user_input == "rock") & (computer == "scissors")):
        print("The compter threw scissors. Rock versus scisssor, you win!")
    elif((user_input == "scisssors") & (computer == "paper")): 
        print("The computer threw paper. scissors versus paper, you win!") 
    elif((user_input == "paper") & (computer == "rock")): 
        print("The computer threw rock. paper versus rock, you win!") 

    elif((user_input == "scissors") & (computer == "rock")): 
        print("The computer threw rock. scissors versus rock, computer wins!") 
    elif((user_input == "rock") & (computer == "paper")): 
        print("The computer threw paper. Rock versus paper, computer wins!")
    elif((user_input == "paper") & (computer == "scissor")): 
        print("The computer threw scissors. paper versus scissor, computer wins!")
    
rock = "rock"
paper = "paper"
scissor = "scissor"

list = [ rock, paper, scissor]

computer = random.choice(list)

#user = input("Rock. Paper. Scissor. Shoot")

#rockpaperscissors(user,computer)

prompt = input("Would you like to play Rock, Paper, Scissor? Y/N:  ")
prompt = prompt.upper()

while prompt == 'Y':
    user_input = input ("Rock. Paper. Scissors. Shoot!:  ")
    rockpaperscissors(user_input, computer)
    print ()
    computer = random.choice(list)
    prompt = input ("Would you like to play another round? Y/N:  ").upper()




