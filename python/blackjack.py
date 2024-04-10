import random
answer=input("Do you want to play the game of Blackjack ? Type y or n ")
if answer=="y":
  user_choice1=[]
  computer_choice1=[]
  user_score=0
  computer_score=0
  def operation_user(user_choice):
      global user_score
      for n1 in user_choice:
          if n1==1:
              user_score= user_score+user_choice[0]+user_choice[1]-n1+11
              if user_score==21:
                       user_score= user_score+user_choice[0]+user_choice[1]-n1+1            
          elif n1==11:
                   user_score= user_score+user_choice[0]+user_choice[1]-n1+10
          elif n1==12:
                   user_score= user_score+user_choice[0]+user_choice[1]-n1+10
          elif n1==13:
                   user_score= user_score+user_choice[0]+user_choice[1]-n1+10     
          else: 
                   user_score= user_score+n1
      return user_score 
  def operation_computer(computer_choice):
        global computer_score
        for n in computer_choice:
            if n==1:
                computer_score= computer_score+computer_choice[0]+computer_choice[1]-n+11
                if computer_score==21:
                   computer_score= computer_score+computer_choice[0]+computer_choice[1]-n+1
            elif n== 11:
               computer_score= computer_score+computer_choice[0]+computer_choice[1]-n+10
            elif n==12:
               computer_score= computer_score+computer_choice[0]+computer_choice[1]-n+10
            elif n==13:
               computer_score= computer_score+computer_choice[0]+computer_choice[1]-n+10
            else: 
               computer_score= computer_score+n
        return computer_score
  conti=False
  while not conti:
    user_choice1=random.sample(range(1,14),2)
    computer_choice1=random.sample(range(1,14),2)
    print(f"Your card: {user_choice1}, computer's card {computer_choice1[0]}")
    user_score1=operation_user(user_choice1)
    computer_score1=operation_computer(computer_choice1)
    if user_score1==21:
            print(f"Your final hand {user_choice1},computer first hand{computer_choice1[0]}")
            print(f"Your score{user_score1}, Computer's score {computer_score1}")
            print("You win")
            conti=True
    elif computer_score1==21:
            print(f"Your final hand {user_choice1},computer first hand{computer_choice1[0]}")
            print(f"Your score{user_score1}, Computer's score {computer_score1}")
            print("You lose")
            conti=True
    elif user_score1==21 and computer_score1==21:
        print(f"Your final hand {user_choice1},computer first hand{computer_choice1[0]}")
        print(f"Your score{user_score1}, Computer's score {computer_score1}")
        print("Draw")
        conti=True
    elif user_score1>21:
        print(f"Your final hand :{user_choice1},computer first hand :{computer_choice1[0]}")
        print(f"Your score :{user_score1}, Computer's score: {computer_score1}")
        print("You went over. you loose")
        conti=True
    elif computer_score1<16:
        computer_choice2=random.randint(1,14)
        computer_choice1.append(computer_choice2)
        operation_computer(computer_choice=computer_choice1)
    start=input("Type y if you want to continue and n to stop ")
    if start=="y":
        user_choice2=random.randint(1,14)
        user_choice1.append(user_choice1)
        operation_user(user_choice=user_choice1)        
    elif start=="n":
        conti==True
        print(f"Your final hand {user_choice1},computer first hand{computer_choice1[0]}")
        if user_score> computer_score:
            print(f"Your final hand {user_choice1},computer first hand{computer_choice1[0]}")
            print(f"Your score{user_score1}, Computer's score {computer_score1}")
            print("You win")
            conti=True
        else:
            print(f"Your final hand {user_choice1},computer first hand{computer_choice1[0]}")
            print(f"Your score{user_score1}, Computer's score {computer_score1}")
            print("You lose")
            conti=True 





