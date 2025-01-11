score = int(input ("enter your score: ")) #changing score to integer
name = input("Enter your name: ")
# score = input("enter your score")
# if score >= 70 and score <= 100:
#     print (f"{name}, Your score is {score}, Your get an A")
# elif score >= 60 and score < 70:
#     print (f"{name}, Your score is {score}, You get a B")
# elif score >= 50 and score < 60:
#     print (f"{name}, Your score is {score}, You get a C")
# elif score >= 40 and score < 50:
#     print (f"{name}, Your score is {score}, You get a D")
# elif score >= 30 and score < 40:
#     print (f"{name}, Your score is {score}, You get an E")
# elif score >= 0 and score < 30:
#     print (f"{name}, Your score is {score}, you get an F")
# else:
#     print(f"{name}, Your score is {score}, Invalid Score")

if score >= 70 and score <= 100:
    message = f"{name}, Your score is {score}, Your get an A"
elif score >= 60 and score < 70:
    message = f"{name}, Your score is {score}, You get a B"
elif score >= 50 and score < 60:
    message = f"{name}, Your score is {score}, You get a C"
elif score >= 40 and score < 50:
    message = f"{name}, Your score is {score}, You get a D"
elif score >= 30 and score < 40:
    message = f"{name}, Your score is {score}, You get an E"
elif score >= 0 and score < 30:
    message = f"{name}, Your score is {score}, you get an F"
else:
    message = f"{name}, Your score is {score}, Invalid Score"
print(message)


