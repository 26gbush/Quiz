questions = ("What is the most popular programming language as of April 12th 2024? (it is NOT the thing this quiz is coded in): ",
                       "What is the square root of 5 x 4 / 578384?: ",
                       "What is the coding language Minecraft BEDROCK runs on?: ",
                       "Which planet is the farthest from Earth?: ",
                       "Which planet in the solar system is the hottest?: ",
             "What is the sphere of the Earth that contains life?: ")

options = (("A. C++", "B. Python", "C. Java Script", "D. HTML/CSS", "E. Block Coding/Scratch"),
                   ("A. I have no idea", "B. 0.00001546424", "C. 2", "D. 0.00001546425", "E. 0.5"),
                   ("A. Java Script", "B. Java", "C. Python", "D. Bedrock", "E. C++"),
                   ("A. Neptune", "B. Mercury", "C. Mars", "D. Uranus", "E. Pluto"),
                   ("A. Venus", "B. Mercury", "C. Earth", "D. Mars", "E. Uranus"),
          ("A. Hydrosphere", "B. Biosphere", "C. Atmosphere", "D. Geosphere", "E. Atmostsphere"))

answers = ("C", "B", "E", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D, E): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
