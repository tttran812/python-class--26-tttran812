# CS 31 Trang T. 10/7/2026

print ("My Easy A Math Quiz")
print("* " * 20) # print a line of 20 astericks

print()
username = input("What is your name? ")
print(f"Hello, {username}!") # f-string format

print()
start_quiz = input("Would you like to take this Easy A Math quiz? Y/N ")
if start_quiz.upper() == "Y":
    print("Great! Let's get started!")

    counter = 0

    # Question 1
    print()
    q1 = int(input("1. What is 10-1?"))
    if q1 == 9:
      # update my counter
      counter += 1 
      print("Yes! You are correct. The answer is 9.")
    else:
      print("Sorry. That is incorrect. ")

    # Question 2 
    print() 
    q2 = int(input("2. What is 6+4?")) 
    if q2 == 10: 
      counter += 1  
      print("Yes! You are correct. The answer is 10.") 
    else:  
      print("Sorry. That is incorrect. ")

    # Question 3 
    print() 
    q3 = int(input("3. What is 7-5?")) 
    if q3 == 2: 
      counter += 1  
      print("Yes! You are correct. The answer is 2.") 
    else:  
      print("Sorry. That is incorrect. ") 

    # Question 4 
    print() 
    q4 = int(input("4. What is 2+3?")) 
    if q4 == 5: 
      counter += 1  
      print("Yes! You are correct. The answer is 5.") 
    else:  
      print("Sorry. That is incorrect. ")

    # Question 5 
    print() 
    q5 = int(input("What is 9-8?")) 
    if q5 == 1: 
      counter += 1  
      print("Yes! You are correct. The answer is 1.") 
    else:  
      print("Sorry. That is incorrect. ") 

    # Output the score 
    print() 
    print("* * * * YOUR FINAL SCORE * * * *") 
    print(f"{username}, your final score is: {counter} out of 5.") 

    if counter == 5:
      print ("You are a rockstar! You got them all correct!")
    elif counter >= 3 and counter < 5: 
      print("Great work!")
    elif counter >= 1 and counter < 3:
      print("Keep studying and try again!")
    else:
      print("Maybe this isn't your area of interest.")  

elif start_quiz.upper() == "N": 
    print("Sorry, maybe next time!")
    exit()

else: # if they type anything else tell them its invalid 
  print("Sorry. That is an invalid response. Try again")
  exit()

print("Thanks and have a great day!")

