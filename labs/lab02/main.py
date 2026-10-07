# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
# CS 31 Trang T. 10/7/2026

# Print out title 
print() # prints an empty line
print ("My Awesome Quiz on Python Concepts")
print() # prints an empty line
print("* " * 20) # print a line of 20 astericks

#Ask for the user's name
print()
username = input("What is your name? ")
print(f"Hello, {username}!") # f-string format

# Ask if they want to take a quiz

print()
start_quiz = input("Do you want to take my awesome quiz? Y/N ")
if start_quiz == "Y": # this will make any lowercase input into an uppercase comparison
  print(Great! Let's get started!")
  #put our quiz questions here all indented
  
# START OUR QUIZ QUESTIONS
# Set our counter to 0
        
elif start_quiz == "N":
  print("Sorry, maybe next time!")

else: # if they type anything else tell them its invalid
  print("Sorry. That is an invalid response. Try again.")
