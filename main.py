questions = ("What is the most popular programming language as of April 12th 2024? (it is NOT the thing this quiz is coded in): ",
                       "What is the square root of 5 x 4 / 578384?: ",
                       "What programming language does Minecraft BEDROCK run on?: ",
                       "Which planet is the farthest from Earth?: ",
                       "Which planet in the solar system is the hottest?: ",
             "Which sphere of the Earth that contains life?: ",
             "What is Scale of The Universe?: ",
             "What is 0 divided by 0?: ",
             "What is the difference between coding and programming?: ",
             "Which Programming language does this quiz use?: ",
            "What is my most popular project on github ( as of 4/18/24)?: ",
            "What is the most downloaded game of all time?: ",
            "What is the most popular web browser?: ",)

options = (("A. C++", "B. Python", "C. JavaScript", "D. HTML/CSS", "E. Block Coding/Scratch"),
                   ("A. I have no idea", "B. 0.00001546424", "C. 2", "D. 0.00001546425", "E. 0.5"),
                   ("A. Java Script", "B. Java", "C. Python", "D. Bedrock", "E. C++"),
                   ("A. Neptune", "B. Mercury", "C. Mars", "D. Uranus", "E. Pluto"),
                   ("A. Venus", "B. Mercury", "C. Earth", "D. Mars", "E. Uranus"),
          ("A. Hydrosphere", "B. Biosphere", "C. Atmosphere", "D. Geosphere", "E. Atmostsphere"),
          ("A. A tool to find code", "B. A calculator", "C. A tool to Find the ratio of Earth", "D. A tool to find the scale of things in the universe", "E. IDK"),
          ("A. 82", "B. 69", "C. 0", "D. 1", "E. Undefined"),
          ("A. Coding uses higher level thinking", "B. Prographing uses higher level thinking", "C. Programming uses higher level thinking", "D. Programming is very easy to understand", "E. They are the same"),
          ("A. Python", "B. Java", "C. Java Script", "D. HTML/CSS/PHP", "E. C++"),
          ("A. Calculator", "B. Quiz", "C. 26gbush README.md", "D. IDK", "E. MATH"),
          ("A. Minecraft", "B. Roblox", "C. Tetris", "D. GTA 5", "E. Pac-Man"),
          ("A. Edge", "B. Chrome", "C. Firefox", "D. Opera", "E. Brave"),)

answers = ("C", "B", "E", "A", "A", "B", "D", "E", "C", "A", "B", "A", "B")
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
